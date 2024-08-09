import pyodbc
import json
from datetime import datetime
import time

class TemperatureDatabase:
    def __init__(self, db_config):
        self.connection = self.connect_to_database(db_config)
        self.known_axle_numbers = set()
        self.processed_axle_numbers = set()
        self.current_train_id = None
        self.shared_train_id = None

    def connect_to_database(self, db_config):
        connection_string = (
            f"DRIVER={db_config['driver']};"
            f"SERVER={db_config['server']};"
            f"DATABASE={db_config['database']};"
            f"Trusted_Connection={db_config['trusted_connection']};"
        )
        try:
            connection = pyodbc.connect(connection_string)
            return connection
        except pyodbc.Error as e:
            print(f"Error connecting to database: {e}")
            return None

    def fetch_temperature(self, train_id):
        if not self.connection:
            print("No database connection.")
            return []

        query = "SELECT TrainId, Axle_No, Timestamp, T1, T2, System_Timestamp FROM Temperature WHERE TrainId = ?;"
        try:
            with self.connection.cursor() as cursor:
                cursor.execute(query, (train_id,))
                rows = cursor.fetchall()
                return rows
        except pyodbc.Error as e:
            print(f"Error fetching data: {e}")
            return []

    def check_for_new_axle_no(self, train_id):
        if train_id != self.current_train_id:
            self.processed_axle_numbers.clear()
            self.current_train_id = train_id

        data = self.fetch_temperature(train_id)
        new_axles = [row for row in data if row[1] not in self.known_axle_numbers]
        
        for row in new_axles:
            self.known_axle_numbers.add(row[1])
            print(f"New Axle Detected - TrainId: {row[0]}, Axle_No: {row[1]}, Timestamp: {row[2]}, T1: {row[3]}, T2: {row[4]}, System_Timestamp: {row[5]}")
            
        return new_axles

    def monitor_train(self, train_id, analysis, interval=10, analysis_interval=60):
        print(f"Monitoring train {train_id} for new axle numbers...")
        last_analysis_time = time.time()

        try:
            while True:
                new_axles = self.check_for_new_axle_no(train_id)
                if new_axles:
                    data = self.fetch_temperature(train_id)
                    new_calculations = analysis.calculate_temperatures(data)
                    self.insert_temperature_calculations(new_calculations)

                if time.time() - last_analysis_time >= analysis_interval:
                    analysis.get_total_axles(data)
                    last_analysis_time = time.time()
                
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")
        finally:
            self.close_connection()

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
                        self.processed_axle_numbers.add(calc[1])
                self.connection.commit()
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
            T1 = t1 - 5
            T2 = t2 + 5
            calculations.append((row[0], row[1], T1, T2))
            print(f"TrainId: {row[0]}, Axle_No: {row[1]}, {T1}, {T2}, Timestamp: {row[2]}, System_Timestamp: {row[5]}")
        return calculations

    def get_total_axles(self, data):
        axle_numbers = {row[1] for row in data}
        total_axles = len(axle_numbers)
        print(f"Total number of unique Axle_Nos: {total_axles}")
        return total_axles
