import threading
import time
from opcua import Client, ua
import pyodbc
from datetime import datetime

# OPC UA Client Setup
class OpcUaNodeScanner:
    def __init__(self, server_url):
        self.client = Client(server_url)

    def connect(self):
        try:
            self.client.connect()
            print("Connected to OPC UA server")
        except Exception as e:
            print(f"Failed to connect to OPC UA server: {e}")

    def disconnect(self):
        self.client.disconnect()
        print("Disconnected from OPC UA server")

class OpcUaDataReceiver:
    def __init__(self, client, node_ids, interval=0.1):
        self.client = client
        self.node_ids = node_ids
        self.interval = interval
        self.running = False
        self.nodes = []

    def start(self):
        self.nodes = [self.client.get_node(ua.NodeId(i, 4)) for i in self.node_ids]
        self.running = True
        self.thread = threading.Thread(target=self._receive_data)
        self.thread.start()
        print(f"Started receiving data from nodes {self.node_ids} every {self.interval} seconds")

    def stop(self):
        self.running = False
        self.thread.join()
        print(f"Stopped receiving data from nodes {self.node_ids}")

    def _receive_data(self):
        # Database connection setup
        connection_string = (
            r"DRIVER={SQL Server};"
            r"SERVER=4MVDUGL\SQLEXPRESS;"
            r"DATABASE=PLC;"
            r"Trusted_Connection=yes;"
        )
        conn = pyodbc.connect(connection_string)
        cursor = conn.cursor()

        # Define the insert query
        insert_query = """
        INSERT INTO Proxy
               ([C1], [C2], [E1], [E2], [S1], [S2], [Axle_No], 
                [C1_Timestamp], [C1_System_Timestamp], 
                [C2_Timestamp], [C2_System_Timestamp], [S1_Timestamp], [S1_System_Timestamp], 
                [S2_Timestamp], [S2_System_Timestamp], [E1_Timestamp], [E1_System_Timestamp], 
                [E2_Timestamp], [E2_System_Timestamp])
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        while self.running:
            for node in self.nodes:
                try:
                    value = node.get_value()
                    # Assuming the value read is appropriate for the columns
                    data_to_insert = (
                        value, value, value, value, value, value, 'Axle_No_value',
                        value, datetime.now(),
                        value, datetime.now(), value, datetime.now(),
                        value, datetime.now(), value, datetime.now(),
                        value, datetime.now()
                    )
                    print("data_to_insert:",data_to_insert)
                    cursor.execute(insert_query, data_to_insert)
                    conn.commit()

                    if isinstance(value, list):
                        print(f"Node ID: {node.nodeid}, Array Values: {value}")
                    else:
                        print(f"Node ID: {node.nodeid}, Value: {value}")
                except Exception as e:
                    print(f"Error reading value from node {node.nodeid}: {e}")
            time.sleep(self.interval)
        
        # Close the connection
        cursor.close()
        conn.close()

if __name__ == "__main__":
    server_url = "opc.tcp://192.168.1.2:4840"  # Replace with your server URL
    node_ids = range(4, 204)  # Range of node IDs to receive data from
    interval = 0.1  # Interval in seconds

    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()

    try:
        receiver = OpcUaDataReceiver(scanner.client, node_ids, interval)
        receiver.start()
        
        # Keep the main thread running to allow data reception
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping data receiver...")
        finally:
            receiver.stop()
    finally:
        scanner.disconnect()





