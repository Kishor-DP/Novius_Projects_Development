


import pyodbc
from datetime import datetime
import time
import logging
import EventLogger2
import json
from json.decoder import JSONDecodeError
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

class insert_Into_tblAlarms:
    def __init__(self):
        self.connection = self.connect_to_database()
        self.current_train_id=None
        self.train_start_value=None
        
        print("self.current_train_id",self.current_train_id)
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
            print(f"Error connecting to database: {e}")
            logger.debug(f"Error connecting to database: {e}")
            return None
    def read_TrainId_Fromjson(self, max_retries=31536063734300000, retry_interval=1):
            retries = 0
            while retries < max_retries:
                try:
                    with open('TrainId.json', 'r') as json_file:
                        TrainId_data = json.load(json_file)
                        self.current_train_id = TrainId_data.get("TrainId", False)
                        print(self.current_train_id)
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
                    print("self.TrainStart",self.TrainStart)
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
        EventLogger2.app_event.info(f"received train_id from main fetch_tblTemperatureForCalc={train_id}")
        train_id=self.read_TrainId_Fromjson()
        if not self.connection:
            print("No database connection.")
            return [],train_id
            
        query = "SELECT intTempLogId,intTrainId,intBogiTypeId,intAxleNo,[IntCoachPosition],[decTs1],[decTs2],[decTs3],[decTs4],[decTs5]      ,[decTs6],[decAxel_Speed]      ,[nvcharDescription]      ,[dtDateofCreation]      ,[dtDateofModification]     ,[ynDeleted] FROM tblTemperatureLog WHERE intTrainId = ?;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (train_id,))
                rows = cursor.fetchall()
                #EventLogger2.app_event.info(f"fetch_tblTemperatureForCalc={rows}")
                #print(f"fetch_tblTemperatureForCalc={rows}")
                return rows
        except pyodbc.Error as e:
            print(f"Error fetching data: {e}")
            return []
        
    def fetch_settings_from_mstAlarm_WarningSettings(self):
        query = """
        SELECT 
            [intAlarm_WarningID],
            [IntStationId],
            [intBogiTypeId],
            [nvcharTypeOfBogi],
            [decAlarmTemprature],
            [decWarningTemprature],
            [nvcharErrorCode],
            [nvcharDescription],
            [dtDateofCreation],
            [dtDateofModification],
            [ynDeleted]
        FROM 
            mstAlarm_WarningSettings;
        """
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query)
                row = cursor.fetchone()  # Fetch the first row
                if row:
                    # Assuming decAlarmTemprature is the 5th column and decWarningTemprature is the 6th column
                    decAlarmTemprature = row[4]
                    decWarningTemprature = row[5]

                    print(f"Alarm Temperature: {decAlarmTemprature}, Warning Temperature: {decWarningTemprature}")
                    return decAlarmTemprature, decWarningTemprature
                else:
                    print("No data found.")
                    return None, None
        except pyodbc.Error as e:
            print(f"Error fetching data: {e}")
            return None, None
        
    def Calculations_for_fetchedtbl(self,decAlarmTemprature, decWarningTemprature):

        print("decAlarmTemprature, decWarningTemprature",decAlarmTemprature, decWarningTemprature)



if __name__ == "__main__":
    starter=insert_Into_tblAlarms()
    TrainId=starter.read_TrainId_Fromjson()

    starter.read_TrainStart_Fromjson()
    starter.fetch_tblTemperatureForCalc(TrainId)
    decAlarmTemprature, decWarningTemprature=starter.fetch_settings_from_mstAlarm_WarningSettings()
    starter.Calculations_for_fetchedtbl(decAlarmTemprature, decWarningTemprature)