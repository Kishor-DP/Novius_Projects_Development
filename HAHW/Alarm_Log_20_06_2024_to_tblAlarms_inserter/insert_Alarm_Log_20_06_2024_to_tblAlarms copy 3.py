import json
import pyodbc
import time
import logging
from decimal import Decimal

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class GlobalVariableHolder:
    global_variable = None

    @classmethod
    def set_global_variable(cls, new_value):
        cls.global_variable = new_value

    @classmethod
    def get_global_variable(cls):
        return cls.global_variable

class DatabaseConnector:
    AlarmTempratureSetting = None
    WarningTempratureSetting = None

    def __init__(self, config_file):
        self.config = self.load_db_config(config_file)
        self.connection = self.connect_to_database()

    @staticmethod
    def convert_decimal_to_float(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

    @staticmethod
    def load_db_config(config_file):
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
            logging.info("Database configuration loaded successfully.")
            return config
        except Exception as e:
            logging.error(f"Error loading database configuration: {e}")
            exit()

    def connect_to_database(self):
        connection_string = f"DRIVER={{SQL Server}};SERVER={self.config['server']};DATABASE={self.config['database']};UID={self.config['username']};PWD={self.config['password']}"
        try:
            connection = pyodbc.connect(connection_string)
            logging.info("Connection to the database was successful.")
            return connection
        except Exception as e:
            logging.error(f"Error connecting to the database: {e}")
            exit()

    def fetch_results(self, query):
        cursor = self.connection.cursor()
        try:
            cursor.execute(query)
            rows = cursor.fetchall()
            logging.info("Fetched results from the database successfully.")
            return rows
        except Exception as e:
            logging.error(f"Error fetching results: {e}")
            exit()
        finally:
            cursor.close()

    @staticmethod
    def save_results_to_json(results, tmp_log_results_json):
        try:
            with open(tmp_log_results_json, 'w') as file:
                json.dump(results, file, default=DatabaseConnector.convert_decimal_to_float, indent=4)
            logging.info(f"Results saved to tmp_log_results_json {tmp_log_results_json}")
        except Exception as e:
            logging.error(f"Error saving results to JSON: {e}")

    @staticmethod
    def load_and_filter_settings(input_file, settings_json):
        try:
            with open(input_file, 'r') as file:
                data = json.load(file)

            filtered_records = [
                record for record in data if record.get("nvcharDescription") == "Absolute Axle Temperature"
            ]
            print(filtered_records)
            for record in filtered_records:
                logging.info(f"decAlarmTemprature: {record['decAlarmTemprature']}")
                logging.info(f"decWarningTemprature: {record['decWarningTemprature']}")
                DatabaseConnector.AlarmTempratureSetting = record['decAlarmTemprature']
                DatabaseConnector.WarningTempratureSetting = record['decWarningTemprature']
                print(f"Alarm Temperature Setting: {DatabaseConnector.AlarmTempratureSetting}")
                print(f"Warning Temperature Setting: {DatabaseConnector.WarningTempratureSetting}")
                GlobalVariableHolder.set_global_variable(DatabaseConnector.WarningTempratureSetting)

            with open(settings_json, 'w') as file:
                json.dump(filtered_records, file, default=DatabaseConnector.convert_decimal_to_float, indent=4)

            logging.info(f"Filtered records saved to {settings_json}")
        except FileNotFoundError:
            logging.error(f"File not found: {input_file}")
        except json.JSONDecodeError:
            logging.error(f"Error decoding JSON from the file: {input_file}")
        except KeyError as e:
            logging.error(f"Missing expected key: {e}")
        except TypeError as e:
            logging.error(f"Type error: {e}")
        except Exception as e:
            logging.error(f"An unexpected error occurred: {e}")

# Example usage:
# load_and_filter_settings('input.json', 'output.json')

    def close_connection(self):
        self.connection.close()
        logging.info("Database connection closed.")

    @classmethod
    def get_alarm_temperature_setting(cls):
        return cls.AlarmTempratureSetting

    @classmethod
    def get_warning_temperature_setting(cls):
        return cls.WarningTempratureSetting

class AlarmLogInserter:
    def __init__(self, config_file):
        self.config = self.load_db_config(config_file)
        self.connection = self.connect_to_database()

    @staticmethod
    def load_db_config(config_file):
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
            logging.info("Database configuration loaded successfully.")
            return config
        except Exception as e:
            logging.error(f"Error loading database configuration: {e}")
            exit()

    def connect_to_database(self):
        connection_string = f"DRIVER={{SQL Server}};SERVER={self.config['server']};DATABASE={self.config['database']};UID={self.config['username']};PWD={self.config['password']}"
        try:
            connection = pyodbc.connect(connection_string)
            logging.info("Connection to the database was successful.")
            return connection
        except Exception as e:
            logging.error(f"Error connecting to the database: {e}")
            exit()
    def data_insert_into_Alarm_Log_20_06_2024():
        print("data insert compare can be added here and then use in any function")
    
    def insert_data(self, data):
        print(data)
        if not self.connection:
            logging.error("No database connection available.")
            return

        try:
            cursor = self.connection.cursor()
            for row in data:
                intTempLogId = row[0]
                # Check if intTempLogId already exists
                cursor.execute("SELECT COUNT(*) FROM [dbo].[Alarm_Log_20_06_2024] WHERE intTempLogId = ?", (intTempLogId,))
                if cursor.fetchone()[0] == 0:
                    cursor.execute("""
                        INSERT INTO [dbo].[Alarm_Log_20_06_2024] (
                            [intTempLogId],
                            [NvcharCoachNo],
                            [intTrainId],
                            [intBogiTypeId],
                            [intAxleNo],
                            [IntCoachPosition],
                            [decTs1],
                            [decTs2],
                            [decTs3],
                            [decTs4],
                            [decTs5],
                            [decTs6],
                            [decAxel_Speed],
                            [nvcharDescription],
                            [dtDateofCreation],
                            [dtDateofModification],
                            [ynDeleted]
                        ) 
                        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?,?)
                    """, row)
                else:
                    logging.warning(f"intTempLogId {intTempLogId} already exists. Skipping insertion.")
            self.connection.commit()
            logging.info("Data inserted successfully!")
        except Exception as e:
            self.connection.rollback()
            logging.error(f"Error inserting data into the database: {e}")
        finally:
            self.close_connection()

    def close_connection(self):
        if self.connection:
            try:
                self.connection.close()
                logging.info("Database connection closed.")
            except Exception as e:
                logging.error(f"Error closing database connection: {e}")
class TableMonitor:
    def __init__(self, config_file):
        self.config = self.load_db_config(config_file)
        self.connection = self.connect_to_database()
        self.last_checked_timestamp = self.read_last_checked_timestamp()

    @staticmethod
    def load_db_config(config_file):
        try:
            with open(config_file, 'r') as file:
                config = json.load(file)
            logging.info("Database configuration loaded successfully.")
            return config
        except Exception as e:
            logging.error(f"Error loading database configuration: {e}")
            exit()

    def connect_to_database(self):
        connection_string = f"DRIVER={{SQL Server}};SERVER={self.config['server']};DATABASE={self.config['database']};UID={self.config['username']};PWD={self.config['password']}"
        try:
            connection = pyodbc.connect(connection_string)
            logging.info("Connection to the database was successful.")
            return connection
        except Exception as e:
            logging.error(f"Error connecting to the database: {e}")
            exit()

    def read_last_checked_timestamp(self):
        try:
            with open('last_checked_timestamp.json', 'r') as file:
                data = json.load(file)
                return data['intTrainId']
        except FileNotFoundError:
            logging.warning("Timestamp file not found, using default value.")
            return 231449
        except Exception as e:
            logging.error(f"Error reading timestamp file: {e}")
            raise

    def write_last_checked_timestamp(self, last_checked_timestamp):
        try:
            with open('last_checked_timestamp.json', 'w') as file:
                json.dump({"intTrainId": last_checked_timestamp}, file)
            with open('config1.json', 'w') as file:
                json.dump({"intTrainId": last_checked_timestamp}, file)
        except Exception as e:
            logging.error(f"Error writing timestamp file: {e}")

    def get_latest_inserts(self, last_checked_timestamp):
        cursor = self.connection.cursor()
        try:
            cursor.execute("SELECT * FROM tblTrainTransaction WHERE intTrainId > ?", (last_checked_timestamp,))
            rows = cursor.fetchall()
            return rows
        except Exception as e:
            logging.error(f"Error fetching latest inserts: {e}")
            raise
        finally:
            cursor.close()
    
    def process_new_inserts(self, new_rows):
        for row in new_rows:
            logging.info(f"New row inserted: {row}")
            print("add process")
            main()
            new_insert_flag = 1
    def monitor_table(self):
        try:
            while True:
                new_rows = self.get_latest_inserts(self.last_checked_timestamp)
                if new_rows:
                    self.process_new_inserts(new_rows)
                    self.last_checked_timestamp = new_rows[-1].intTrainId
                    self.write_last_checked_timestamp(self.last_checked_timestamp)
                time.sleep(10)
        except KeyboardInterrupt:
            logging.info("Monitoring stopped by user.")
        except Exception as e:
            logging.error(f"Unexpected error: {e}")
        finally:
            self.connection.close()
            logging.info("Database connection closed.")

    def close_connection(self):
        self.connection.close()
        logging.info("Database connection closed.")

def run_table_monitor():
    # Run TableMonitor
    config_file = 'db_config.json'
    table_monitor = TableMonitor(config_file)
    table_monitor.monitor_table()

class TemperatureLogDB:
    def __init__(self, config_file):
        self.config = self.load_db_config(config_file)
        self.connection = self.connect_to_database(self.config)
        self.cursor = self.connection.cursor()

    @staticmethod
    def convert_decimal_to_float(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

    @staticmethod
    def load_db_config(config_file):
        with open(config_file, 'r') as file:
            return json.load(file)

    def connect_to_database(self, config):
        connection_string = f"DRIVER={{SQL Server}};SERVER={config['server']};DATABASE={config['database']};UID={config['username']};PWD={config['password']}"
        try:
            connection = pyodbc.connect(connection_string)
            print("Connection successful!")
            return connection
        except Exception as e:
            print("Error connecting to the database:", e)
            exit()

    def fetch_results(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows

    def save_results_to_json(self, results, tmp_log_results_json):
        with open(tmp_log_results_json, 'w') as file:
            json.dump(results, file, default=self.convert_decimal_to_float, indent=4)
        print(f"Results saved to {tmp_log_results_json}")

    def fetch_temperature_log(self, TemperatureLogDB_tmp_log_reslt,return_value):
        
        query = """
        SELECT TOP 200
            [intTempLogId]
            ,[intTrainId]
            ,[intBogiTypeId]
            ,[intAxleNo]
            ,[NvcharCoachNo]
            ,[IntCoachPosition]
            ,[decTs1]
            ,[decTs2]
            ,[decTs3]
            ,[decTs4]
            ,[decTs5]
            ,[decTs6]
            ,[decAxel_Speed]
            ,[nvcharDescription]
            ,[dtDateofCreation]
            ,[dtDateofModification]
            ,[ynDeleted]
        FROM [dbo].[tblTemperatureLog]
        ORDER BY [intTempLogId] DESC
        """
        
        rows = self.fetch_results(query)
        
        filtered_rows = [
            row for row in rows
            if any(
                (float(getattr(row, f"decTs{i}")) if getattr(row, f"decTs{i}") is not None else float('-inf')) > return_value
                for i in range(1, 7)
            )
        ]
        
        results = [
            {
                "intTempLogId": row.intTempLogId,
                "intTrainId": row.intTrainId,
                "intBogiTypeId": row.intBogiTypeId,
                "intAxleNo": row.intAxleNo,
                "NvcharCoachNo": row.NvcharCoachNo,
                "IntCoachPosition": row.IntCoachPosition,
                "decTs1": float(row.decTs1) if row.decTs1 is not None else None,
                "decTs2": float(row.decTs2) if row.decTs2 is not None else None,
                "decTs3": float(row.decTs3) if row.decTs3 is not None else None,
                "decTs4": float(row.decTs4) if row.decTs4 is not None else None,
                "decTs5": float(row.decTs5) if row.decTs5 is not None else None,
                "decTs6": float(row.decTs6) if row.decTs6 is not None else None,
                "decAxel_Speed": float(row.decAxel_Speed) if row.decAxel_Speed is not None else None,
                "nvcharDescription": row.nvcharDescription,
                "dtDateofCreation": row.dtDateofCreation.strftime('%Y-%m-%d %H:%M:%S') if row.dtDateofCreation else None,
                "dtDateofModification": row.dtDateofModification.strftime('%Y-%m-%d %H:%M:%S') if row.dtDateofModification else None,
                "ynDeleted": row.ynDeleted
            }
            for row in filtered_rows
        ]
        print("tempfetchlogfunction",return_value)
        
        print("tempfetchlogfunction", return_value)
        self.save_results_to_json(results, TemperatureLogDB_tmp_log_reslt)

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

class fetch_from_Alarm_Log_20_06_2024_insert_to_tblAlarms:
    def __init__(self, config_file):        
        self.config = self.load_db_config(config_file)
        self.connection = self.connect_to_database(self.config)
        self.cursor = self.connection.cursor()

    @staticmethod
    def load_db_config(config_file):
        with open(config_file, 'r') as file:
            return json.load(file)

    @staticmethod
    def convert_decimal_to_float(obj):
        if isinstance(obj, Decimal):
            return float(obj)
        raise TypeError(f'Object of type {obj.__class__.__name__} is not JSON serializable')

    def connect_to_database(self, config):
        connection_string = f"DRIVER={{SQL Server}};SERVER={config['server']};DATABASE={config['database']};UID={config['username']};PWD={config['password']}"
        try:
            connection = pyodbc.connect(connection_string)
            print("Connection successful!")
            return connection
        except Exception as e:
            print("Error connecting to the database:", e)
            exit()

    def fetch_results(self, query):
        self.cursor.execute(query)
        rows = self.cursor.fetchall()
        return rows
    
    def save_results_to_json(self, results, Alarm_Log_20_06_2024):
        with open(Alarm_Log_20_06_2024, 'w') as file:
            json.dump(results, file, default=self.convert_decimal_to_float, indent=4)
        print(f"Results saved to {Alarm_Log_20_06_2024}")

    def Alarm_Log_20_06_2024_fetcher(self, Alarm_Log_20_06_2024):
        query = """
        SELECT TOP 200
            [intTempLogId]
            ,[intTrainId]
            ,[intBogiTypeId]
            ,[intAxleNo]
            ,[NvcharCoachNo]
            ,[IntCoachPosition]
            ,[decTs1]
            ,[decTs2]
            ,[decTs3]
            ,[decTs4]
            ,[decTs5]
            ,[decTs6]
            ,[decAxel_Speed]
            ,[nvcharDescription]
            ,[dtDateofCreation]
            ,[dtDateofModification]
            ,[ynDeleted]
        FROM [dbo].[Alarm_Log_20_06_2024]
        ORDER BY [intTempLogId] DESC
        """
        
        rows = self.fetch_results(query)
        
        filtered_rows = [row for row in rows]
        
        results = [
            {
                "intTempLogId": row.intTempLogId,
                "intTrainId": row.intTrainId,
                "intBogiTypeId": row.intBogiTypeId,
                "intAxleNo": row.intAxleNo,
                "NvcharCoachNo": row.NvcharCoachNo,
                "IntCoachPosition": row.IntCoachPosition,
                "decTs1": float(row.decTs1) if row.decTs1 is not None else None,
                "decTs2": float(row.decTs2) if row.decTs2 is not None else None,
                "decTs3": float(row.decTs3) if row.decTs3 is not None else None,
                "decTs4": float(row.decTs4) if row.decTs4 is not None else None,
                "decTs5": float(row.decTs5) if row.decTs5 is not None else None,
                "decTs6": float(row.decTs6) if row.decTs6 is not None else None,
                "decAxel_Speed": float(row.decAxel_Speed) if row.decAxel_Speed is not None else None,
                "nvcharDescription": row.nvcharDescription,
                "dtDateofCreation": row.dtDateofCreation.strftime('%Y-%m-%d %H:%M:%S') if row.dtDateofCreation else None,
                "dtDateofModification": row.dtDateofModification.strftime('%Y-%m-%d %H:%M:%S') if row.dtDateofModification else None,
                "ynDeleted": row.ynDeleted
            }
            for row in filtered_rows
        ]
        print("tempfetchlogfunction")
        
        self.save_results_to_json(results, Alarm_Log_20_06_2024)

    def insert_Alarm_Log_20_06_2024_into_tblAlarms(self, json_file):
        alarm_temp_settings = DatabaseConnector.get_alarm_temperature_setting()
        warning_temp_settings = DatabaseConnector.get_warning_temperature_setting()
        with open(json_file, 'r') as file:
            data = json.load(file)

        for record in data:
            intTempLogId = record.get("intTempLogId")
            
            # Check if the intTempLogId already exists
            check_query = "SELECT COUNT(*) FROM [dbo].[tblAlarms_test_insert] WHERE [intTempLogId] = ?"
            self.cursor.execute(check_query, (intTempLogId,))
            exists = self.cursor.fetchone()[0]

            if exists:
                print(f"Record with intTempLogId {intTempLogId} already exists. Skipping insertion.")
                continue

            # Extract and filter the temperature fields
            temperature_fields = [
                ("decTs1", record.get("decTs1")),
                ("decTs2", record.get("decTs2")),
                ("decTs3", record.get("decTs3")),
                ("decTs4", record.get("decTs4")),
                ("decTs5", record.get("decTs5")),
                ("decTs6", record.get("decTs6"))
            ]
            
            # Loop through each temperature field and insert if the value is greater than 80
            for field_name, temperature in temperature_fields:
                if temperature and temperature > alarm_temp_settings:
                    query = """
                    INSERT INTO [dbo].[tblAlarms_test_insert] (
                        [intTrainId],
                        [intTempLogId],
                        [intAxelNo],
                        [NvcharCoachNo],
                        [IntCoachPosition],
                        [decTemperature],
                        [nvcharDescription],
                        [dtDateofCreation],
                        [dtDateofModification],
                        [ynDeleted]
                    ) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
                    """
                    values = (
                        record.get("intTrainId"),
                        intTempLogId,
                        record.get("intAxleNo"),
                        record.get("NvcharCoachNo"),
                        record.get("IntCoachPosition"),
                        temperature,
                        record.get("nvcharDescription"),
                        record.get("dtDateofCreation"),
                        record.get("dtDateofModification"),
                        record.get("ynDeleted")
                    )

                    try:
                        self.cursor.execute(query, values)
                        self.connection.commit()
                        print(f"Record with {field_name}={temperature} from {json_file} inserted into tblAlarms.")
                    except KeyError as e:
                        print(f"KeyError: Missing key {e} in the record. Record content: {record}")
                    except Exception as e:
                        print(f"Unexpected error: {e}")

    def close_connection(self):
        self.cursor.close()
        self.connection.close()

    def Executor_for_Class_fetch_from_Alarm_Log_20_06_2024_insert_to_tblAlarms():
        config_file = 'db_config.json'
        Alarm_Log_20_06_2024 = 'Alarm_Log_20_06_2024.json'
        arugument_passing_Alarm_Log_20_06_2024_json = fetch_from_Alarm_Log_20_06_2024_insert_to_tblAlarms(config_file)
        arugument_passing_Alarm_Log_20_06_2024_json.Alarm_Log_20_06_2024_fetcher(Alarm_Log_20_06_2024)
        arugument_passing_Alarm_Log_20_06_2024_json.insert_Alarm_Log_20_06_2024_into_tblAlarms(Alarm_Log_20_06_2024)
        arugument_passing_Alarm_Log_20_06_2024_json.close_connection()

config_file = 'db_config.json'
results_file = 'results.json'
filtered_file = 'settings.json'
#for class TemperatureLogDB
config_file = 'db_config.json'
db_connector = DatabaseConnector(config_file)


query = """
SELECT TOP 1000 [intAlarm_WarningID]
        ,[IntStationId]
        ,[intBogiTypeId]
        ,[nvcharTypeOfBogi]
        ,[decAlarmTemprature]
        ,[decWarningTemprature]
        ,[nvcharErrorCode]
        ,[nvcharDescription]
        ,[dtDateofCreation]
        ,[dtDateofModification]
        ,[ynDeleted]
    FROM [HBDDB].[dbo].[mstAlarm_WarningSettings]
"""

rows = db_connector.fetch_results(query)

results = [
    {
        "intAlarm_WarningID": row.intAlarm_WarningID,
        "IntStationId": row.IntStationId,
        "intBogiTypeId": row.intBogiTypeId,
        "nvcharTypeOfBogi": row.nvcharTypeOfBogi,
        "decAlarmTemprature": float(row.decAlarmTemprature) if row.decAlarmTemprature is not None else None,
        "decWarningTemprature": float(row.decWarningTemprature) if row.decWarningTemprature is not None else None,
        "nvcharErrorCode": row.nvcharErrorCode,
        "nvcharDescription": row.nvcharDescription,
        "dtDateofCreation": row.dtDateofCreation.strftime('%Y-%m-%d %H:%M:%S') if row.dtDateofCreation else None,
        "dtDateofModification": row.dtDateofModification.strftime('%Y-%m-%d %H:%M:%S') if row.dtDateofModification else None,
        "ynDeleted": row.ynDeleted
    }
    for row in rows
]

db_connector.save_results_to_json(results, results_file)
db_connector.load_and_filter_settings(results_file, filtered_file)

db_connector.close_connection()
config_file = 'db_config.json'
TemperatureLogDB_tmp_log_reslt = 'temperature_log_results.json'
return_value=(GlobalVariableHolder.get_global_variable())
   
temperature_log_db = TemperatureLogDB(config_file)
temperature_log_db.fetch_temperature_log(TemperatureLogDB_tmp_log_reslt,return_value)
temperature_log_db.close_connection()
def main():
    config_file = 'db_config.json'
    results_file = 'results.json'
    filtered_file = 'settings.json'
    #for class TemperatureLogDB
    config_file = 'db_config.json'
    TemperatureLogDB_tmp_log_reslt = 'temperature_log_results.json'
    
    print(GlobalVariableHolder.get_global_variable())
    return_value=(GlobalVariableHolder.get_global_variable())
    print (return_value)

    temperature_log_db = TemperatureLogDB(config_file)
    temperature_log_db.fetch_temperature_log(TemperatureLogDB_tmp_log_reslt,return_value)
    temperature_log_db.close_connection()

    # Run DatabaseConnector first
    db_connector = DatabaseConnector(config_file)


    query = """
    SELECT TOP 1000 [intAlarm_WarningID]
          ,[IntStationId]
          ,[intBogiTypeId]
          ,[nvcharTypeOfBogi]
          ,[decAlarmTemprature]
          ,[decWarningTemprature]
          ,[nvcharErrorCode]
          ,[nvcharDescription]
          ,[dtDateofCreation]
          ,[dtDateofModification]
          ,[ynDeleted]
      FROM [HBDDB].[dbo].[mstAlarm_WarningSettings]
    """

    rows = db_connector.fetch_results(query)

    results = [
        {
            "intAlarm_WarningID": row.intAlarm_WarningID,
            "IntStationId": row.IntStationId,
            "intBogiTypeId": row.intBogiTypeId,
            "nvcharTypeOfBogi": row.nvcharTypeOfBogi,
            "decAlarmTemprature": float(row.decAlarmTemprature) if row.decAlarmTemprature is not None else None,
            "decWarningTemprature": float(row.decWarningTemprature) if row.decWarningTemprature is not None else None,
            "nvcharErrorCode": row.nvcharErrorCode,
            "nvcharDescription": row.nvcharDescription,
            "dtDateofCreation": row.dtDateofCreation.strftime('%Y-%m-%d %H:%M:%S') if row.dtDateofCreation else None,
            "dtDateofModification": row.dtDateofModification.strftime('%Y-%m-%d %H:%M:%S') if row.dtDateofModification else None,
            "ynDeleted": row.ynDeleted
        }
        for row in rows
    ]
    
    db_connector.save_results_to_json(results, results_file)
    db_connector.load_and_filter_settings(results_file, filtered_file)

    db_connector.close_connection()
    #print(return_value)
      # Run AlarmLogInserter
    
    alarm_log_inserter = AlarmLogInserter(config_file)

    with open('temperature_log_results.json', 'r') as file:
        data = json.load(file)

    

    alarm_log_inserter.insert_data([
        (
            row["intTempLogId"],
            row["NvcharCoachNo"],
            row["intTrainId"],
            row["intBogiTypeId"],
            row["intAxleNo"],
            row["IntCoachPosition"],
            row["decTs1"],
            row["decTs2"],
            row["decTs3"],
            row["decTs4"],
            row["decTs5"],
            row["decTs6"],
            row["decAxel_Speed"],
            row["nvcharDescription"],
            row["dtDateofCreation"],
            row["dtDateofModification"],
            row["ynDeleted"]
        )
        for row in data
    ])
    asdfs=(GlobalVariableHolder.get_global_variable())
    #print(asdfs)
    
    alarm_log_inserter.close_connection()
    fetch_from_Alarm_Log_20_06_2024_insert_to_tblAlarms.Executor_for_Class_fetch_from_Alarm_Log_20_06_2024_insert_to_tblAlarms()

    


if __name__ == "__main__":
    (GlobalVariableHolder.get_global_variable())
    #main()
    run_table_monitor()
