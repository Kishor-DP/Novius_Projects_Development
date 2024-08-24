import time
from datetime import datetime, timedelta
import pyodbc
from opcua import Client, ua
import json
from json.decoder import JSONDecodeError
import logging
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set your application's logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        #logging.FileHandler('opcua_data_receiver.log'),
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
        self.nodes = []
        self.last_insertion_times = {}
        self.current_train_id = None
        self.TrainStart = None
    def read_TrainId_Fromjson(self, max_retries=3, retry_interval=1):
        retries = 0
        while retries < max_retries:
            try:
                with open('TrainId.json', 'r') as json_file:
                    TrainId_data = json.load(json_file)
                    self.current_train_id = TrainId_data.get("TrainId", False)
                    return self.current_train_id
            except FileNotFoundError:
                logger.warning(f"File not found. Retrying in {retry_interval} seconds...")
            except JSONDecodeError:
                logger.warning(f"Invalid JSON data. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
            retries += 1
        return False

    def read_TrainStart_Fromjson(self, max_retries=3, retry_interval=1):
        retries = 0
        while retries < max_retries:
            try:
                with open('TrainStart.json', 'r') as json_file:
                    TrainStart_data = json.load(json_file)
                    self.TrainStart = TrainStart_data.get("TrainStart", False)
                    self.train_start_value = self.TrainStart
                    return self.TrainStart
            except FileNotFoundError:
                logger.warning(f"File not found. Retrying in {retry_interval} seconds...")
            except JSONDecodeError:
                logger.warning(f"Invalid JSON data. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
            retries += 1
        return False
    def _receive_data(self):
        self.nodes = [self.client.get_node(ua.NodeId(i, 4)) for i in self.node_ids]
        connection_string = (
            r"DRIVER={SQL Server};"
            r"SERVER=4MVDUGL\SQLEXPRESS;"
            r"DATABASE=NVS_HAHW_V2;"
            r"Trusted_Connection=yes;"
        )

        try:
            conn = pyodbc.connect(connection_string)
            cursor = conn.cursor()
        except Exception as e:
            print(f"Database connection failed: {e}")
            return

        insert_query = """
        INSERT INTO Proxy_s1
               ([TrainId],[S1],[S1_Timestamp],[S1_System_Timestamp])
        VALUES (?, ?, ?,?)
        """

        while True:
            train_id=self.read_TrainId_Fromjson()
            self.TrainStart=self.read_TrainStart_Fromjson()
            train_start_value = self.train_start_value
            if train_start_value and not self.train_active:
                # TrainStart became True, start processing
                self.train_active = True
                # self.insert_into_tblTrainTransaction(train_id)
                # new_axles = self.check_for_new_axle_no(train_id)
                # data = self.fetch_temperature(train_id)
                # new_calculations = analysis.calculate_temperatures(data)
                
                
                logger.info(f"New TrainId acquired: {self.current_train_id}")
            
            elif not train_start_value and self.train_active:
                # TrainStart became False, reset the TrainId for next activation

                self.train_active = False
                # self.known_axle_numbers.clear()
                # self.processed_axle_numbers.clear()
                logger.info(f"TrainStart is False, resetting.")
                continue  # Skip the rest of the loop to avoid processing

            for node in self.nodes:
                try:
                    value = node.get_value()
                    if isinstance(value, str):
                        parts = [part.strip() for part in value.split(',') if part.strip()]
                        print(f"Parts: {parts}")

                        if len(parts) != 3:
                            print("Error: Unexpected number of elements in the input string.")
                        else:
                            S = parts[0]
                            count = int(parts[1])
                            time_stamp = parts[2]

                            print(f"S = {S}")
                            print(f"count = {count}")
                            print(f"time_stamp = {time_stamp}")

                            current_time = datetime.now()
                            last_insertion_time = self.last_insertion_times.get(count)

                            if last_insertion_time is None or (current_time - last_insertion_time) > timedelta(minutes=2):
                                try:
                                    System_Timestamp = datetime.now()
                                    data_to_insert = (train_id,count, time_stamp, System_Timestamp)
                                    print("data_to_insert:", data_to_insert)
                                    cursor.execute(insert_query, data_to_insert)
                                    conn.commit()
                                    self.last_insertion_times[count] = current_time
                                except ValueError as e:
                                    print(f"Error converting values to integers from node {node.nodeid}: {parts}, Error: {e}")
                            else:
                                print(f"self.TrainStart,train_id",self.TrainStart,train_id)
                                print(f"Skipping insertion for count {count} as it was inserted less than 2 minutes ago")
                    else:
                        print(f"Unexpected data format from node {node.nodeid}: {value}")
                except Exception as e:
                    print(f"Error reading value from node {node.nodeid}: {e}")

            time.sleep(self.interval)

        cursor.close()
        conn.close()

if __name__ == "__main__":
    server_url = "opc.tcp://192.168.1.2:4840"  # Replace with your server URL
    node_ids = range(204, 404)  # Range of node IDs to receive data from
    interval = 1  # Interval in seconds

    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()

    try:
        receiver = OpcUaDataReceiver(scanner.client, node_ids, interval)
        receiver._receive_data()
    except KeyboardInterrupt:
        print("Stopping data receiver...")
    finally:
        scanner.disconnect()
