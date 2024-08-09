import sqlite3
import json
from datetime import datetime


with open('PLC.json') as f:
    dbpath = json.load(f)


def insert_event(C1, Axle_No):
    # Ensure the SQL statement has the correct number of placeholders
    sql = "INSERT INTO PLC_DATA (C1, Axle_No) VALUES (?, ?)"
    conn = sqlite3.connect(dbpath["DBpath"])
    cursor = conn.cursor()
    try:
        # Execute the SQL statement with the correct number of parameters
        cursor.execute(sql, (C1, Axle_No))
        conn.commit()
    except sqlite3.Error as e:
        print(f"Database error: {e}")
    finally:
        cursor.close()
        conn.close()


# #def insert_event(Code, CoachId, CoachNo, Train_Time_Stamp, Coach_Time_Stamp, CoachNoOCR):
# def insert_event(CoachNo):
#     # Connect to the SQLite database (or create a new one if it doesn't exist)
#     conn = sqlite3.connect(dbpath["DBpath"])

#     # Create a cursor object to execute SQL statements
#     cursor = conn.cursor()
    
#     # Generate a short UUID for CoachId
#     #CoachId = generate_short_uuid()
    
#     # Insert a record with specific column values
    
#     insert_query = '''
#         INSERT INTO info (CoachNoOCR)
#         VALUES (?)
#     '''

#     # Values to insert
#     #record_values = (Code, CoachId, CoachNo, Train_Time_Stamp, Coach_Time_Stamp)
#     record_values = (CoachNoOCR)

#     # Execute the INSERT query
#     cursor.execute(insert_query, record_values)

#     # Commit the changes and close the connection
#     conn.commit()
#     conn.close()

#insert_query = '''
        #INSERT INTO info (Code, CoachId, CoachNo, Train_Time_Stamp, Coach_Time_Stamp)
        #VALUES (?, ?, ?, ?, ?, ?)
    #'''
