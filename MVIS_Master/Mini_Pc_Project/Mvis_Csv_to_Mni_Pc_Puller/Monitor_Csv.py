import pandas as pd
import json
import time
import os
from datetime import datetime
import subpro
from functools import wraps
import subpro

class CodeFetcher:
    def __init__(self, csv_file_path, json_file_path):
        self.csv_file_path = csv_file_path
        self.json_file_path = json_file_path
        self.last_row_count = self.get_row_count()
        self.last_mod_time = self.get_last_mod_time()

    def retry(exceptions, tries=60, delay=1, backoff=2):
        def decorator_retry(func):
            @wraps(func)
            def wrapper_retry(*args, **kwargs):
                _tries, _delay = tries, delay
                while _tries > 1:
                    try:
                        return func(*args, **kwargs)
                    except exceptions as e:
                        print(f"Retrying func1 in {_delay} seconds... ({_tries-1} tries left)")
                        time.sleep(_delay)
                        _tries -= 1
                        #_delay *= backoff
                return func(*args, **kwargs)
            return wrapper_retry
        return decorator_retry

    def read_config():
        # Read database configuration from config.json
        with open('config.json') as f:
            config = json.load(f)
        return config
    
    @retry(Exception, tries=31536063734300000, delay=1, backoff=3)
    def get_row_count(self):
        # Force re-reading of the file from disk
        try:
            df = pd.read_csv(self.csv_file_path)
            return len(df)
        except pd.errors.EmptyDataError:
            return 0
    #@retry(Exception, tries=50, delay=2, backoff=3)
    def get_last_mod_time(self):
        return os.path.getmtime(self.csv_file_path)
    
    #@retry(Exception, tries=50, delay=2, backoff=3)
    def fetch_last_code(self):
        try:
            # Read the CSV file
            df = pd.read_csv(self.csv_file_path)

            # Get the last row of the 'Code' column
            last_code = df['Code'].iloc[-1]

            # Prepare the data to be saved into JSON
            data = {"last_code": last_code}
            print(last_code)
            # Write the data to a JSON file
            with open(self.json_file_path, 'w') as json_file:
                json.dump(data, json_file, indent=4)

            print(f"Last code saved to {self.json_file_path}")
        except pd.errors.EmptyDataError:
            print("CSV file is empty.")
        except KeyError:
            print("'Code' column not found in the CSV file.")
        except Exception as e:
            print(f"An error occurred: {e}")

    
    def observe_new_row(self, interval=1):
        try:
            while True:
                current_mod_time = self.get_last_mod_time()
                if current_mod_time != self.last_mod_time:
                    self.last_mod_time = current_mod_time
                    current_row_count = self.get_row_count()
                    if current_row_count > self.last_row_count:
                        readable_time = self.convert_mod_time(current_mod_time)
                        print(f"New row detected. Previous row count: {self.last_row_count}, Current row count: {current_row_count}, Modification time: {readable_time}")
                        self.last_row_count = current_row_count
                        self.fetch_last_code()
                        subpro.openpyfile() # Adjust to the correct command
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Observation stopped.")

    #@retry(Exception, tries=50, delay=2, backoff=3)
    def convert_mod_time(self, mod_time):
        return datetime.fromtimestamp(mod_time).strftime('%Y-%m-%d %H:%M:%S')

    def cleanup(self):
        # This is where you would close any connections or perform any cleanup necessary.
        # Currently, there's nothing to clean up, but this is a placeholder for future needs.
        print("Cleanup operations completed.")
    

def retry(exceptions, tries=31536063734300000, delay=1, backoff=2):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Retrying func2 in {_delay} seconds... ({_tries-1} tries left) due to {e}")
                    time.sleep(_delay)
                    _tries -= 1
                    #_delay *= backoff
            return func(*args, **kwargs)
        return wrapper_retry
    return decorator_retry

# Example usage
Csv_filepath=CodeFetcher.read_config()
csv=Csv_filepath['Csv_filename']['Csv_Gridviewtbl']
print(csv)
csv_file_path = csv
#r'\\192.168.1.253\Documents\Gridviewtbl.csv'  # Replace with your CSV file path
json_file_path = 'last_code.json'  # Replace with your desired JSON file path

code_fetcher = CodeFetcher(csv_file_path, json_file_path)
#1month retry until end of world=31536063734300000
@retry(Exception, tries=31536063734300000, delay=1, backoff=0)
def main():
    code_fetcher.fetch_last_code()
    code_fetcher.observe_new_row()

try:
    main()
except Exception as e:
    print(f"An error occurred during observation: {e}")
finally:
    code_fetcher.cleanup()