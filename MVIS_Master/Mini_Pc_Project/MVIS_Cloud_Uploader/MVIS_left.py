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
    # Fetch data from the database (tblTemperatureLog table) based on Code
    cursor = conn.cursor()
    select_query = '''
        SELECT Sr_No, Code, CoachId, Component, Parameter, Status, Time_stamp, Start_Time_stamp
        FROM [MVISCopy].[noviusr1_noviusr1].[MVIS_left]
        WHERE Code = ?
    '''
    cursor.execute(select_query, (train_id,))
    return cursor.fetchall()


def insert_into_tblTrainTransaction(conn, data, Code):
    cursor = conn.cursor()
    insert_query = '''
        INSERT INTO dbo.MVIS_left(Sr_No, Code, CoachId, Component, Parameter, Status, Time_stamp, Start_Time_stamp)
        VALUES (?,?,?,?,?,?,?,?)
    '''
    cursor.executemany(insert_query, data)
    conn.commit()
    print("Data inserted into tblTrainTransaction successfully for Code:", Code)

    return data  # Return the inserted data

def compare_and_sync_databases(config, train_id):
    # Establish connection to local and cloud databases
    conn_local = establish_connection(config, 'database')
    conn_cloud = establish_connection(config, 'cloud_database')

    # Fetch data for the specified train_id from the local database
    data_to_sync = fetch_data_by_train_id(conn_local, train_id)

    if data_to_sync:
        # Insert data into cloud database and capture the inserted data
        inserted_data = insert_into_tblTrainTransaction(conn_cloud, data_to_sync, train_id)  # Pass train_id here

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
    
    # Read Code from config1.json
    with open('config1.json') as f:
        config1 = json.load(f)
    
    train_id_from_trigger = config1["Code"]
    
    compare_and_sync_databases(config, train_id_from_trigger)


if __name__ == "__main__":
    main()


