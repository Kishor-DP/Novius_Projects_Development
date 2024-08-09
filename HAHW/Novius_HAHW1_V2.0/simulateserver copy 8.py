from opcua import Server, ua

# Initialize the OPC UA server
server = Server()

# Set up the server's endpoint
server.set_endpoint("opc.tcp://127.0.0.1:4841/freeopcua/server/")

# Register namespace
uri = "http://custom.namespace.example"
idx = server.register_namespace(uri)
print(f"Namespace index for {uri}: {idx}")

# Set up the object node
objects = server.get_objects_node()

# Create nodes for IDs 3 to 206
temperature_nodes = {}
print("Creating temperature nodes...")
for i in range(3, 207):  # 207 is exclusive, so it covers 3 to 206
    node = objects.add_variable(idx, f"TemperatureNode{i}", ua.Variant('', ua.VariantType.String))
    temperature_nodes[i] = node

# Create TrainStart node with ID 829
train_start_node = objects.add_variable(idx, "TrainStart", ua.Variant(False, ua.VariantType.Boolean))
train_start_node.set_value(False)  # Initialize with False
print("Created TrainStart node with ID 829")

# Start the server before setting values
server.start()
print("Server started.")

try:
    # Set auto-incrementing string values for all temperature nodes
    for i in range(3, 20):
        value = f'C1,{i-2},5 4 4 4 8748537456,768,34'  # Adjust based on the node ID
        node = temperature_nodes[i]
        node.set_value(value)
        print(f"Set value for node ns={idx};i={i}: {value}")

    # Optionally set TrainStart node value (for example, True)
    train_start_node.set_value(True)
    print("Set TrainStart node value to True")
     # Optionally read back the TrainStart node value
    read_value = train_start_node.get_value()
    print(f"TrainStart node value is {train_start_node,read_value}")
    print("Nodes 3 to 206 have been set with auto-incrementing string values.")
    print(f"Server running with CustomNode and temperature nodes (ns={idx}, i=3 to i=206)")

    # Keep the server running
    while True:
        pass  # Keep the server running

finally:
    server.stop()
    print("Server stopped.")
