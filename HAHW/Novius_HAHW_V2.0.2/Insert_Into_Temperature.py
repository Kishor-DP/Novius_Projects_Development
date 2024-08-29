#Insert_Into_Temperature.py
import time
from datetime import datetime, timedelta
import pyodbc
from opcua import Client, ua
import logging
from train_entry_timestamp import train_entry_timestamp
import EventLogger2
from json.decoder import JSONDecodeError  # Import JSONDecodeError
import json


# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set your application's logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Set logging level for opcua library to WARNING to suppress debug logs
logging.getLogger('opcua').setLevel(logging.WARNING)

# OPC UA Client Setup
class OpcUaNodeScanner:
    def __init__(self, server_url):
        self.client = Client(server_url)

    def connect(self):
        try:
            self.client.connect()
            logger.info("Connected to OPC UA server")
        except Exception as e:
            logger.error(f"Failed to connect to OPC UA server: {e}")

    def disconnect(self):
        self.client.disconnect()
        logger.info("Disconnected from OPC UA server")

class OpcUaDataReceiver:
    
    def __init__(self, client, node_ids, train_start_nodeid, interval=1):
        self.client = client
        self.node_ids = node_ids
        self.interval = interval
        self.train_start_nodeid = train_start_nodeid
        self.nodes = []
        self.last_inserted_count = {}
        self.current_train_id = None
        self.train_active = False  # Flag to track if TrainStart was True
        self.train_start_value = False

    def write_TrainId_Tojson(status, max_retries=31536063734300000, retry_interval=1):
        retries = 0
        while retries < max_retries:
            try:
                TrainId_data = {"TrainId": status}
                with open('TrainId.json', 'w') as json_file:
                    json.dump(TrainId_data, json_file)
                return  # Exit function if writing succeeds
            except Exception as e:
                print(f"Error writing JSON file (retry {retries + 1}/{max_retries}):", e)
                retries += 1
                time.sleep(retry_interval)
        print("Failed to write JSON file after maximum retries")

    def write_TrainStart_Tojson(status, max_retries=31536063734300000, retry_interval=1):
        retries = 0
        while retries < max_retries:
            try:
                TrainStart_data = {"TrainStart": status}
                with open('TrainStart.json', 'w') as json_file:
                    json.dump(TrainStart_data, json_file)
                return  # Exit function if writing succeeds
            except Exception as e:
                print(f"Error writing JSON file (retry {retries + 1}/{max_retries}):", e)
                retries += 1
                time.sleep(retry_interval)
        print("Failed to write JSON file after maximum retries")

    def receive_data(self):
        self.nodes = [self.client.get_node(ua.NodeId(i, 4)) for i in self.node_ids]

        connection_string = (
            r"DRIVER={SQL Server};"
            r"SERVER=4MVDUGL\KISHOR;"
            r"DATABASE=NVS_HAHW_V2;"
            r"Trusted_Connection=yes;"
        )

        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            return

        insert_query = """
        INSERT INTO Temperature
               ([TrainId], [Axle_No], [Timestamp], [T1], [T2], [System_Timestamp])
        VALUES (?, ?, ?, ?, ?, ?)
        """

        node = self.client.get_node(ua.NodeId(self.train_start_nodeid, 4))
        try:
            train_start_value = node.get_value()
            OpcUaDataReceiver.write_TrainStart_Tojson(train_start_value)
            self.train_start_value = train_start_value
            EventLogger2.app_event.info("Train_Start_NodeId value: %s", train_start_value)
        except Exception as e:
            logger.error(f"Error reading Train_Start_NodeId_Node: {e}")
            return

        if train_start_value and not self.train_active:
            # TrainStart became True, get a new TrainId
            self.current_train_id = train_entry_timestamp()
            self.train_active = True
            OpcUaDataReceiver.write_TrainId_Tojson(self.current_train_id)
            logger.info(f"New TrainId acquired: {self.current_train_id}")
        elif not train_start_value and self.train_active:
            # TrainStart became False, reset the TrainId for next activation
            self.train_active = False
            self.last_inserted_count.clear()  # Clear the dictionary to reset insertion times
            logger.info(f"TrainStart is False, resetting TrainId.")

        for node in self.nodes:
            try:
                value = node.get_value()

                if isinstance(value, str):
                    parts = [part.strip() for part in value.split(',') if part.strip()]
                    if len(parts) != 5:
                        logger.error("Error: Unexpected number of elements in the input string.")
                    else:
                        c1 = parts[0]
                        count = int(parts[1])
                        time_stamp = parts[2]
                        t1 = int(parts[3])
                        t2 = int(parts[4])

                        current_time = datetime.now()
                        last_insertion_time = self.last_inserted_count.get(count)
                        
                        if self.train_active:
                            if last_insertion_time is None or (current_time - last_insertion_time) > timedelta(minutes=10):
                                try:
                                    System_Timestamp = datetime.now()
                                    formatted_timestamp = System_Timestamp.strftime('%d %b %Y %H:%M')
                                    data_to_insert = (self.current_train_id, count, time_stamp, t1, t2, formatted_timestamp)
                                    cursor.execute(insert_query, data_to_insert)
                                    conn.commit()
                                    self.last_inserted_count[count] = current_time
                                    logger.info(f"Inserted data for count {count} with TrainId {self.current_train_id}")
                                except ValueError as e:
                                    logger.error(f"ValueError while inserting data: {e}")
                            else:
                                logger.info(f"Skipping insertion for count {count} as it was inserted less than 1 minute ago")
                        else:
                            self.last_inserted_count.pop(count, None)
                            logger.info(f"Skipping insertion as TrainStart is False")
                else:
                    logger.error(f"Unexpected data format from node {node.nodeid}: {value}")
            except Exception as e:
                logger.error(f"Error reading value from node {node.nodeid}: {e}")

        cursor.close()
        conn.close()

    def get_train_start_value(self):
        return self.train_start_value  # Method to get the current train_start_value
    
# if __name__ == "__main__":
#     # OPC UA Server Configuration
#     server_url = "opc.tcp://192.168.1.2:4840"
#     node_ids = range(4, 204)  # Range of node IDs to receive data from
#     train_start_nodeid = 829  # Replace with your Train Start Node ID
#     interval = 1  # Interval in seconds

#     # Initialize and connect to OPC UA Server
#     scanner = OpcUaNodeScanner(server_url)
#     scanner.connect()

#     # Initialize OpcUaDataReceiver
#     receiver = OpcUaDataReceiver(scanner.client, node_ids, train_start_nodeid, interval)

#     try:
#         while True:
#             # Receive data from OPC UA nodes and process it
#             receiver.receive_data()
#             time.sleep(interval)  # Wait for the specified interval before the next read

#     except KeyboardInterrupt:
#         logger.info("Stopping data receiver...")

#     finally:
#         # Disconnect from OPC UA Server
#         scanner.disconnect()
#         logger.info("Data receiver stopped.")
