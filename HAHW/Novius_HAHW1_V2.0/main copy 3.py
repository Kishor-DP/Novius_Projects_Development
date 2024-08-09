import time
import logging
from Insert_Into_Temperature import OpcUaNodeScanner, OpcUaDataReceiver
from Fetch_Temperaturetbl import TemperatureDatabase, TemperatureAnalysis
import EventLogger2
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set your application's logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('opcua_data_receiver.log'),
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Set logging level for opcua library to WARNING to suppress debug logs
logging.getLogger('opcua').setLevel(logging.WARNING)

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

    if db.connection:  # Check if the connection was successful
        analysis = TemperatureAnalysis(db)
    else:
        print("Failed to connect to the database.")
        return

    try:
        while True:
            # Obtain the current TrainId from the OPC UA receiver
            current_train_id = receiver.current_train_id  # Ensure this attribute is set in OpcUaDataReceiver
            EventLogger2.app_event.info(f"Current Train ID in main: {current_train_id}")
            if current_train_id:
                # Periodically fetch and print data from the database
                data = db.fetch_temperature(current_train_id)
                EventLogger2.app_event.info(f"sent from main Fetched temperature data: {data}")
                for row in data:
                    print(row)
                    #logger.debug(f"TrainId: {row[0]}, Axle_No: {row[1]}, Timestamp: {row[2]}, T1: {row[3]}, T2: {row[4]}, System_Timestamp: {row[5]}")
                
                # Monitor train for new axle numbers and perform analysis
                
                db.monitor_train(current_train_id, analysis, interval=5, analysis_interval=1)
                
            # Sleep for a while before fetching again
            time.sleep(5)  # Fetch data every 5 seconds
    except KeyboardInterrupt:
        logger.info("Stopping data receiver...")
    finally:
        # Clean up resources
        receiver.stop()
        scanner.disconnect()
        db.close_connection()

if __name__ == "__main__":
    main()
