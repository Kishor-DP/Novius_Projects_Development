from opcua import Client, ua
from EventLogger import app_event
class OpcUaNodeScanner:
    def __init__(self, server_url):
        self.client = Client(server_url)

    def connect(self):
        try:
            self.client.connect()
            print("Connected to OPC UA server")
        except Exception as e:
            print(f"Failed to connect to OPC UA server: {e}")

    def disconnect(self):
        self.client.disconnect()
        print("Disconnected from OPC UA server")

    def get_node_values(self, node):
        nodes = []
        for child in node.get_children():
            nodes.append(child)
            nodes.extend(self.get_node_values(child))
        return nodes

    def scan_nodes(self, start_node):
        nodes = self.get_node_values(start_node)
        node_values = {}
        for node in nodes:
            try:
                value = node.get_value()
                node_values[node.nodeid] = value
            except Exception as e:
                node_values[node.nodeid] = f"Error: {e}"
        return node_values

if __name__ == "__main__":
    server_url = "opc.tcp://192.168.1.2:4840"  # Replace with your server URL
    start_node_id = "ns=4;i=830"  # Replace with your specific node ID

    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()

    try:
        start_node = scanner.client.get_node(ua.NodeId.from_string(start_node_id))
        node_values = scanner.scan_nodes(start_node)
        for node_id, value in node_values.items():
            print(f"Node ID: {node_id}, Value: {value}")
            app_event.debug(f"Node ID: {node_id}, Value: {value}")
    finally:
        scanner.disconnect()
