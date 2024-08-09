import threading
import time
from datetime import datetime, timedelta
import pyodbc
from opcua import Client, ua

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
        self.last_insertion_times = {}

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
               ([Axle_No],[Timestamp],[T1], [T2],[System_Timestamp])
        VALUES (?, ?, ?, ?,?)
        """

        while self.running:
            for node in self.nodes:
                try:
                    value = node.get_value()
                    if isinstance(value, str):
                        # Strip extra spaces and split the string by commas
                        parts = [part.strip() for part in value.split(',') if part.strip()]

                        # Print parts for debugging
                        print(f"Parts: {parts}")

                        # Check the length of parts to avoid IndexError
                        if len(parts) != 5:
                            print("Error: Unexpected number of elements in the input string.")
                        else:
                            # Extract values
                            c1 = parts[0]
                            count = int(parts[1])
                            time_stamp = parts[2]
                            t1 = int(parts[3])
                            t2 = int(parts[4])

                            # Print the extracted values
                            print(f"c1 = {c1}")
                            print(f"count = {count}")
                            print(f"time_stamp = {time_stamp}")
                            print(f"t1 = {t1}")
                            print(f"t2 = {t2}")

                            current_time = datetime.now()
                            last_insertion_time = self.last_insertion_times.get(count)

                            if last_insertion_time is None or (current_time - last_insertion_time) > timedelta(minutes=2):
                                try:
                                    System_Timestamp=datetime.now()
                                    data_to_insert = (count, time_stamp, t1, t2,System_Timestamp)
                                    print("data_to_insert:", data_to_insert)
                                    cursor.execute(insert_query, data_to_insert)
                                    conn.commit()
                                    self.last_insertion_times[count] = current_time
                                except ValueError as e:
                                    print(f"Error converting values to integers from node {node.nodeid}: {parts}, Error: {e}")
                            else:
                                print(f"Skipping insertion for count {count} as it was inserted less than 2 minutes ago")
                    else:
                        print(f"Unexpected data format from node {node.nodeid}: {value}")
                except Exception as e:
                    print(f"Error reading value from node {node.nodeid}: {e}")

            time.sleep(self.interval)

        # Ensure resources are closed properly
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
