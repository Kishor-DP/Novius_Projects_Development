import json
from opcua import Server, ua

# Load configuration from JSON file
def load_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config

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

# Create nodes for IDs 3 to 206 and node 829 for TrainStart flag
temperature_nodes = {}
train_start_node = objects.add_variable(idx, "TrainStartFlag", ua.Variant(False, ua.VariantType.Boolean))

print("Creating temperature nodes...")
for i in range(3, 207):  # 207 is exclusive, so it covers 3 to 206
    node = objects.add_variable(idx, f"TemperatureNode{i}", ua.Variant('', ua.VariantType.String))
    temperature_nodes[i] = node

# Start the server before setting values
server.start()
print("Server started.")

try:
    # Load the configuration
    config = load_config('TrainStartFlag.json')
    
    # Set auto-incrementing string values for all nodes
    for i in range(3, 9):
        value = f'C1,{i-2},5 4 4 4 8748537456,768,34'  # Adjust based on the node ID
        node = temperature_nodes[i]
        node.set_value(value)
        print(f"Set value for node ns={idx};i={i}: {value}")

    # Set the TrainStart flag based on the configuration
    train_start_flag = config.get("TrainStartFlag", False)
    train_start_node.set_value(train_start_flag)
    print(f"Set TrainStartFlag to {train_start_flag}")

    print("Nodes 3 to 206 have been set with auto-incrementing string values.")
    print(f"Server running with CustomNode and temperature nodes (ns={idx}, i=3 to i=206)")

    # Keep the server running
    while True:
        pass  # Keep the server running

finally:
    server.stop()
    print("Server stopped.")
