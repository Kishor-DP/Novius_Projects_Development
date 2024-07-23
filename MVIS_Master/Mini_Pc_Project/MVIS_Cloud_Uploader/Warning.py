import json
import pyodbc

def read_config():
    # Read database configuration from config.json
    with open('config.json') as f:
        config = json.load(f)
    return config

def establish_connection(config, database_type):
    # Establish the database connection
    db_config = config[database_type]
    conn_str = (
        f"Driver={db_config['driver']};"
        f"Server={db_config['server']};"
        f"Database={db_config['database_name']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']};"
    )
    return pyodbc.connect(conn_str)

def fetch_data_by_train_id(conn, train_id):
    # Fetch data from the database (tblTemperatureLog table) based on IntTrainId
    cursor = conn.cursor()
    select_query = '''
        SELECT intWarningId, intTrainId, intTempLogId, intAlarm_WarningID, intAxelNo, NvcharCoachNo, IntCoachPosition, NvcharSide, decTemperature, ynAcknowledged, nvcharFindings, nvcharActionTaken, nvcharDescription, dtDateofCreation, dtDateofModification,ynDeleted
        FROM tblWarning
        WHERE intTrainId = ?
    '''
    cursor.execute(select_query, (train_id,))
    return cursor.fetchall()


def insert_into_cloud_temp_log(conn, data):
    # Insert fetched data into the cloud database (tblTemperatureLog table)
    cursor = conn.cursor()
    insert_query = '''
        INSERT INTO tblWarning(intWarningId, intTrainId, intTempLogId, intAlarm_WarningID, intAxelNo, NvcharCoachNo, IntCoachPosition, NvcharSide, decTemperature, ynAcknowledged, nvcharFindings, nvcharActionTaken, nvcharDescription, dtDateofCreation, dtDateofModification, ynDeleted)
        VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
    '''
    cursor.executemany(insert_query, data)
    conn.commit()
    print("Data inserted into cloud database successfully.")

    return data  # Return the inserted data

def compare_and_sync_databases(config, train_id):
    # Establish connection to local and cloud databases
    conn_local = establish_connection(config, 'database')
    conn_cloud = establish_connection(config, 'cloud_database')

    # Fetch data for the specified train_id from the local database
    data_to_sync = fetch_data_by_train_id(conn_local, train_id)

    if data_to_sync:
        # Insert data into cloud database and capture the inserted data
        inserted_data = insert_into_cloud_temp_log(conn_cloud, data_to_sync)

        # Print info about inserted data
        print(f"Inserted data into cloud database for train_id: {train_id}:")
        for entry in inserted_data:
            print(entry)
    else:
        print(f"No data found in the local database for train_id: {train_id}")

    # Close connections
    conn_local.close()
    conn_cloud.close()

def main():
    config = read_config()
    
    # Read intTrainId from config1.json
    with open('config1.json') as f:
        config1 = json.load(f)
    
    train_id_from_trigger = config1["intTrainId"]
    
    compare_and_sync_databases(config, train_id_from_trigger)


if __name__ == "__main__":
    main()


