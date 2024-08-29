import pyodbc
from datetime import datetime
import time
import logging
import EventLogger2
import json
from json.decoder import JSONDecodeError
import decimal
# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class insert_Into_tblAlarms:
    def __init__(self):
        self.connection = self.connect_to_database()
        self.current_train_id = None
        self.train_start_value = None
        
    def connect_to_database(self):
        connection_string = (
            r"DRIVER={SQL Server};"
            r"SERVER=4MVDUGL\KISHOR;"
            r"DATABASE=NVS_HAHW_V2;"
            r"Trusted_Connection=yes;"
        )
        try:
            connection = pyodbc.connect(connection_string)
            return connection
        except pyodbc.Error as e:
            logger.error(f"Error connecting to database: {e}")
            return None

    def read_TrainId_Fromjson(self, max_retries=31536063734300000, retry_interval=1):
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

    def read_TrainStart_Fromjson(self, max_retries=31536063734300000, retry_interval=1):
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
    
    def fetch_tblTemperatureForCalc(self, train_id):
        train_id = self.read_TrainId_Fromjson()
        if not self.connection:
            logger.error("No database connection.")
            return [], train_id
            
        query = """
        SELECT intTempLogId, intTrainId, intBogiTypeId, intAxleNo, IntCoachPosition, 
               decTs1, decTs2, decTs3, decTs4, decTs5, decTs6, decAxel_Speed, 
               nvcharDescription, dtDateofCreation, dtDateofModification, ynDeleted 
        FROM tblTemperatureLog 
        WHERE intTrainId = ?;
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (train_id,))
                rows = cursor.fetchall()
                return rows
        except pyodbc.Error as e:
            logger.error(f"Error fetching data: {e}")
            return []

    def fetch_settings_from_mstAlarm_WarningSettings(self):
        query = """
        SELECT decAlarmTemprature, decWarningTemprature
        FROM mstAlarm_WarningSettings;
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()  
                if row:
                    decAlarmTemprature = row[0]
                    decWarningTemprature = row[1]
                    return decAlarmTemprature, decWarningTemprature
                else:
                    logger.warning("No data found in mstAlarm_WarningSettings.")
                    return None, None
        except pyodbc.Error as e:
            logger.error(f"Error fetching data: {e}")
            return None, None
        
    
    def Calculations_for_fetchedtbl(self, decAlarmTemprature, decWarningTemprature):
        rows = self.fetch_tblTemperatureForCalc(self.current_train_id)
        if not rows:
            logger.warning("No data fetched for calculations.")
            return
        
        for row in rows:
            temperatures = row[5:11]  # decTs1 to decTs6
            axle_no = row[3]  # Assuming this is the axle number from the row
            for temp in temperatures:
                if temp is None:
                    logger.warning("Temperature value is None, skipping comparison.")
                    continue
                try:
                    temp = decimal.Decimal(temp)
                except decimal.InvalidOperation:
                    logger.warning(f"Invalid temperature value: {temp}")
                    continue
                
                if decAlarmTemprature is not None and temp > decAlarmTemprature:
                    logger.info(f"Temperature {temp} exceeds alarm threshold {decAlarmTemprature}")
                    self.insert_into_tblAlarms(self.current_train_id, axle_no, temp)
                    # Handle alarm condition
                elif decWarningTemprature is not None and temp > decWarningTemprature:
                    logger.info(f"Temperature {temp} exceeds warning threshold {decWarningTemprature}")
                    self.insert_into_tblWarning(self.current_train_id, axle_no, temp)
                    # Handle warning condition
    def insert_into_tblAlarms(self, train_id, axle_no, temperature):
        query = """
        INSERT INTO tblAlarms (intTrainId, intAxelNo, decTemperature)
        VALUES (?, ?, ?)
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (train_id, axle_no, temperature))
                self.connection.commit()  # Commit the transaction
                logger.info(f"Inserted alarm record for TrainId: {train_id}, AxleNo: {axle_no}, Temperature: {temperature}")
        except pyodbc.Error as e:
            logger.error(f"Error inserting data into tblAlarms: {e}")

    def insert_into_tblWarning(self, train_id, axle_no, temperature):
        query = """
        INSERT INTO tblWarning (intTrainId, intAxelNo, decTemperature)
        VALUES (?, ?, ?)
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (train_id, axle_no, temperature))
                self.connection.commit()  # Commit the transaction
                logger.info(f"Inserted alarm record for TrainId: {train_id}, AxleNo: {axle_no}, Temperature: {temperature}")
        except pyodbc.Error as e:
            logger.error(f"Error inserting data into tblAlarms: {e}")
if __name__ == "__main__":
    starter = insert_Into_tblAlarms()
    TrainId = starter.read_TrainId_Fromjson()
    starter.read_TrainStart_Fromjson()
    decAlarmTemprature, decWarningTemprature = starter.fetch_settings_from_mstAlarm_WarningSettings()
    starter.Calculations_for_fetchedtbl(decAlarmTemprature, decWarningTemprature)
