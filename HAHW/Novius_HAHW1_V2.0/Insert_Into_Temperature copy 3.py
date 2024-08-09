import threading
import time
from datetime import datetime, timedelta
import pyodbc
from opcua import Client, ua
import logging
from train_entry_timestamp import train_entry_timestamp
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('opcua_data_receiver.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

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
        self.running = False
        self.nodes = []
        self.last_insertion_times = {}

    def start(self):
        self.nodes = [self.client.get_node(ua.NodeId(i, 4)) for i in self.node_ids]
        self.running = True
        self.thread = threading.Thread(target=self._receive_data)
        self.thread.start()
        logger.info(f"Started receiving data from nodes {self.node_ids} every {self.interval} seconds")
        self.train_start_thread = threading.Thread(target=self._train_start)
        self.train_start_thread.start()
        logger.info("Started Train Start Node data reception")

    def stop(self):
        self.running = False
        self.thread.join()
        self.train_start_thread.join()
        logger.info(f"Stopped receiving data from nodes {self.node_ids}")

    def _train_start(self):
        while self.running:
            node = self.client.get_node(ua.NodeId(self.train_start_nodeid, 4))
            try:
                train_start_value = node.get_value()
                logger.debug("Train_Start_NodeId value: %s", train_start_value)
            except Exception as e:
                logger.error(f"Error reading Train_Start_NodeId_Node: {e}")

            time.sleep(self.interval)
            return train_start_value
        
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
            logger.error(f"Database connection failed: {e}")
            return

        insert_query = """
        INSERT INTO Temperature
               ([TrainId],[Axle_No],[Timestamp],[T1], [T2],[System_Timestamp])
        VALUES (?, ?, ?, ?,?,?)
        """

        while self.running:
            for node in self.nodes:
                try:
                    value = node.get_value()
                    if isinstance(value, str):
                        # Strip extra spaces and split the string by commas
                        parts = [part.strip() for part in value.split(',') if part.strip()]

                        # Log parts for debugging
                        logger.debug("Parts: %s", parts)

                        # Check the length of parts to avoid IndexError
                        if len(parts) != 5:
                            logger.error("Error: Unexpected number of elements in the input string.")
                        else:
                            # Extract values
                            c1 = parts[0]
                            count = int(parts[1])
                            time_stamp = parts[2]
                            t1 = int(parts[3])
                            t2 = int(parts[4])

                            # Log the extracted values
                            logger.debug("c1 = %s", c1)
                            logger.debug("count = %d", count)
                            logger.debug("time_stamp = %s", time_stamp)
                            logger.debug("t1 = %d", t1)
                            logger.debug("t2 = %d", t2)
                            
                            TrainId=train_entry_timestamp()
                            current_time = datetime.now()
                            last_insertion_time = self.last_insertion_times.get(count)
                            #if self._train_start()==True:
                            
                            if last_insertion_time is None or (current_time - last_insertion_time) > timedelta(minutes=2):
                                try:
                                    
                                    System_Timestamp = datetime.now()
                                    data_to_insert = (TrainId,count, time_stamp, t1, t2, System_Timestamp)
                                    logger.debug("data_to_insert: %s", data_to_insert)
                                    cursor.execute(insert_query, data_to_insert)
                                    conn.commit()
                                    self.last_insertion_times[count] = current_time
                                except ValueError as e:
                                    logger.error(f"Error converting values to integers from node {node.nodeid}: {parts}, Error: {e}")
                            else:
                                logger.info(f"Skipping insertion for count {count} as it was inserted less than 10 minutes ago")
                    else:
                        logger.error(f"Unexpected data format from node {node.nodeid}: {value}")
                except Exception as e:
                    logger.error(f"Error reading value from node {node.nodeid}: {e}")

            time.sleep(self.interval)

        # Ensure resources are closed properly
        cursor.close()
        conn.close()

if __name__ == "__main__":
    server_url = "opc.tcp://192.168.1.2:4840"  # Replace with your server URL
    node_ids = range(4, 204)  # Range of node IDs to receive data from
    interval = 0.1  # Interval in seconds
    train_start_nodeid = 829  # Replace with your Train Start Node ID
    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()

    try:
        receiver = OpcUaDataReceiver(scanner.client, node_ids, train_start_nodeid, interval)
        receiver.start()

        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            logger.info("Stopping data receiver...")
        finally:
            receiver.stop()
    finally:
        scanner.disconnect()
