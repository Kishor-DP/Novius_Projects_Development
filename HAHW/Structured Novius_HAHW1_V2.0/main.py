import json
import logging
from Insert_Into_Temperature.opcua_modules import OpcUaNodeScanner, OpcUaDataReceiver
from Fetch_Temperaturetbl.temperature_db import TemperatureDatabase, TemperatureAnalysis
from utils.train_entry_timestamp import train_entry_timestamp
import os

# Load configuration
def load_config():
    config_file = 'config/config.json'
    if not os.path.isfile(config_file):
        print(f"Configuration file not found: {config_file}")
        return {}
    with open(config_file, 'r') as f:
        config = json.load(f)
    return config

# Main execution
def main():
    # Load configuration
    config = load_config()
    if not config:
        return

    # Configure logging
    logging.basicConfig(
        level=logging.getLevelName(config['logging']['level']),
        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        handlers=[
            logging.FileHandler(config['logging']['logfile']),
            logging.StreamHandler()
        ]
    )
    logger = logging.getLogger(__name__)

    opcua_config = config['opcua']
    server_url = opcua_config['server_url']
    node_ids = opcua_config['node_ids']
    train_start_nodeid = opcua_config['train_start_nodeid']
    interval = opcua_config['interval']

    # Initialize OPC UA client and data receiver
    node_scanner = OpcUaNodeScanner(server_url)
    node_scanner.connect()
    
    data_receiver = OpcUaDataReceiver(node_scanner.client, node_ids, train_start_nodeid, interval)
    data_receiver.start()

    # Initialize database and analysis
    db = TemperatureDatabase(config['database'])
    analysis = TemperatureAnalysis(db)
    
    train_id = train_entry_timestamp()  # Get initial train ID

    # Start monitoring
    try:
        db.monitor_train(train_id, analysis, interval=10, analysis_interval=60)
    except KeyboardInterrupt:
        logger.info("Monitoring interrupted. Stopping...")
    finally:
        #data_receiver.stop()
        db.close_connection()
        node_scanner.disconnect()

if __name__ == "__main__":
    main()
