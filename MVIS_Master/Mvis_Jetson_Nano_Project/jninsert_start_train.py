#jninsert.py
import json
import pymssql
from datetime import datetime
def read_config():
    with open('config.json', 'r') as config_file:
        return json.load(config_file)

def establish_connection(config):
    try:
        conn = pymssql.connect(**config)
        print("Connection successful!")
        return conn
    except pymssql.Error as e:
        print("Error while connecting to database:", e)
        return None

def insert_into_start_train(conn,Code):
    try:
        
        # Execute INSERT statement
        cursor = conn.cursor()
        insert_query = '''
            INSERT INTO Gridviewtbl (Time_Stamp_Gridviewtbl,Code)
            VALUES (%s,%s)
        '''
        record_values = (datetime.now().strftime('%Y-%m-%d %H:%M:%S'),Code)
        print("Number of placeholders:", insert_query.count("%s"))
        print("Number of values:", len(record_values))
        cursor.execute(insert_query, record_values)
        

        conn.commit()
        print("Data inserted successfully.")
    except Exception as e:
        print("Error inserting data:", e)

def main():
    config = read_config()
    conn = establish_connection(config)
    # Insert data into mvisuser table
    #insert_into_start_train(conn, "test1")
    # Close the connection
    conn.close()

if __name__ == "__main__":
    main()
