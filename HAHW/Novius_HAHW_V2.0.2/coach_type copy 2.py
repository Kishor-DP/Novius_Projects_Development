from datetime import datetime, timedelta
import pyodbc
from json.decoder import JSONDecodeError
import json
import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.StreamHandler()
    ]
)

logger = logging.getLogger(__name__)

class TrainSpeedDistanceCalculator:
    def __init__(self, initial_distance=20.0):
        self.initial_distance = initial_distance
        self.conn_str = (
            "DRIVER={SQL Server};"
            "SERVER=4MVDUGL\\SQLEXPRESS;"
            "DATABASE=NVS_HAHW_V2;"
            "Trusted_Connection=yes;"
        )
        self.current_train_id = None
        self.train_start_value = None
        self.coach_type = None

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
                    self.train_start_value = TrainStart_data.get("TrainStart", False)
                    return self.train_start_value
            except FileNotFoundError:
                logger.warning(f"File not found. Retrying in {retry_interval} seconds...")
            except JSONDecodeError:
                logger.warning(f"Invalid JSON data. Retrying in {retry_interval} seconds...")
            time.sleep(retry_interval)
            retries += 1
        return False

    def convert_to_datetime(self, timestamp):
        try:
            parts = timestamp.strip().split()
            if len(parts) < 5:
                print(f"Invalid timestamp format: {timestamp}")
                return None

            hours = int(parts[1])
            minutes = int(parts[2])
            seconds = int(parts[3])
            nanoseconds = int(parts[4])

            reference_date = datetime(2000, 1, 1)
            converted_date = reference_date + timedelta(
                hours=hours, minutes=minutes, seconds=seconds, microseconds=nanoseconds // 1000
            )
            return converted_date
        except (ValueError, IndexError) as e:
            print(f"Error converting timestamp: {timestamp}. Exception: {e}")
            return None
        
    def insert_into_tblSpeedDistance(self, TrainId,speed_result,c1_timestamp,s1_timestamp,coach_type):
        with pyodbc.connect(self.conn_str) as conn:
            cursor = conn.cursor()
            query = "INSERT INTO [dbo].[tblSpeedDistance] ([TrainId],[speed_result],[C1_Timestamp],[S1_Timestamp],[coach_type]) VALUES (?,?,?,?,?)"
            cursor.execute(query, TrainId,speed_result,c1_timestamp,s1_timestamp,coach_type)
            conn.commit()

    def update_coach_type(self, TrainId, coach_type):
        with pyodbc.connect(self.conn_str) as conn:
            cursor = conn.cursor()
            query = """
                UPDATE [dbo].[tblSpeedDistance]
                SET [coach_type] = ?
                WHERE [TrainId] = ?;
            """
            cursor.execute(query, coach_type, TrainId)
            conn.commit()
            logger.info(f"Updated coach_type to {coach_type} for TrainId {TrainId}")

    def calculate_speed_and_distance(self):
        try:
            self.current_train_id = self.read_TrainId_Fromjson()
            if not self.current_train_id:
                logger.warning("No TrainId found. Exiting.")
                return

            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                TrainId = self.current_train_id

                cursor.execute("""
                    SELECT
                        p2.[Axle_No],
                        p2.[Timestamp],
                        p3.[S1_Timestamp]
                    FROM 
                        (SELECT *, ROW_NUMBER() OVER (ORDER BY [Timestamp]) AS rn FROM [NVS_HAHW_V2].[dbo].[Temperature] WHERE TrainId = ?) p2
                    JOIN 
                        (SELECT *, ROW_NUMBER() OVER (ORDER BY [S1_Timestamp]) AS rn FROM [NVS_HAHW_V2].[dbo].[Proxy_s1] WHERE TrainId = ?) p3
                    ON p2.rn = p3.rn
                    ORDER BY p2.[Timestamp]
                """, TrainId, TrainId)

                rows = cursor.fetchall()
                print(f"Number of rows fetched: {len(rows)}")
                coach_type = None
                speeds = []
                distances = []

                for row in rows:
                    c1_value = row[0]
                    c1_timestamp = row[1]
                    s1_timestamp = row[2]

                    timestamp_c1 = self.convert_to_datetime(c1_timestamp)
                    timestamp_s1 = self.convert_to_datetime(s1_timestamp)

                    if timestamp_c1 is not None and timestamp_s1 is not None:
                        time_diff = abs((timestamp_s1 - timestamp_c1).total_seconds())

                        if time_diff > 0:
                            speed_mps = self.initial_distance / time_diff
                            speed_kmph = speed_mps * 3.6
                        else:
                            speed_kmph = 0

                        speeds.append((timestamp_c1, speed_kmph))
                        print(f"Speed for Axle {c1_value}: {speed_kmph:.2f} km/h")
                        speed_result = f"Speed for Axle {c1_value}: {speed_kmph:.2f} km/h"
                        self.insert_into_tblSpeedDistance(TrainId,speed_result,c1_timestamp,s1_timestamp,self.coach_type)
                    else:
                        print(f"Timestamp conversion failed for C1 value {c1_value}")

                    print(f"C1_Timestamp: {c1_timestamp}")
                    print(f"S1_Timestamp: {s1_timestamp}")
                    
                for i in range(len(speeds) - 1):
                    timestamp1, speed_kmph1 = speeds[i]
                    timestamp2, speed_kmph2 = speeds[i + 1]

                    time_diff = abs((timestamp2 - timestamp1).total_seconds())
                    distance = speed_kmph1 / 3.6 * time_diff
                    distances.append(distance)
                    print(f"Distance between Axle {i+1} and Axle {i+2}: {distance:.2f} meters")

                if len(distances) >= 2:
                    distance_1_2 = distances[0]
                    distance_2_3 = distances[1]

                    if abs(distance_1_2 - distance_2_3) < 0.01:
                        print("The type is LOCO")
                    else:
                        print("The type is Coach")
                        
                        if abs(distance_1_2 - 2896) < 0.01:
                            self.coach_type = "ICF"
                        elif abs(distance_1_2 - 2560) < 0.01:
                            self.coach_type = "LHB"
                        elif abs(distance_1_2 - 2000) < 0.01:
                            self.coach_type = "WAGON"

                        if self.coach_type:
                            print(f"The Coach type is {self.coach_type}")
                        else:
                            print("OTHER STOCK")
                            self.coach_type = 'OTHER STOCK'
                    # Update the coach type in the database
                    self.update_coach_type(TrainId, self.coach_type)
                else:
                    print("Not enough distances to compare.")

        except Exception as e:
            print(f"Database error: {e}")

    

    def process_data_based_on_train_start(self, check_interval=10):
        processing_needed = False

        while True:
            self.train_start_value = self.read_TrainStart_Fromjson()
            
            if self.train_start_value:
                if processing_needed:
                    print("TrainStart is False. Waiting...")
                    processing_needed = False
            else:
                if not processing_needed:
                    print("TrainStart is True. Processing data...")
                    self.calculate_speed_and_distance()
                    
                    processing_needed = True
                
            
            # Wait before the next check
            time.sleep(check_interval)
if __name__ == "__main__":
    calculator = TrainSpeedDistanceCalculator()
    calculator.process_data_based_on_train_start()
