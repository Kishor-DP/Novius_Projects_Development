import pyodbc

connection_string = (
    r"DRIVER={SQL Server};"
    r"SERVER=4MVDUGL\SQLEXPRESS;"
    r"DATABASE=NVS_HAHW_V2;"
    r"Trusted_Connection=yes;"
)

try:
    # Establish the connection
    connection = pyodbc.connect(connection_string)
    print("Connection successful!")

    # Optionally, you can execute a simple query to further verify the connection
    cursor = connection.cursor()
    cursor.execute("SELECT @@VERSION;")
    row = cursor.fetchone()
    print(f"SQL Server Version: {row[0]}")

    # Close the connection
    cursor.close()
    connection.close()
except Exception as e:
    print(f"Error connecting to database: {e}")
