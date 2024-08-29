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
        rx_info_list = status_data.get("rxInfo", [])
        tx_info = status_data.get("txInfo", {})

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

        # Print rxInfo details
        if rx_info_list:
            print("RxInfo Details:")
            for rx_info in rx_info_list:
                print(f"  Gateway ID: {rx_info.get('gatewayId')}")
                print(f"  Uplink ID: {rx_info.get('uplinkId')}")
                print(f"  GW Time: {rx_info.get('gwTime')}")
                print(f"  NS Time: {rx_info.get('nsTime')}")
                print(f"  RSSI: {rx_info.get('rssi')}")
                print(f"  SNR: {rx_info.get('snr')}")
                print(f"  Channel: {rx_info.get('channel')}")
                print(f"  Location: {rx_info.get('location', {})}")
                print(f"  CRC Status: {rx_info.get('crcStatus')}")
        else:
            print("No RxInfo available.")

        # Print txInfo details
        frequency = tx_info.get("frequency")
        modulation = tx_info.get("modulation", {})
        lora_modulation = modulation.get("lora", {})
        bandwidth = lora_modulation.get("bandwidth")
        spreading_factor = lora_modulation.get("spreadingFactor")
        code_rate = lora_modulation.get("codeRate")

        print("TxInfo Details:")
        print(f"  Frequency: {frequency}")
        print(f"  Modulation:")
        print(f"    Bandwidth: {bandwidth}")
        print(f"    Spreading Factor: {spreading_factor}")
        print(f"    Code Rate: {code_rate}")

if __name__ == "__main__":
    read_status_json('status.json')
