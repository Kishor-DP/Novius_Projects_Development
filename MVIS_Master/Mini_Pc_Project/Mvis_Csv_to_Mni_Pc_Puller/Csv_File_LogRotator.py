import os
import json
import pandas as pd
from datetime import datetime

class CSVLogRotator:
    def __init__(self, file_paths, row_limit=10000):
        self.file_paths = file_paths
        self.row_limit = row_limit
    
    def rotate_log(self):
        for file_path in self.file_paths:
            # Check if the file exists
            if not os.path.exists(file_path):
                print(f"The file {file_path} does not exist.")
                continue

            # Read the CSV file and count the rows
            df = pd.read_csv(file_path)
            row_count = len(df)
            print(f"{file_path} contains {row_count} rows.")

            # If row count exceeds the limit, rotate the file
            if row_count >= self.row_limit:
                # Generate the new file name with a timestamp
                timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
                new_file_name = f"{os.path.splitext(file_path)[0]}_{timestamp}.csv"
                
                # Rename the file
                os.rename(file_path, new_file_name)
                print(f"Rotated log file {file_path} to {new_file_name}")

    @staticmethod
    def load_config(config_path):
        with open(config_path, 'r') as config_file:
            config = json.load(config_file)
        return config

    @staticmethod
    def Csv_File_LogRotator_Main():
        # Load the configuration
        config = CSVLogRotator.load_config('config.json')

        # Extract CSV file paths
        csv_files = list(config["Csv_filename"].values())
        
        # Create and run the log rotator
        log_rotator = CSVLogRotator(csv_files)
        log_rotator.rotate_log()

if __name__ == "__main__":
    CSVLogRotator.Csv_File_LogRotator_Main()
