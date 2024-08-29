import json
import pyodbc
from datetime import datetime

def read_status_json(file_path):
    with open(file_path, 'r') as file:
        data = json.load(file)

        status_json_str = data.get("status")

        try:
            status_data = json.loads(status_json_str)
        except json.JSONDecodeError as e:
            print(f"Error decoding status JSON: {e}")
            status_data = {}

        deduplication_id = status_data.get("deduplicationId")
        time = status_data.get("time")
        device_info = status_data.get("deviceInfo", {})
        device_name = device_info.get("deviceName")
        data_content = status_data.get("data")
        object_data = status_data.get("object", {}).get("mydata")
        rx_info_list = status_data.get("rxInfo", [])

        return {
            'gateway_id': data.get("gateway_id"),
            'sensor_id': data.get("sensor_id"),
            'location': data.get("location"),
            'timestamp': data.get("timestamp"),
            'deduplication_id': deduplication_id,
            'time': time,
            'device_name': device_name,
            'data_content': data_content,
            'object_data': object_data,
            'rx_info_list': rx_info_list
        }

def insert_into_Device(connection_str, data):
    try:
        # Establish the connection to the SQL Server
        with pyodbc.connect(connection_str) as conn:
            cursor = conn.cursor()

            # Define the SQL INSERT statement
            sql = """
                INSERT INTO Device (modifiedBy, Devicename, Deviceinstalllocation, createdDate, Deviceip, createdBy, Deviceinputdetails, Deviceoutputdetails, Deviceuser)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            # Convert parameters
            params = (
                data['gateway_id'],
                data['sensor_id'],
                data['location'],
                datetime.fromisoformat(data['timestamp']),
                data['deduplication_id'],
                datetime.fromisoformat(data['time']),
                data['device_name'],
                data['data_content'],
                data['object_data']
            )

            # Execute the SQL statement
            cursor.execute(sql, params)

            # Commit the transaction
            conn.commit()
            print("Data inserted successfully.")
    except pyodbc.Error as e:
        print("Error occurred while inserting into rx_info_list:", e)
def insert_into_rx_info_list(connection_str, rx_info_list):
    try:
        with pyodbc.connect(connection_str) as conn:
            cursor = conn.cursor()

            sql = """
                INSERT INTO rx_info_list (GatewayID, uplinkId, gwTime, nsTime, rssi, snr, channel, location, crcStatus)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """

            for rx_info in rx_info_list:
                params = (
                    rx_info.get('gatewayId'),
                    rx_info.get('uplinkId'),
                    rx_info.get('gwTime'),
                    rx_info.get('nsTime'),
                    rx_info.get('rssi'),
                    rx_info.get('snr'),
                    rx_info.get('channel'),
                    json.dumps(rx_info.get('location')),  # Assuming location is a nested object
                    rx_info.get('crcStatus')
                )

                cursor.execute(sql, params)

            conn.commit()
            print("Data inserted successfully into rx_info_list table.")
    except pyodbc.Error as e:
        print("Error occurred while inserting into rx_info_list:", e)
    
# Example usage 
if __name__ == "__main__":
    file_path = 'status.json'
    connection_str = 'DRIVER={SQL Server};SERVER=4MVDUGL\\KISHOR;DATABASE=1439;Trusted_Connection=yes;'
    
    status_data = read_status_json(file_path)
    insert_into_Device(connection_str, status_data)
    
    if status_data['rx_info_list']:
        insert_into_rx_info_list(connection_str, status_data['rx_info_list'])
