import pyodbc
import logging

class TemperatureDataProcessor:
    def __init__(self, connection_string):
        self.connection_string = connection_string
        self.conn = None
        self.cursor = None

    def connect(self):
        try:
            self.conn = pyodbc.connect(self.connection_string)
            self.cursor = self.conn.cursor()
        except Exception as e:
            logging.error(f"Database connection failed: {e}")

    def parse_custom_time(self, time_str):
        try:
            # Split the time string into components
            parts = time_str.split()
            day = int(parts[0])
            hour = int(parts[1])
            minute = int(parts[2])
            second = int(parts[3])
            millisecond = int(parts[4])

            # Return the components in a tuple
            return (day, hour, minute, second, millisecond)
        except Exception as e:
            logging.error(f"Error parsing time string '{time_str}': {e}")
            return None

    def calculate_time_difference(self, time1, time2):
        try:
            day1, hour1, minute1, second1, millisecond1 = time1
            day2, hour2, minute2, second2, millisecond2 = time2

            # Convert everything to milliseconds
            total_milliseconds1 = ((day1 * 24 * 3600 + hour1 * 3600 + minute1 * 60 + second1) * 1000) + millisecond1
            total_milliseconds2 = ((day2 * 24 * 3600 + hour2 * 3600 + minute2 * 60 + second2) * 1000) + millisecond2

            # Calculate the difference in milliseconds
            difference = abs(total_milliseconds2 - total_milliseconds1)

            logging.info(f"Total milliseconds1: {total_milliseconds1}, Total milliseconds2: {total_milliseconds2}")
            logging.info(f"Time difference in milliseconds: {difference}")

            return difference / 1000.0  # Return in seconds

        except Exception as e:
            logging.error(f"Error calculating time difference: {e}")
            return 0.0

    def fetch_proxy_s1_data(self, train_id):
        query = f"""
        SELECT [intDBAxleCount], [TrainId], [S1], [S1_Timestamp], [S1_System_Timestamp]
        FROM [NVS_HAHW_V2].[dbo].[Proxy_s1]
        WHERE [TrainId] = ?
        """
        self.cursor.execute(query, train_id)
        data = self.cursor.fetchall()

        # Clean up the data by stripping spaces and newlines
        cleaned_data = []
        for row in data:
            cleaned_row = (
                row[0],  # intDBAxleCount
                row[1].strip(),  # TrainId
                row[2].strip(),  # S1
                row[3].strip(),  # S1_Timestamp
                row[4].strip(),  # S1_System_Timestamp
            )
            cleaned_data.append(cleaned_row)
            #print(f"fetch_proxy_s1_data cleaned_data:{cleaned_data}")
        return cleaned_data

    def fetch_temperature_data(self, train_id):
        query = f"""
        SELECT [intDBAxleCount], [TrainId], [T1], [T2], [T3], [T4], [T5], [T6], [Timestamp], [Axle_No], [System_Timestamp]
        FROM [NVS_HAHW_V2].[dbo].[Temperature]
        WHERE [TrainId] = ?
        """
        self.cursor.execute(query, train_id)
        data = self.cursor.fetchall()

        # Clean up the data by stripping spaces and newlines
        cleaned_data = []
        for row in data:
            cleaned_row = (
                row[0],  # intDBAxleCount
                row[1].strip(),  # TrainId
                row[2],  # T1
                row[3],  # T2
                row[4],  # T3
                row[5],  # T4
                row[6],  # T5
                row[7],  # T6
                row[8].strip(),  # Timestamp
                row[9].strip(),  # Axle_No
                row[10].strip(),  # System_Timestamp
            )
            cleaned_data.append(cleaned_row)
            #print(f"fetch_temperature_data cleaned_data:{cleaned_data}")
        return cleaned_data

    def insert_into_tblSpeedDistance(self, speed_result):
        query = "INSERT INTO [dbo].[tblSpeedDistance] ([speed_result]) VALUES (?)"
        self.cursor.execute(query, speed_result)
        self.conn.commit()

    def process_and_insert_data(self, train_id):
        proxy_s1_data = self.fetch_proxy_s1_data(train_id)
        temperature_data = self.fetch_temperature_data(train_id)

        i, j = 0, 0
        distance = 10  # Distance in meters

        while i < len(proxy_s1_data) and j < len(temperature_data):
            s1_row = proxy_s1_data[i]
            temp_row = temperature_data[j]

            s1_time = self.parse_custom_time(s1_row[3])
            temp_time = self.parse_custom_time(temp_row[8])

            if s1_time and temp_time:
                logging.info(f"S1 Time: {s1_time}, Temp Time: {temp_time}")

                if s1_row[2] == temp_row[9]:  # Matching S1 and Axle_No
                    try:
                        # Calculate the time difference in seconds
                        time_difference = self.calculate_time_difference(s1_time, temp_time)
                        logging.info(f"Time Difference: {time_difference} seconds")

                        if time_difference > 0:  # Ensure that time difference is positive
                            # Calculate speed
                            speed = distance / time_difference  # Speed in meters per second
                            speed_result = f"{speed:.2f} m/s"
                            self.insert_into_tblSpeedDistance(speed_result)
                            logging.info(f"Inserted speed data: {speed_result}")
                        else:
                            logging.warning(f"Non-positive time difference: {time_difference} seconds")
                    except Exception as e:
                        logging.error(f"Error processing data: {e}")

                    # Move to the next row in both lists
                    i += 1
                    j += 1
                elif s1_row[2] < temp_row[9]:  # If S1 < Axle_No, move to the next S1 row
                    i += 1
                else:  # If Axle_No < S1, move to the next Temperature row
                    j += 1
            else:
                # Handle case where time parsing fails
                i += 1
                j += 1

    def close_connection(self):
        if self.conn:
            self.conn.close()

if __name__ == "__main__":
    connection_string = (
        r"DRIVER={SQL Server};"
        r"SERVER=4MVDUGL\SQLEXPRESS;"
        r"DATABASE=NVS_HAHW_V2;"
        r"Trusted_Connection=yes;"
    )

    processor = TemperatureDataProcessor(connection_string)
    processor.connect()
    processor.process_and_insert_data('2024_08_22_10_22_50_2000')
    processor.close_connection()
