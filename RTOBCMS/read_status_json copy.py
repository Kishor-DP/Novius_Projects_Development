import json

def read_status_json(file_path):
    with open(file_path, 'r') as file:
        # Load the JSON data from the file
        data = json.load(file)

        # Extract fields from the JSON data
        gateway_id = data.get("gateway_id")
        sensor_id = data.get("sensor_id")
        location = data.get("location")
        status_json_str = data.get("status")
        timestamp = data.get("timestamp")

        # Parse the nested JSON string in the 'status' field
        try:
            status_data = json.loads(status_json_str)
        except json.JSONDecodeError as e:
            print(f"Error decoding status JSON: {e}")
            status_data = {}

        # Extract fields from the nested JSON data
        deduplication_id = status_data.get("deduplicationId")
        time = status_data.get("time")
        device_info = status_data.get("deviceInfo", {})
        device_name = device_info.get("deviceName")
        data_content = status_data.get("data")
        object_data = status_data.get("object", {})
        mydata = object_data.get("mydata")
    
        # Print extracted information
        print(f"Gateway ID: {gateway_id}")
        print(f"Sensor ID: {sensor_id}")
        print(f"Location: {location}")
        print(f"Timestamp: {timestamp}")
        print(f"Deduplication ID: {deduplication_id}")
        print(f"Time: {time}")
        print(f"Device Name: {device_name}")
        print(f"Data Content: {data_content}")
        print(f"Object 'mydata': {mydata}")

if __name__ == "__main__":
    read_status_json('status.json')
