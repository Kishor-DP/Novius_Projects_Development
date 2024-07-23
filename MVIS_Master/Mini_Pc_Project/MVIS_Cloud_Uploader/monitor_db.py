import pyodbc
import time
import json
import subpro
def read_config():
    # Read database configuration from config.json
    with open('config.json') as f:
        config = json.load(f)
    return config

def read_last_checked_timestamp():
    try:
        with open('last_checked_timestamp.json') as f:
            data = json.load(f)
            return data['Sr_No']
    except FileNotFoundError:
        # File not found, return a very old timestamp
        return 231449

def write_last_checked_timestamp(last_checked_timestamp):
    with open('last_checked_timestamp.json', 'w') as f:
        json.dump({"Sr_No": last_checked_timestamp}, f)
    with open('config1.json', 'w') as f:
        json.dump({"Sr_No": last_checked_timestamp}, f)

def get_connection(db_config):
    # Establish the database connection
    connection_string = (
        f"Driver={db_config['driver']};"
        f"Server={db_config['server']};"
        f"Database={db_config['database_name']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']};"
    )
    return pyodbc.connect(connection_string)

def get_latest_inserts(cursor, last_checked_timestamp):
    cursor.execute("SELECT * FROM [MVISCopy].[dbo].[Gridviewtbl] WHERE Sr_No > ?", (last_checked_timestamp,))
    return cursor.fetchall()

def process_new_inserts(new_rows):
    for row in new_rows:
        print(f"New row inserted: {row}")
        subpro.openpyfile()

def monitor_table():
    last_checked_timestamp = read_last_checked_timestamp()  # Initialize with the value from the JSON file
    config = read_config()
    db_config = config['database']  # Use the 'database' key
    connection = get_connection(db_config)
    cursor = connection.cursor()

    try:
        while True:
            new_rows = get_latest_inserts(cursor, last_checked_timestamp)
            if new_rows:
                process_new_inserts(new_rows)
                last_checked_timestamp = new_rows[-1].Sr_No  # Update the last checked timestamp
                write_last_checked_timestamp(last_checked_timestamp)  # Write the updated timestamp to the JSON file

            time.sleep(10)  # Check for new rows every 10 seconds
    except KeyboardInterrupt:
        print("Monitoring stopped.")
    finally:
        cursor.close()
        connection.close()

if __name__ == "__main__":
    monitor_table()
