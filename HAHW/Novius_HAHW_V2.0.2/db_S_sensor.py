#Insert_Into_Temperature.py
import time
from datetime import datetime, timedelta
import pyodbc
from opcua import Client, ua
import logging
#from train_entry_timestamp import train_entry_timestamp
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
               INSERT INTO Proxy_s1
               ([TrainId],[S1],[S1_Timestamp],[S1_System_Timestamp])
        VALUES (?, ?, ?,?)
        """

        node = self.client.get_node(ua.NodeId(self.train_start_nodeid, 4))
        try:
            train_start_value = node.get_value()
            #OpcUaDataReceiver.write_TrainStart_Tojson(train_start_value)
            self.train_start_value = train_start_value
            EventLogger2.app_event.info("Train_Start_NodeId value: %s", train_start_value)
        except Exception as e:
            logger.error(f"Error reading Train_Start_NodeId_Node: {e}")
            return

        if train_start_value and not self.train_active:
            # TrainStart became True, get a new TrainId
            self.current_train_id = self.read_TrainId_Fromjson()
            self.train_active = True
            #OpcUaDataReceiver.write_TrainId_Tojson(self.current_train_id)
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
                        # c1 = parts[0]
                        # count = int(parts[1])
                        # time_stamp = parts[2]
                        # t1 = int(parts[3])
                        # t2 = int(parts[4])

                        current_time = datetime.now()
                        last_insertion_time = self.last_inserted_count.get(count)
                        
                        if self.train_active:
                            if last_insertion_time is None or (current_time - last_insertion_time) > timedelta(minutes=10):
                                try:
                                    System_Timestamp = datetime.now()
                                    formatted_timestamp = System_Timestamp.strftime('%d %b %Y %H:%M')
                                    logger.info(f"System_Timestamp{System_Timestamp}")
                                    logger.info(f"System_Timestamp{formatted_timestamp}")
                                    data_to_insert = (self.current_train_id, count, time_stamp, formatted_timestamp)
                                    cursor.execute(insert_query, data_to_insert)
                                    conn.commit()
                                    self.last_inserted_count[count] = current_time
                                    logger.info(f"Inserted data for count {count} with TrainId {self.current_train_id}")
                                except ValueError as e:
                                    logger.error(f"ValueError while inserting data: {e}")
                            else:
                                logger.info(f"System_Timestamp{System_Timestamp}")
                                logger.info(f"Skipping insertion for count {count} as it was inserted less than 1 minute ago")
                        else:
                            
                            self.last_inserted_count.pop(count, None)
                            
                else:
                    logger.info(f"Skipping insertion as TrainStart is False")
                    logger.error(f"Unexpected data format from node {node.nodeid}: {value}")
            except Exception as e:
                logger.error(f"Error reading value from node {node.nodeid}: {e}")

        cursor.close()
        conn.close()

    def get_train_start_value(self):
        return self.train_start_value  # Method to get the current train_start_value
    
def monitor_train_data():
    # OPC UA Server Configuration
    server_url = "opc.tcp://192.168.1.2:4840"
    node_ids = range(204, 404)  # Range of node IDs to receive data from
    train_start_nodeid = 829
    interval = 1  # Interval in seconds
    
    # OPC UA Node Scanner Setup
    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()
    
    # OPC UA Data Receiver Setup
    data_receiver = OpcUaDataReceiver(scanner.client, node_ids, train_start_nodeid, interval)
    
    # Temperature Database and Analysis Setup
    # db = TemperatureDatabase()
    # analysis = TemperatureAnalysis(db)
    
    try:
        while True:
            data_receiver.receive_data()
            
            # Read TrainStart value and TrainId from the JSON files
            #train_start_value = data_receiver.get_train_start_value()
            #train_id = db.read_TrainId_Fromjson()
            
            # If TrainStart is True, monitor train data and update the database
            # if train_start_value:
            #     db.update_train_id(train_id)
            #     db.monitor_train(train_id, analysis)
            # else:
            #     print("TrainStart is False. Waiting for TrainStart to become True...")
            
            time.sleep(interval)
            
    except KeyboardInterrupt:
        print("Program interrupted. Exiting...")
    finally:
        scanner.disconnect()
        #db.close_connection()

if __name__ == "__main__":
    print("monitor train commented")
    monitor_train_data()