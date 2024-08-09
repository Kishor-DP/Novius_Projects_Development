import threading
import time
from opcua import Client, ua
import pyodbc
from datetime import datetime
from EventLogger import app_event

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
    def __init__(self, client, node_ids, interval=1):
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
        connection_string = (
            r"DRIVER={SQL Server};"
            r"SERVER=4MVDUGL\SQLEXPRESS;"
            r"DATABASE=PLC;"
            r"Trusted_Connection=yes;"
        )

        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
        except Exception as e:
            print(f"Database connection failed: {e}")
            return

        insert_query = """
        INSERT INTO Temperature
               ([T1], [T2], [T3], [T4], [T5], [T6], [Timestamp], [Axle_No], [System_Timestamp])
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """

        while self.running:
            for node in self.nodes:
                try:
                    value = node.get_value()
                    if not isinstance(value, list) or len(value) < 6:
                        print(f"Unexpected data format from node {node.nodeid}: {value}")
                        continue

                    axle_no = "Axle_No_value"  # Replace with actual logic to determine Axle_No
                    data_to_insert = (
                        value[0], value[1], value[2], value[3],
                        value[4], value[5], datetime.now(), axle_no, datetime.now()
                    )

                    print("data_to_insert:", data_to_insert)
                    cursor.execute(insert_query, data_to_insert)
                    app_event.debug("Data inserted", data_to_insert)
                    conn.commit()
                except Exception as e:
                    print(f"Error reading value from node {node.nodeid}: {e}")
            time.sleep(self.interval)

        cursor.close()
        conn.close()

if __name__ == "__main__":
    server_url = "opc.tcp://192.168.1.2:4840"  # Replace with your server URL
    node_ids = range(4, 204)  # Range of node IDs to receive data from
    interval = 1  # Interval in seconds

    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()

    try:
        receiver = OpcUaDataReceiver(scanner.client, node_ids, interval)
        receiver.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping data receiver...")
        finally:
            receiver.stop()
    finally:
        scanner.disconnect()
