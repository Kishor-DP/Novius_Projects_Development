#main.py
import time
import logging
from Insert_Into_Temperature import OpcUaNodeScanner, OpcUaDataReceiver
from Inser_Into_tblTemperatureLog import TemperatureDatabase, TemperatureAnalysis

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

    try:
        while True:
            # Receive data from OPC UA nodes and process it
            receiver.receive_data()
            time.sleep(interval)  # Wait for the specified interval before the next read

    except KeyboardInterrupt:
        logger.info("Stopping data receiver...")

    finally:
        # Disconnect from OPC UA Server
        scanner.disconnect()
        logger.info("Data receiver stopped.")
