import json
import time
import threading
from opcua import Server, ua

# Load configuration from JSON file
def load_config(filename):
    with open(filename, 'r') as file:
        config = json.load(file)
    return config

# Function to read TrainStartFlag value
def read_train_start_flag():
    while True:
        try:
            train_start_flag_value = train_start_node.get_value()
            print(f"Current TrainStartFlag value: {train_start_flag_value}")
        except Exception as e:
            print(f"Error reading TrainStartFlag value: {e}")
        time.sleep(1)  # Read every second

# Function to update TrainStartFlag value from JSON file
def update_train_start_flag():
    while True:
        try:
            config = load_config('TrainStartFlag.json')
            train_start_flag = config.get("TrainStartFlag", False)
            train_start_node.set_value(train_start_flag)
            print(f"Updated TrainStartFlag to {train_start_flag}")
        except Exception as e:
            print(f"Error updating TrainStartFlag: {e}")
        time.sleep(5)  # Update every 5 seconds

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
    # Load the configuration initially
    config = load_config('TrainStartFlag.json')
    
    # Set initial TrainStartFlag value
    train_start_flag = config.get("TrainStartFlag", False)
    train_start_node.set_value(train_start_flag)
    print(f"Initial TrainStartFlag set to {train_start_flag}")

    # Set auto-incrementing string values for all nodes
    for i in range(3, 5):
        value = f'C1,{i-2},5 4 4 4 8748537456,768,34'  # Adjust based on the node ID
        node = temperature_nodes[i]
        node.set_value(value)
        print(f"Set value for node ns={idx};i={i}: {value}")

    # Start threads for reading and updating TrainStartFlag
    read_thread = threading.Thread(target=read_train_start_flag)
    read_thread.daemon = True  # This makes sure the thread will exit when the main program exits
    read_thread.start()

    update_thread = threading.Thread(target=update_train_start_flag)
    update_thread.daemon = True
    update_thread.start()
    print(f"TrainStart node value is {train_start_node,train_start_flag}")
    print("Nodes 3 to 206 have been set with auto-incrementing string values.")
    print(f"Server running with CustomNode and temperature nodes (ns={idx}, i=3 to i=206)")

    # Keep the server running
    while True:
        pass  # Keep the server running

finally:
    server.stop()
    print("Server stopped.")
