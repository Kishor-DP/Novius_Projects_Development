import unittest
from unittest.mock import MagicMock, patch
from opcua import ua
from Insert_Into_Temperature.opcua_modules import OpcUaNodeScanner, OpcUaDataReceiver
from utils.train_entry_timestamp import train_entry_timestamp

class TestOpcUaNodeScanner(unittest.TestCase):

    @patch('Insert_Into_Temperature.opcua_modules.Client')
    def test_connect(self, MockClient):
        mock_client_instance = MockClient.return_value
        scanner = OpcUaNodeScanner("opc.tcp://localhost:4840")

        scanner.connect()
        mock_client_instance.connect.assert_called_once()

    @patch('Insert_Into_Temperature.opcua_modules.Client')
    def test_disconnect(self, MockClient):
        mock_client_instance = MockClient.return_value
        scanner = OpcUaNodeScanner("opc.tcp://localhost:4840")

        scanner.connect()
        scanner.disconnect()
        mock_client_instance.disconnect.assert_called_once()

class TestOpcUaDataReceiver(unittest.TestCase):

    @patch('Insert_Into_Temperature.opcua_modules.Client')
    @patch('pyodbc.connect')
    def setUp(self, mock_pyodbc_connect, MockClient):
        self.mock_client = MockClient.return_value
        self.mock_cursor = mock_pyodbc_connect.return_value.cursor.return_value
        self.node_ids = [1, 2, 3]
        self.train_start_nodeid = 4
        self.receiver = OpcUaDataReceiver(self.mock_client, self.node_ids, self.train_start_nodeid)
        
    def test_start(self):
        self.mock_client.get_node.return_value.get_value.return_value = "31, 5, 16, 11, 197343000"
        
        with patch.object(self.receiver, '_receive_data', return_value=None):
            with patch.object(self.receiver, '_train_start', return_value=None):
                self.receiver.start()
                self.assertTrue(self.receiver.running)
                self.receiver.stop()
                self.assertFalse(self.receiver.running)

    @patch('utils.train_entry_timestamp.train_entry_timestamp')
    def test_receive_data(self, mock_train_entry_timestamp):
        mock_train_entry_timestamp.return_value = "test_train_id"
        self.mock_client.get_node.return_value.get_value.return_value = "2024_08_03_20_28_29_2000"
        
        self.receiver.start()
        self.receiver.running = False  # Stop the loop after the first run
        
        self.mock_cursor.execute.assert_called_once_with(
            """
            INSERT INTO Temperature
                   ([TrainId],[Axle_No],[Timestamp],[T1], [T2],[System_Timestamp])
            VALUES (?, ?, ?, ?,?,?)
            """,
            ("test_train_id", 5, "16", 11, 197343000, unittest.mock.ANY)
        )

    @patch('utils.train_entry_timestamp.train_entry_timestamp')
    def test_train_start(self, mock_train_entry_timestamp):
        mock_train_entry_timestamp.return_value = "test_train_id"
        self.mock_client.get_node.return_value.get_value.return_value = True
        
        with patch.object(self.receiver, '_receive_data', return_value=None):
            self.receiver.start()
            self.receiver.running = False  # Stop the loop after the first run
            
            self.assertEqual(self.receiver.current_train_id, "2024_08_03_20_28_29_2000")

if __name__ == '__main__':
    unittest.main()
