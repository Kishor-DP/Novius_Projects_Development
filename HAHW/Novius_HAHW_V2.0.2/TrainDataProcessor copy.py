import pyodbc
import logging

# Set up logging
logging.basicConfig(level=logging.ERROR)
logger = logging.getLogger(__name__)

class TrainDataProcessor:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = None
        self.cursor = None
        self.connect_to_db()

    def connect_to_db(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()
        except Exception as e:
            logger.error(f"Database connection failed: {e}")
            return

    def fetch_proxy_s1_data(self, train_id):
        query = f"""
        SELECT [intDBAxleCount], [TrainId], [S1], [S1_Timestamp], [S1_System_Timestamp]
        FROM [NVS_HAHW_V2].[dbo].[Proxy_s1]
        WHERE [TrainId] = ?
        """
        self.cursor.execute(query, train_id)
        data = self.cursor.fetchall()
        print("Proxy_s1 Data:")
        for row in data:
            print(row)
        return data


    def fetch_temperature_data(self, train_id):
        query = f"""
        SELECT [intDBAxleCount], [TrainId], [T1], [T2], [T3], [T4], [T5], [T6], [Timestamp], [Axle_No], [System_Timestamp]
        FROM [NVS_HAHW_V2].[dbo].[Temperature]
        WHERE [TrainId] = ?
        """
        self.cursor.execute(query, train_id)
        data = self.cursor.fetchall()
        print("Temperature Data:")
        for row in data:
            print(row)
        return data

    def process_and_insert_data(self, train_id):
        proxy_s1_data = self.fetch_proxy_s1_data(train_id)
        temperature_data = self.fetch_temperature_data(train_id)

        if len(proxy_s1_data) != len(temperature_data):
            logger.error("Axle count mismatch between Proxy_s1 and Temperature tables.")
            return

        for index in range(len(proxy_s1_data)):
            s1_row = proxy_s1_data[index]
            temp_row = temperature_data[index]

            # Match based on specific row index
            if s1_row[2] == temp_row[9]:  # Matching S1 and Axle_No for the same record number
                addition_result = s1_row[3] + temp_row[8]  # Adding S1_Timestamp and Timestamp
                self.insert_into_tblSpeedDistance(addition_result)

    def insert_into_tblSpeedDistance(self, addition_result):
        query = f"""
        INSERT INTO [NVS_HAHW_V2].[dbo].[tblSpeedDistance] ([addition_result])
        VALUES (?)
        """
        self.cursor.execute(query, addition_result)
        self.conn.commit()

    def close_connection(self):
        if self.cursor:
            self.cursor.close()
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    connection_string = (
        r"DRIVER={SQL Server};"
        r"SERVER=4MVDUGL\SQLEXPRESS;"
        r"DATABASE=NVS_HAHW_V2;"
        r"Trusted_Connection=yes;"
    )

    processor = TrainDataProcessor(connection_string)
    processor.process_and_insert_data('2024_08_16_16_58_18_2000')
    processor.close_connection()
