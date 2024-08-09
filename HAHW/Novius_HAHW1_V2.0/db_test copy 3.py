import threading
import time
import re
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
               ([Axle_No],[Timestamp],[T1], [T2])
        VALUES (?, ?, ?, ?)
        """

        while self.running:
            for node in self.nodes:
                try:
                    value = node.get_value()
                    if isinstance(value, str):
                    # Input string
                    #input_str = 'C1,    10,  31   5  16  11  197343000,   716,     0,'

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
                    # value = node.get_value()
                    # if isinstance(value, str):
                        # Remove 'C1' and commas, normalize spaces
                        # cleaned_value = re.sub(r'[C1,]', '', value)
                        # cleaned_value = re.sub(r'\s+', ' ', cleaned_value)
                        # parts = [part.strip() for part in cleaned_value.split(' ') if part.strip()]

                        # if len(parts) < 7:
                        #     print(f"Unexpected number of values from node {node.nodeid}: {value}")
                        #     continue

                        try:
                            # # Convert parts to integers
                            # numeric_values = [int(part) for part in parts[:7]]
                            # axle_no = numeric_values[6]  # Assuming the seventh value is the Axle_No
                            # timestamp = ' '.join(parts[1:6])  # Join timestamp parts
                            # t1 = numeric_values[0]
                            # t2 = numeric_values[1]

                            data_to_insert = (count,time_stamp,t1,t2 )
                            

                            print("data_to_insert:", data_to_insert)
                            cursor.execute(insert_query, data_to_insert)
                            #app_event.debug("Data inserted", data_to_insert)
                            conn.commit()
                        except ValueError:
                            print(f"Error converting values to integers from node {node.nodeid}: {parts}")
                    else:
                        print(f"Unexpected data format from node {node.nodeid}: {value}")
                        continue
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
