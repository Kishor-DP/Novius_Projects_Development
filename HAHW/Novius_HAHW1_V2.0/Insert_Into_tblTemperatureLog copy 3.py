import pyodbc
from datetime import datetime
import time
import logging
import EventLogger2
import json
from json.decoder import JSONDecodeError

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class TemperatureDatabase:
    def __init__(self):
        self.connection = self.connect_to_database()
        self.known_axle_numbers = set()
        self.processed_axle_numbers = set()
        self.current_train_id = None
        self.TrainStart = None
        self.previous_TrainStart = None  # Track the previous state of TrainStart

    def process_train_data(self):
        if self.TrainStart:
            current_train_id = self.read_TrainId_Fromjson()
            if self.is_new_train_id(current_train_id):
                self.reset_state()
                logger.debug(f"Processing new TrainId: {current_train_id}")
            else:
                logger.debug(f"Continuing with existing TrainId: {current_train_id}")
            self.process_axles()  # Method needs to be implemented
        else:
            logger.debug("TrainStart is False. Waiting for TrainStart to be True.")

    def reset_state(self):
        self.known_axle_numbers.clear()  # Example: Clear axle numbers

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
                    return self.TrainStart
            except FileNotFoundError:
                logger.warning(f"File not found. Retrying in {retry_interval} seconds...")
            except JSONDecodeError:
                logger.warning(f"Invalid JSON data. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
            retries += 1
        return False

    def update_train_id(self, train_id):
        if train_id != self.current_train_id:
            logger.info(f"New TrainId detected: {train_id}. Updating...")
            self.current_train_id = train_id
            self.processed_axle_numbers.clear()

    def connect_to_database(self):
        connection_string = (
            r"DRIVER={SQL Server};"
            r"SERVER=4MVDUGL\SQLEXPRESS;"
            r"DATABASE=NVS_HAHW_V2;"
            r"Trusted_Connection=yes;"
        )
        try:
            connection = pyodbc.connect(connection_string)
            return connection
        except pyodbc.Error as e:
            logger.error(f"Error connecting to database: {e}")
            return None

    def ensure_connection(self):
        try:
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        except (pyodbc.Error, AttributeError):
            self.connection = self.connect_to_database()

    def fetch_temperature(self, train_id):
        EventLogger2.app_event.info(f"Received train_id from main fetch_temperature={train_id}")
        self.current_train_id = train_id
        self.ensure_connection()
        
        if not self.connection:
            logger.error("No database connection.")
            return [], train_id
            
        query = "SELECT TrainId, Axle_No, Timestamp, T1, T2, System_Timestamp FROM Temperature WHERE TrainId = ?;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (train_id,))
                rows = cursor.fetchall()
                return rows
        except pyodbc.Error as e:
            logger.error(f"Error fetching data: {e}")
            return []

    def insert_temperature_calculations(self, calculations):
        self.ensure_connection()
        
        if not self.connection:
            logger.error("No database connection.")
            return

        query = """
        INSERT INTO [NVS_HAHW_V2].[dbo].[tblTemperatureLog] (intTrainId, intAxleNo, decTs1, decTs2)
        VALUES (?, ?, ?, ?)
        """
        try:
            with self.connection.cursor() as cursor:
                for calc in calculations:
                    if calc[1] not in self.processed_axle_numbers:
                        cursor.execute(query, (calc[0], calc[1], calc[2], calc[3]))
                        EventLogger2.app_event.debug("Inserted temperature calculations")
                        self.processed_axle_numbers.add(calc[1])
                self.connection.commit()
        except pyodbc.Error as e:
            logger.error(f"Error inserting data: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def check_for_new_axle_no(self):
        # Reset state if TrainStart changes from True to False
        if not self.TrainStart and self.previous_TrainStart:
            logger.info("TrainStart changed from True to False. Resetting state...")
            self.reset_state()
        
        data = self.fetch_temperature(self.current_train_id)
        EventLogger2.app_event.debug("check_for_new_axle_no data")
        new_axles = [row for row in data if row[1] not in self.known_axle_numbers]
        
        for row in new_axles:
            self.known_axle_numbers.add(row[1])
            logger.info(f"New Axle Detected - TrainId: {row[0]}, Axle_No: {row[1]}, Timestamp: {row[2]}, T1: {row[3]}, T2: {row[4]}, System_Timestamp: {row[5]}")
            
        return new_axles

    def monitor_train(self, analysis, interval=5, analysis_interval=5):
        logger.info("Monitoring train for new axle numbers...")
        last_analysis_time = time.time()
        
        try:
            while True:
                self.TrainStart = self.read_TrainStart_Fromjson()
                data = []  # Initialize data
                
                if self.TrainStart != self.previous_TrainStart:
                    if not self.TrainStart:
                        logger.debug("TrainStart is False. Waiting for TrainStart to become True...")
                    else:
                        self.current_train_id = self.read_TrainId_Fromjson()
                        logger.debug(f"TrainStart is True. Current TrainId: {self.current_train_id}")

                    self.previous_TrainStart = self.TrainStart
                    self.check_for_new_axle_no()  # This now also handles the reset
                    
                    if self.TrainStart and self.current_train_id:
                        self.ensure_connection()
                        data = self.fetch_temperature(self.current_train_id)
                        new_axles = self.check_for_new_axle_no()
                        
                        if new_axles:
                            new_calculations = analysis.calculate_temperatures(data)
                            self.insert_temperature_calculations(new_calculations)
                        
                        if time.time() - last_analysis_time >= analysis_interval:
                            analysis.get_total_axles(data)
                            last_analysis_time = time.time()
                        
                        time.sleep(interval)
                else:
                    logger.debug("TrainStart has not changed. Waiting for TrainStart to change...")
                    time.sleep(2)

        except KeyboardInterrupt:
            logger.info("Monitoring stopped.")
        finally:
            self.close_connection()

class TemperatureAnalysis:
    def __init__(self, db):
        self.db = db

    def calculate_temperatures(self, data):
        calculations = []
        for row in data:
            t1 = row[3]
            t2 = row[4]
            T1 = t1 - 5
            T2 = t2 + 5
            calculations.append((row[0], row[1], T1, T2))
            logger.debug("Calculations done.")
            logger.info(f"TrainId: {row[0]}, Axle_No: {row[1]}, {T1}, {T2}, Timestamp: {row[2]}, System_Timestamp: {row[5]}")
        return calculations

    def get_total_axles(self, data):
        axle_numbers = {row[1] for row in data}
        total_axles = len(axle_numbers)
        logger.info(f"Total number of unique Axle_Nos: {total_axles}")
        return total_axles

def main():
    db = TemperatureDatabase()
    analysis = TemperatureAnalysis(db)
    
    db.monitor_train(analysis)

if __name__ == "__main__":
    main()
