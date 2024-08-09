from opcua import ua, Server

# Initialize the OPC UA server
server = Server()

# Set up the server's endpoint
server.set_endpoint("opc.tcp://127.0.0.1:4841/freeopcua/server/")

# Register namespace "http://custom.namespace.example"
uri = "http://custom.namespace.example"
idx = server.register_namespace(uri)

# Confirm the namespace index
print(f"Namespace index for {uri}: {idx}")

# Set up the object node
objects = server.get_objects_node()

# Define the temperature_nodes dictionary outside the conditional block
temperature_nodes = {}

# Create a custom node in the correct namespace (check idx)
if idx == 2:
    custom_node = objects.add_object(idx, "CustomNode")

    # Create 203 temperature nodes with IDs from i=3 to i=205
    for i in range(3, 206):  # Range includes 205
        temp_name = f"Temperature_{i}"
        temp_node = custom_node.add_variable(idx, temp_name, 0.0, ua.VariantType.Float)
        temp_node.set_writable()  # Allow clients to write to these variables
        temperature_nodes[i] = temp_node

    print(f"Created {len(temperature_nodes)} temperature nodes under ns={idx}.")
else:
    print(f"Expected namespace index 2, but got {idx}. Nodes will not be created in ns={idx}.")

# Start the server
server.start()

try:
    print(f"Server running with CustomNode and temperature nodes (ns={idx}, i=3 to i=205)")
    while True:
        # Optionally, update the temperature values dynamically
        for i in range(3, 206):
            temperature_nodes[i].set_value(768 + (i % 10))  # Example: Vary temperature slightly by ID
finally:
    # Close the server when exiting
    server.stop()
