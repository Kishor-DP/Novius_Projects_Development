#Insert_Into_tblTemperatureLog.py
import pyodbc
from datetime import datetime
import time
import logging
import EventLogger2
import json
from json.decoder import JSONDecodeError
from calibration import calibration_formula
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set your application's logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        #logging.FileHandler('opcua_data_receiver.log'),
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
        self.current_train_id=None
        self.train_start_value=None
        self.train_active = None
        print("self.current_train_id",self.current_train_id)
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
                    self.train_start_value = self.TrainStart
                    return self.TrainStart
            except FileNotFoundError:
                logger.warning(f"File not found. Retrying in {retry_interval} seconds...")
            except JSONDecodeError:
                logger.warning(f"Invalid JSON data. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
            retries += 1
        return False
    
    def fetch_temperature(self, train_id):
        EventLogger2.app_event.info(f"received train_id from main fetch_temperature={train_id}")
        train_id=self.read_TrainId_Fromjson()
        if not self.connection:
            print("No database connection.")
            return [],train_id
            
        query = "SELECT TrainId, Axle_No, Timestamp, T1, T2, System_Timestamp FROM Temperature WHERE TrainId = ?;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (train_id,))
                rows = cursor.fetchall()
                #EventLogger2.app_event.info(f"fetch_temperature={rows}")
                return rows
        except pyodbc.Error as e:
            print(f"Error fetching data: {e}")
            return []

    def check_for_new_axle_no(self, train_id):
        # Reset processed axles if a new train ID is detected
        if train_id != self.current_train_id:
            self.processed_axle_numbers.clear()
            self.current_train_id = train_id  # Update current_train_id to the new one
        
        # Fetch the latest temperature data for the given train_id
        data = self.fetch_temperature(train_id)
        EventLogger2.app_event.debug(f"Fetched temperature data: {data}")

        # Identify new axles not present in known_axle_numbers
        new_axles = [row for row in data if row[1] not in self.known_axle_numbers]
        EventLogger2.app_event.debug(f"Identified new axles: {new_axles}")

        # Add new axles to known_axle_numbers and process them
        for row in new_axles:
            axle_no = row[1]
            if axle_no not in self.known_axle_numbers:
                self.known_axle_numbers.add(axle_no)
                EventLogger2.app_event.debug(f"Adding axle number {axle_no} to known_axle_numbers")
                print(f"New Axle Detected - TrainId: {row[0]}, Axle_No: {axle_no}, Timestamp: {row[2]}, T1: {row[3]}, T2: {row[4]}, System_Timestamp: {row[5]}")
                
                
                # Perform temperature calculations for the new axle
                db = TemperatureDatabase()
                analysis = TemperatureAnalysis(db)
                data = self.fetch_temperature(train_id)
                new_calculations = analysis.calculate_temperatures(data)
                self.insert_temperature_calculations(new_calculations)
                # After successful insertion, mark the axle as processed
                self.processed_axle_numbers.add(axle_no)

        # Debugging: print updated known_axle_numbers and processed_axle_numbers
        EventLogger2.app_event.debug(f"Updated known_axle_numbers: {self.known_axle_numbers}")
        EventLogger2.app_event.debug(f"Processed axle numbers: {self.processed_axle_numbers}")

        return new_axles
    
    def monitor_train(self, train_id, analysis, interval=5, analysis_interval=5):
        print(f"Monitoring train {train_id} for new axle numbers...")
        last_analysis_time = time.time()
        
        while True:
            train_id=self.read_TrainId_Fromjson()
            self.read_TrainStart_Fromjson()
            train_start_value = self.train_start_value
            
            if train_start_value and not self.train_active:
                # TrainStart became True, start processing
                self.train_active = True
                self.insert_into_tblTrainTransaction(train_id)
                new_axles = self.check_for_new_axle_no(train_id)
                data = self.fetch_temperature(train_id)
                new_calculations = analysis.calculate_temperatures(data)
                
                
                logger.info(f"New TrainId acquired: {self.current_train_id}")
            
            elif not train_start_value and self.train_active:
                # TrainStart became False, reset the TrainId for next activation

                self.train_active = False
                self.known_axle_numbers.clear()
                self.processed_axle_numbers.clear()
                logger.info(f"TrainStart is False, resetting.")
                continue  # Skip the rest of the loop to avoid processing

            if self.train_active:
                
                if new_axles:
                    data = self.fetch_temperature(train_id)
                    self.insert_temperature_calculations(new_calculations)
                    EventLogger2.app_event.debug(f"fetch_temperature monitor train{self.current_train_id}")
                    
                # Perform analysis periodically
                if time.time() - last_analysis_time >= analysis_interval:
                    new_axles = self.check_for_new_axle_no(train_id)
                    EventLogger2.app_event.debug(f"last_analysis_time{last_analysis_time}")
                    EventLogger2.app_event.debug(f"new axle detected{new_axles}")

                    analysis.get_total_axles(data)
                    EventLogger2.app_event.debug(f"Perform analysis periodically{data}")
                    last_analysis_time = time.time()
                    
                    EventLogger2.app_event.debug(f"fetch_temperature monitor train{self.current_train_id}")
                    EventLogger2.app_event.debug(f"processed_axle_numbers{self.processed_axle_numbers}")
                    EventLogger2.app_event.debug(f"known_axle_numbers{self.known_axle_numbers}")
                    
                    EventLogger2.app_event.debug(f"check_for_new_axle_no data = self.fetch_temperature{data}")
            time.sleep(interval)

    def insert_temperature_calculations(self, calculations):
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
                        EventLogger2.app_event.debug(f"processed_axle_numbers{self.processed_axle_numbers}")
                self.connection.commit()
        except pyodbc.Error as e:
            print(f"Error inserting data: {e}")

    def insert_into_tblTrainTransaction(self,tblTrainTransaction):
        self.connection.cursor()
        print ("add tblTrainTransaction entry here....................")
        query = """
        INSERT INTO [NVS_HAHW_V2].[dbo].[tblTrainTransaction] (intTrainId)
        VALUES (?)
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query,tblTrainTransaction)
        except pyodbc.Error as e:
            print(f"Error inserting data: {e}")


    def close_connection(self):
        if self.connection:
            self.connection.close()

class TemperatureAnalysis:
    def __init__(self, db):
        self.db = db

    def calculate_temperatures(self, data):
        
        calculations = []
        for row in data:
            t1 = row[3]
            t2 = row[4]
            #T1 = t1 - 5
            #T2 = t2 + 5
            calibration_data = calibration_formula()
            # Iterate over calibration data and calculate actual temperatures
            for slopes_offsets in calibration_data:
                slope1, offset1, slope2, offset2, slope3, offset3, slope4, offset4 = slopes_offsets
            # Calculating actual temperatures
            T1 = (t1 - offset1) / slope1
            T2 = (t2 - offset2) / slope2
            #t3 = (t1 - offset3) / slope3
            #t4 = (t2 - offset4) / slope4
            calculations.append((row[0], row[1], T1, T2))
            print(f'Actual Temperature T1: {T1:.2f}°C')
            print(f'Actual Temperature T2: {T2:.2f}°C')
            #print(f'Actual Temperature T3: {t3:.2f}°C')
            #print(f'Actual Temperature T4: {t4:.2f}°C')
            logger.debug("calculations done.")
            #print(f"TrainId: {row[0]}, Axle_No: {row[1]}, {T1}, {T2}, Timestamp: {row[2]}, System_Timestamp: {row[5]}")
            EventLogger2.app_event.debug("calculate_temperatures")
        return calculations

    def get_total_axles(self, data):
        axle_numbers = {row[1] for row in data}
        total_axles = len(axle_numbers)
        print(f"Total number of unique Axle_Nos: {total_axles}")
        return total_axles

    

def main():
    db = TemperatureDatabase()
    analysis = TemperatureAnalysis(db)

    # Retrieve TrainId and TrainStart from JSON
    train_id = db.read_TrainId_Fromjson()
    db.read_TrainStart_Fromjson()

    # Check if TrainStart is True before monitoring
    
    db.monitor_train(train_id, analysis)
    

if __name__ == "__main__":
    main()