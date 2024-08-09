import time
import logging
from Insert_Into_Temperature import OpcUaNodeScanner, OpcUaDataReceiver
from Fetch_Temperaturetbl import TemperatureDatabase,TemperatureAnalysis
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

if __name__ == "__main__":
    server_url = "opc.tcp://192.168.1.2:4840"
    node_ids = range(4, 204)  # Range of node IDs to receive data from
    interval = 1  # Interval in seconds
    train_start_nodeid = 829  # Replace with your Train Start Node ID

    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()
    #################################################################################
    db = TemperatureDatabase()
    analysis = TemperatureAnalysis(db)
    
    
    
    
    
    #################################################################################
    try:
        receiver = OpcUaDataReceiver(scanner.client, node_ids, train_start_nodeid, interval)
        receiver.start()
        #receiver=OpcUaDataReceiver._receive_data()
        print("receiver:",receiver)
        try:
            while True:
                time.sleep(1)
                if receiver.latest_train_id:  # Check if a TrainId has been set
                    logger.info(f"Latest TrainId: {receiver.latest_train_id}")
                    current_train_id = receiver.latest_train_id
                    train_id = current_train_id
                    logger.debug(f"train_id_from_ft: {train_id}")
                    #Monitor train for new axle numbers and perform analysis
                    db.monitor_train(train_id, analysis, interval=5, analysis_interval=1)  # Check every 5 seconds and analyze every 60 seconds
        except KeyboardInterrupt:
            logger.info("Stopping data receiver...")
        finally:
            receiver.stop()
    finally:
        scanner.disconnect()
