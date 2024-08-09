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

    def monitor_train(self, train_id, interval=10):
        print(f"Monitoring train {train_id} for new axle numbers...")
        try:
            while True:
                self.check_for_new_axle_no(train_id)
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Monitoring stopped.")
        finally:
            self.close_connection()

    def close_connection(self):
        if self.connection:
            self.connection.close()

if __name__ == "__main__":
    db = TemperatureDatabase()
    train_id = '2024_08_03_20_28_29_2000'  # Replace with actual TrainId
    db.monitor_train(train_id, interval=5)  # Check every 5 seconds
