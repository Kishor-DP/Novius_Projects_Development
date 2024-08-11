#main.py
import time
import logging
from Insert_Into_Temperature import OpcUaNodeScanner, OpcUaDataReceiver
from Insert_Into_tblTemperatureLog import TemperatureDatabase, TemperatureAnalysis
from threading import Thread

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[logging.StreamHandler()]
)

logger = logging.getLogger(__name__)

def monitor_train_data(db, analysis, receiver):
    """Monitor train data and update the database."""
    while True:
        try:
            current_train_id = receiver.current_train_id
            logger.debug(f"Current TrainId: {current_train_id}")

            # Update TrainId in TemperatureDatabase
            db.update_train_id(current_train_id)

            # Monitor train and process data
            db.monitor_train(current_train_id, analysis, interval=5, analysis_interval=1)
        except Exception as e:
            logger.error(f"Error in monitoring train data: {e}")
        time.sleep(5)  # Wait for a while before the next monitoring

if __name__ == "__main__":
    # OPC UA Server Configuration
    server_url = "opc.tcp://192.168.1.2:4840"
    node_ids = range(4, 204)  # Range of node IDs to receive data from
    train_start_nodeid = 829  # Replace with your Train Start Node ID
    interval = 1  # Interval in seconds

    # Initialize and connect to OPC UA Server
    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()

    # Initialize OpcUaDataReceiver
    receiver = OpcUaDataReceiver(scanner.client, node_ids, train_start_nodeid, interval)

    # Initialize TemperatureDatabase and TemperatureAnalysis
    db = TemperatureDatabase()
    analysis = TemperatureAnalysis(db)

    # Start monitoring in a separate thread
    monitor_thread = Thread(target=monitor_train_data, args=(db, analysis, receiver))
    monitor_thread.start()

    try:
        while True:
            try:
                # Receive data from OPC UA nodes and process it
                receiver.receive_data()
            except Exception as e:
                logger.error(f"Error in receiving data: {e}")

            time.sleep(interval)  # Wait for the specified interval before the next read

    except KeyboardInterrupt:
        logger.info("Stopping data receiver...")

    finally:
        # Disconnect from OPC UA Server
        scanner.disconnect()
        logger.info("Data receiver stopped.")
        monitor_thread.join()  # Ensure monitoring thread completes
