from opcua import Client

# OPC UA server address
url = "opc.tcp://127.0.0.1:4841/freeopcua/server/"

# Initialize the OPC UA client
client = Client(url)

try:
    # Connect to the server
    client.connect()

    # Print namespaces to verify
    namespaces = client.get_namespace_array()
    print("Namespaces:", namespaces)

    # Get the root node and then the objects node
    root = client.get_root_node()
    print("Root children are:", root.get_children())

    objects = client.get_objects_node()
    print("Objects node:", objects)

    # Access the "SimulatedData" object using its node ID
    simulated_data_node = objects.get_child(["2:SimulatedData"])

    # Read and print the values of the tags for each equipment
    for i in range(1, 6):
        try:
            equipment_node = simulated_data_node.get_child([f"2:Equipment_{i}"])
            print(f"Equipment_{i}:")
            
            for tag_name in ["Temperature", "Pressure", "Torque", "Humidity", "Light", "Voltage", "Watts"]:
                tag_node = equipment_node.get_child([f"2:{tag_name}"])
                print(f"  {tag_name}: {tag_node.get_value()}")
                
        except Exception as e:
            print(f"Failed to access Equipment_{i}: {e}")

finally:
    # Disconnect from the server
    client.disconnect()
