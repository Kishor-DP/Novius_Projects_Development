from datetime import datetime, timedelta
import pyodbc
from json.decoder import JSONDecodeError  # Import JSONDecodeError
import json
import logging
import time

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,  # Set your application's logging level
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
            # Split the timestamp and ignore the date part
            parts = timestamp.strip().split()
            if len(parts) < 5:
                print(f"Invalid timestamp format: {timestamp}")
                return None

            # Extract relevant parts: hours, minutes, seconds, and nanoseconds
            hours = int(parts[1])
            minutes = int(parts[2])
            seconds = int(parts[3])
            nanoseconds = int(parts[4])

            # Assuming a reference date for conversion
            reference_date = datetime(2000, 1, 1)
            converted_date = reference_date + timedelta(
                hours=hours, minutes=minutes, seconds=seconds, microseconds=nanoseconds // 1000
            )
            return converted_date
        except (ValueError, IndexError) as e:
            print(f"Error converting timestamp: {timestamp}. Exception: {e}")
            return None

    def calculate_speed_and_distance(self):
        try:
            self.train_start_value=self.read_TrainStart_Fromjson()
            self.current_train_id = self.read_TrainId_Fromjson()
            TrainStart=self.train_start_value
            with pyodbc.connect(self.conn_str) as conn:
                cursor = conn.cursor()
                TrainId = self.current_train_id#'2024_08_16_16_58_18_2000'
                
                # Fetch data by joining the two tables based on row number
                cursor.execute("""
                    SELECT
                        p2.[Axle_No],
                        p2.[Timestamp],
                        p3.[S1_Timestamp]
                    FROM 
                        (SELECT *, ROW_NUMBER() OVER (ORDER BY [Timestamp]) AS rn FROM [NVS_HAHW_V2].[dbo].[Temperature]  WHERE TrainId = ?) p2
                    JOIN 
                        (SELECT *, ROW_NUMBER() OVER (ORDER BY [S1_Timestamp]) AS rn FROM [NVS_HAHW_V2].[dbo].[Proxy_s1]  WHERE TrainId = ?) p3
                    ON p2.rn = p3.rn
                    ORDER BY p2.[Timestamp]
                """, TrainId, TrainId)
                
                rows = cursor.fetchall()
                
                # Print the number of rows fetched for debugging
                print(f"Number of rows fetched: {len(rows)}")
                
                speeds = []
                distances = []
                
                for row in rows:
                    c1_value = row[0]
                    c1_timestamp = row[1]
                    s1_timestamp = row[2]
                    
                    # Convert timestamps to datetime objects
                    timestamp_c1 = self.convert_to_datetime(c1_timestamp)
                    timestamp_s1 = self.convert_to_datetime(s1_timestamp)
                    
                    if timestamp_c1 is not None and timestamp_s1 is not None:
                        # Calculate absolute time difference in seconds
                        time_diff = abs((timestamp_s1 - timestamp_c1).total_seconds())
                        
                        # Calculate speed (in m/s)
                        if time_diff > 0:
                            speed_mps = self.initial_distance / time_diff
                            # Convert speed to km/h
                            speed_kmph = speed_mps * 3.6
                        else:
                            speed_kmph = 0  # Set speed to 0 if time difference is zero or negative
                        
                        speeds.append((timestamp_c1, speed_kmph))
                        
                        print(f"Speed for Axle {c1_value}: {speed_kmph:.2f} km/h")
                    else:
                        print(f"Timestamp conversion failed for C1 value {c1_value}")

                    # Print the C1_Timestamp and S1_Timestamp for the row
                    print(f"C1_Timestamp: {c1_timestamp}")
                    print(f"S1_Timestamp: {s1_timestamp}")
                
                # Calculate distances between consecutive axles
                for i in range(len(speeds) - 1):
                    timestamp1, speed_kmph1 = speeds[i]
                    timestamp2, speed_kmph2 = speeds[i + 1]
                    
                    # Calculate time difference in seconds between consecutive C1_Timestamps
                    time_diff = abs((timestamp2 - timestamp1).total_seconds())
                    
                    # Calculate distance
                    distance = speed_kmph1 / 3.6 * time_diff  # Convert speed back to m/s for calculation
                    
                    distances.append(distance)
                    print(f"Distance between Axle {i+1} and Axle {i+2}: {distance:.2f} meters")
                
                # Check if distances between Axles 1-2 and 2-3 are the same
                if len(distances) >= 2:
                    distance_1_2 = distances[0]
                    distance_2_3 = distances[1]
                    
                    if abs(distance_1_2 - distance_2_3) < 0.01:  # Tolerance for comparison
                        print("The type is LOCO")
                    else:
                        print("The type is Coach")
                        
                        # Further classification of Coach type
                        coach_type = None
                        if abs(distance_1_2 - 2896) < 0.01:
                            coach_type = "ICF"
                        elif abs(distance_1_2 - 2560) < 0.01:
                            coach_type = "LHB"
                        elif abs(distance_1_2 - 2000) < 0.01:
                            coach_type = "WAGON"
                        
                        if coach_type:
                            print(f"The Coach type is {coach_type}")
                        else:
                            print("OTHER STOCK")
                else:
                    print("Not enough distances to compare.")
        
        except Exception as e:
            print(f"Database error: {e}")


if __name__ == "__main__":
    calculator = TrainSpeedDistanceCalculator()
    calculator.calculate_speed_and_distance()
