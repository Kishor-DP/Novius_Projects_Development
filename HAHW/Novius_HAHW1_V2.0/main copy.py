#main.py
import time
import logging
from Insert_Into_Temperature import OpcUaNodeScanner, OpcUaDataReceiver
from Fetch_Temperaturetbl import TemperatureDatabase

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

def main():
    # Initialize OPC UA Scanner
    server_url = "opc.tcp://192.168.1.2:4840"  # Replace with your server URL
    node_ids = range(4, 204)  # Range of node IDs to receive data from
    interval = 0.1  # Interval in seconds
    train_start_nodeid = 829  # Replace with your Train Start Node ID
    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()

    # Initialize OPC UA Data Receiver
    receiver = OpcUaDataReceiver(scanner.client, node_ids, train_start_nodeid, interval)
    receiver.start()
    
    # Initialize Database Connection
    db = TemperatureDatabase()
    logger.debug("main.py")
    try:
        while True:
            # Obtain the current TrainId from the OPC UA receiver
            train_id = receiver.current_train_id  # Ensure this attribute is set in OpcUaDataReceiver
            logger.debug(f"train_id____________: {train_id}")
            if train_id:
                # Periodically fetch and print data from the database
                data = db.fetch_temperature(train_id)
                logger.debug(f"data_fetch_temperature: {data}")
                for row in data:
                    logger.debug(f"TrainId: {row[0]}, Axle_No: {row[1]}, Timestamp: {row[2]}, T1: {row[3]}, T2: {row[4]}, System_Timestamp: {row[5]}")
            
            # Sleep for a while before fetching again
            time.sleep(5)  # Fetch data every 60 seconds
    except KeyboardInterrupt:
        logger.info("Stopping data receiver...")
    finally:
        # Clean up resources
        receiver.stop()
        scanner.disconnect()
        db.close_connection()

if __name__ == "__main__":
    main()
