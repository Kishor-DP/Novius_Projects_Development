import time
import logging
from db_S_sensor import OpcUaNodeScanner, OpcUaDataReceiver
#from Insert_Into_tblTemperatureLog import TemperatureDatabase, TemperatureAnalysis

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

def monitor_train_data():
    # OPC UA Server Configuration
    server_url = "opc.tcp://192.168.1.2:4840"
    node_ids = range(4, 204)  # Range of node IDs to receive data from
    train_start_nodeid = 829  # Replace with your Train Start Node ID
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