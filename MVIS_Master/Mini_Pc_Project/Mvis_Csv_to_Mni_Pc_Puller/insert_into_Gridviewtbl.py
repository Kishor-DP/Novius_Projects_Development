import json
import pyodbc
import pandas as pd
import time
def read_config():
    # Read database configuration from config.json
    with open('config.json') as f:
        config = json.load(f)
    return config

def establish_connection(config, database_type):
    db_config = config[database_type]
    # Establish the database connection
    if db_config['driver'] == '{SQL Server}':
        return pyodbc.connect(
            f"DRIVER={{SQL Server}};SERVER={db_config['server']};DATABASE={db_config['database_name']};UID={db_config['username']};PWD={db_config['password']}"
        )
    else:
        raise ValueError("Unsupported database driver: " + db_config['driver'])

def fetch_data_by_train_id_from_csv(train_id, csv_file):
    # Fetch data from the CSV file based on IntTrainId
    df = pd.read_csv(csv_file)
    
    # Print the content of the CSV file for debugging
    print("Content of the CSV file:")
    print(df.head())
    
    # Check and print data types of the CSV file columns
    print("Data types of the CSV file columns:")
    print(df.dtypes)
    
    # Ensure train_id and Code column are the same data type
    train_id = str(train_id)  # Convert train_id to string if Code is a string
    
    # Print the train_id for debugging
    print(f"Filtering for train_id: {train_id}")
    
    filtered_data = df[df['Code'] == train_id][['Code', 'Time_Stamp_Gridviewtbl']]
    
    # Print the filtered data for debugging
    print("Filtered data:")
    print(filtered_data)
    
    return filtered_data.values.tolist()
    
    #return filtered_data.values.tolist()

def insert_into_cloud_temp_log(conn, data):
    # Insert fetched data into the cloud database (tblTemperatureLog table)
    cursor = conn.cursor()
    insert_query = '''
        INSERT INTO  [MVIS].[dbo].[Gridviewtbl](Code, Time_Stamp_Gridviewtbl)
        VALUES (?, ?)
    '''
    cursor.executemany(insert_query, data)
    conn.commit()
    print("Data inserted into Mini_Pc Gridviewtbl successfully.")

    return data  # Return the inserted data

def compare_and_sync_databases(config, train_id):
    csv_file =config['Csv_filename']['Csv_Gridviewtbl']
    print(csv_file)
    # Establish connection to cloud database
    conn_cloud = establish_connection(config, 'cloud_database')
    
    # Fetch data for the specified train_id from the CSV file
    data_to_sync = fetch_data_by_train_id_from_csv(train_id,csv_file)
    print(data_to_sync)
    if data_to_sync:
        # Insert data into cloud database and capture the inserted data
        inserted_data = insert_into_cloud_temp_log(conn_cloud, data_to_sync)

        # Print info about inserted data
        print(f"Inserted data into Mini PC database for train_id: {train_id}:")
        for entry in inserted_data:
            print(entry)
    else:
        print(f"No data found in the CSV file for train_id: {train_id}")

    # Close connection
    conn_cloud.close()

def main():
    config = read_config()
    
    # Read intTrainId from config1.json
    with open('last_code.json') as f:
        config1 = json.load(f)
    
    train_id_from_trigger = config1["last_code"]  # Fetch data_by_train_id from CSV file based on json key
    
    compare_and_sync_databases(config, train_id_from_trigger)

if __name__ == "__main__":
    #while True:
        
    main()
     #   time.sleep(10)
