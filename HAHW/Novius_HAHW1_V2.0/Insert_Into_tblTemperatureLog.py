import pyodbc
from datetime import datetime
import time
import logging
import EventLogger2

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

# Set logging level for opcua library to WARNING to suppress debug logs
logging.getLogger('opcua').setLevel(logging.WARNING)

class TemperatureDatabase:
    def __init__(self):
        self.connection = self.connect_to_database()
        self.known_axle_numbers = set()
        self.processed_axle_numbers = set()
        self.current_train_id = None
        print("self.current_train_id", self.current_train_id)

    def update_train_id(self, train_id):
        """Update the current TrainId in the database instance."""
        if train_id != self.current_train_id:
            logger.info(f"New TrainId detected: {train_id}. Updating...")
            self.current_train_id = train_id
            self.processed_axle_numbers.clear()  # Clear processed axles for the new TrainId

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
            print(f"Error connecting to database: {e}")
            logger.debug(f"Error connecting to database: {e}")
            return None

    def ensure_connection(self):
        """Ensure the database connection is open, reconnect if needed."""
        try:
            # Attempt to execute a simple query to test the connection
            with self.connection.cursor() as cursor:
                cursor.execute("SELECT 1")
        except (pyodbc.Error, AttributeError):
            # Reconnect if there's an error or if connection is None
            self.connection = self.connect_to_database()

    def fetch_temperature(self, train_id):
        EventLogger2.app_event.info(f"received train_id from main fetch_temperature={train_id}")
        self.current_train_id = train_id
        self.ensure_connection()  # Ensure the connection is open
        
        if not self.connection:
            print("No database connection.")
            return [], train_id
            
        query = "SELECT TrainId, Axle_No, Timestamp, T1, T2, System_Timestamp FROM Temperature WHERE TrainId = ?;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (train_id,))
                rows = cursor.fetchall()
                EventLogger2.app_event.info(f"fetch_temperature={rows}")
                return rows
        except pyodbc.Error as e:
            print(f"Error fetching data: {e}")
            return []

    def insert_temperature_calculations(self, calculations):
        self.ensure_connection()  # Ensure the connection is open
        
        if not self.connection:
            print("No database connection.")
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
                        EventLogger2.app_event.debug("insert_temperature_calculations")
                        self.processed_axle_numbers.add(calc[1])
                self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error inserting data: {e}")

    def close_connection(self):
        if self.connection:
            self.connection.close()

    def check_for_new_axle_no(self, train_id):
        # Reset processed axles if a new train ID is detected
        if train_id != self.current_train_id:
            self.processed_axle_numbers.clear()
            self.current_train_id = train_id

        data = self.fetch_temperature(train_id)
        EventLogger2.app_event.debug("check_for_new_axle_no data = self.fetch_temperature(train_id)")
        new_axles = [row for row in data if row[1] not in self.known_axle_numbers]
        
        for row in new_axles:
            self.known_axle_numbers.add(row[1])
            print(f"New Axle Detected - TrainId: {row[0]}, Axle_No: {row[1]}, Timestamp: {row[2]}, T1: {row[3]}, T2: {row[4]}, System_Timestamp: {row[5]}")
            
        return new_axles

    def monitor_train(self, train_id, analysis, interval=5, analysis_interval=5):
        print(f"Monitoring train {train_id} for new axle numbers...")
        last_analysis_time = time.time()
        
        try:
            while True:
                self.ensure_connection()  # Ensure the connection is open before any operation
                new_axles = self.check_for_new_axle_no(train_id)
                # Fetch data only if new axles are detected
                if new_axles:
                    data = self.fetch_temperature(train_id)
                    new_calculations = analysis.calculate_temperatures(data)
                    self.insert_temperature_calculations(new_calculations)
                    EventLogger2.app_event.debug("fetch_temperature monitor train()=")
                # Perform analysis periodically
                if time.time() - last_analysis_time >= analysis_interval:
                    analysis.get_total_axles(data)
                    last_analysis_time = time.time()
                    EventLogger2.app_event.debug("fetch_temperature monitor train()2=")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")
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
            logger.debug("calculations done.")
            print(f"TrainId: {row[0]}, Axle_No: {row[1]}, {T1}, {T2}, Timestamp: {row[2]}, System_Timestamp: {row[5]}")
            EventLogger2.app_event.debug("calculate_temperatures")
        return calculations

    def get_total_axles(self, data):
        axle_numbers = {row[1] for row in data}
        total_axles = len(axle_numbers)
        print(f"Total number of unique Axle_Nos: {total_axles}")
        return total_axles
