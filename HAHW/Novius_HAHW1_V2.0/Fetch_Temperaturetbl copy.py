#Fetch_Temperaturetbl.py
import pyodbc
from datetime import datetime

class TemperatureDatabase:
    def __init__(self):
        self.connection = self.connect_to_database()

    def connect_to_database(self):
        connection_string = (
            r"DRIVER={SQL Server};"
            r"SERVER=4MVDUGL\SQLEXPRESS;"
            r"DATABASE=PLC;"
            r"Trusted_Connection=yes;"
        )
        return pyodbc.connect(connection_string)

    # def insert_temperature(self, axle_no, timestamp, t1, t2):
    #     system_timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    #     query = """
    #         INSERT INTO Temperature (Axle_No, Timestamp, T1, T2, System_Timestamp)
    #         VALUES (?, ?, ?, ?, ?)
    #     """
    #     with self.connection.cursor() as cursor:
    #         cursor.execute(query, (axle_no, timestamp, t1, t2, system_timestamp))
    #         self.connection.commit()

    def fetch_temperature(self):
        query = "SELECT TrainId,Axle_No, Timestamp, T1, T2, System_Timestamp FROM Temperature WHERE T1 = '716';"
        with self.connection.cursor() as cursor:
            cursor.execute(query)
            rows = cursor.fetchall()
            return rows

# Example usage
Fetch_Temperaturetbl = TemperatureDatabase()

# Fetching data
Fetch_Temperaturetbl_data = Fetch_Temperaturetbl.fetch_temperature()
for row in Fetch_Temperaturetbl_data:
    print(f"TrainId: {row[0]},Axle_No: {row[1]}, Timestamp: {row[2]}, T1: {row[3]}, T2: {row[4]}, System_Timestamp: {row[4]}")
