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

# Use the registered namespace index for node creation
# Create nodes for IDs 3 to 206
temperature_nodes = {}
print("Creating temperature nodes...")
for i in range(3, 207):  # 207 is exclusive, so it covers 3 to 206
    node = objects.add_variable(idx, f"TemperatureNode{i}", ua.Variant('', ua.VariantType.String))
    temperature_nodes[i] = node

# Set the same string value for all nodes
value = 'C1,1,5 4 4 4 8748537456,768,34'
print(f"Setting value: {value}")
for i in range(3, 207):
    temperature_nodes[i].set_value(value)
    print(f"Set value for node ns={idx};i={i}")

print("Nodes 3 to 206 have been set with the same string value.")

# Start the server
server.start()

try:
    print(f"Server running with CustomNode and temperature nodes (ns={idx}, i=3 to i=206)")
    while True:
        pass  # Keep the server running
finally:
    server.stop()
    print("Server stopped.")
