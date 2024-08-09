# import pyodbc
# from datetime import datetime

# # Define the connection string using raw strings to avoid escape sequence warnings
# connection_string = (
#     r"DRIVER={SQL Server};"
#     r"SERVER=DESKTOP-FI2AEOT\SQLEXPRESS;"
#     r"DATABASE=PLC;"
#     r"Trusted_Connection=yes;"
# )

# # Establish a connection to the database
# conn = pyodbc.connect(connection_string)
# cursor = conn.cursor()

# # Define the insert query
# insert_query = """
# INSERT INTO Proxy
#        ([C1], [C2], [E1], [E2], [S1], [S2], [Axle_No], 
#         [C1_Timestamp], [C1_System_Timestamp], 
#         [C2_Timestamp], [C2_System_Timestamp], [S1_Timestamp], [S1_System_Timestamp], 
#         [S2_Timestamp], [S2_System_Timestamp], [E1_Timestamp], [E1_System_Timestamp], 
#         [E2_Timestamp], [E2_System_Timestamp])
# VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
# """

# # Example data to insert
# data_to_insert = (
#     'C1_value', 'C2_value', 'E1_value', 'E2_value', 'S1_value', 'S2_value', 'Axle_No_value',
#     'C1_Timestamp_value', datetime.now(),
#     'C2_Timestamp_value', datetime.now(), 'S1_Timestamp_value', datetime.now(),
#     'S2_Timestamp_value', datetime.now(), 'E1_Timestamp_value', datetime.now(),
#     'E2_Timestamp_value', datetime.now()
# )

# try:
#     # Execute the insert query
#     cursor.execute(insert_query, data_to_insert)

#     # Commit the transaction
#     conn.commit()

#     # Print success message
#     print("Data successfully inserted into the database.")
# except Exception as e:
#     # Print error message
#     print(f"An error occurred: {e}")
# finally:
#     # Close the connection
#     cursor.close()
#     conn.close()


# import pyodbc

# # Define the connection string using raw strings to avoid escape sequence warnings
# connection_string = (
#     r"DRIVER={SQL Server};"
#     r"SERVER=DESKTOP-FI2AEOT\SQLEXPRESS;"
#     r"DATABASE=PLC;"
#     r"Trusted_Connection=yes;"
# )

# # Establish a connection to the database
# conn = pyodbc.connect(connection_string)
# cursor = conn.cursor()

# # Define the update query to clear data from specific columns
# update_query = """
# UPDATE Proxy
# SET [C1] = NULL, [C2] = NULL, [E1] = NULL, [E2] = NULL, [S1] = NULL, [S2] = NULL,
#     [C1_Timestamp] = NULL, [C1_System_Timestamp] = NULL, 
#     [C2_Timestamp] = NULL, [C2_System_Timestamp] = NULL,
#     [S1_Timestamp] = NULL, [S1_System_Timestamp] = NULL,
#     [S2_Timestamp] = NULL, [S2_System_Timestamp] = NULL,
#     [E1_Timestamp] = NULL, [E1_System_Timestamp] = NULL,
#     [E2_Timestamp] = NULL, [E2_System_Timestamp] = NULL
# """

# try:
#     # Execute the update query
#     cursor.execute(update_query)

#     # Commit the transaction
#     conn.commit()

#     # Print success message
#     print("Data successfully cleared from the specified columns.")
# except Exception as e:
#     # Print error message
#     print(f"An error occurred: {e}")
# finally:
#     # Close the connection
#     cursor.close()
#     conn.close()


import pyodbc

# Define the connection string using raw strings to avoid escape sequence warnings
connection_string = (
    r"DRIVER={SQL Server};"
    r"SERVER=DESKTOP-FI2AEOT\SQLEXPRESS;"
    r"DATABASE=PLC;"
    r"Trusted_Connection=yes;"
)

# Establish a connection to the database
conn = pyodbc.connect(connection_string)
cursor = conn.cursor()

# Define the delete query to remove all rows
delete_query = "DELETE FROM Proxy"

try:
    # Execute the delete query
    cursor.execute(delete_query)

    # Commit the transaction
    conn.commit()

    # Print success message
    print("All rows successfully deleted from the table.")
except Exception as e:
    # Print error message
    print(f"An error occurred: {e}")
finally:
    # Close the connection
    cursor.close()
    conn.close()
