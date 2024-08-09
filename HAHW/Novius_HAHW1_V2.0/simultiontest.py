from opcua import Client
from opcua.ua.uaerrors import UaStatusCodeError

# OPC UA server address
url = "opc.tcp://127.0.0.1:4841/freeopcua/server/"

# Connect to the server
client = Client(url)

try:
    # Connect to the server
    client.connect()

    # Define the correct namespace index (from the server output)
    namespace_index = 2

    # Read and print values from all 203 temperature nodes
    temperature_values = {}
    for i in range(3, 206):  # Node IDs from 3 to 205
        node_id = f"ns={namespace_index};i={i}"
        try:
            node = client.get_node(node_id)
            value = node.get_value()
            temperature_values[i] = value
            print(f"Node ID: {node_id}, Value: {value}")
        except UaStatusCodeError as e:
            print(f"Error accessing node {node_id}: {e}")

finally:
    # Disconnect from the server
    client.disconnect()
