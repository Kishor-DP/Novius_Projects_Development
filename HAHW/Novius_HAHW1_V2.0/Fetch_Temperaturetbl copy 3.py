import pyodbc
from datetime import datetime
import time

class TemperatureDatabase:
    def __init__(self):
        self.connection = self.connect_to_database()
        self.known_axle_numbers = set()

    def connect_to_database(self):
        connection_string = (
            r"DRIVER={SQL Server};"
            r"SERVER=4MVDUGL\SQLEXPRESS;"
            r"DATABASE=PLC;"
            r"Trusted_Connection=yes;"
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
                self.check_for_new_axle_no(train_id)
                
                # Perform analysis periodically
                if time.time() - last_analysis_time >= analysis_interval:
                    data = self.fetch_temperature(train_id)
                    analysis.calculate_temperatures(data)
                    analysis.get_total_axles(data)
                    last_analysis_time = time.time()
                
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")
        finally:
            self.close_connection()

    def close_connection(self):
        if self.connection:
            self.connection.close()

class TemperatureAnalysis:
    def __init__(self, db):
        self.db = db

    def calculate_temperatures(self, data):
        calculations = []
        for row in data:
            t1, t2 = row[3], row[4]
            total_temp = t1 + t2
            calculations.append((row[0], row[1], row[2], total_temp, row[5]))
            print(f"TrainId: {row[0]}, Axle_No: {row[1]}, Total Temperature: {total_temp}, Timestamp: {row[2]}, System_Timestamp: {row[5]}")
        return calculations

    def get_total_axles(self, data):
        axle_numbers = {row[1] for row in data}
        total_axles = len(axle_numbers)
        print(f"Total number of unique Axle_Nos: {total_axles}")
        return total_axles

if __name__ == "__main__":
    db = TemperatureDatabase()
    analysis = TemperatureAnalysis(db)
    train_id = '2024_08_03_20_28_29_2000'  # Replace with actual TrainId
    
    # Monitor train for new axle numbers and perform analysis
    db.monitor_train(train_id, analysis, interval=5, analysis_interval=6)  # Check every 5 seconds and analyze every 60 seconds
