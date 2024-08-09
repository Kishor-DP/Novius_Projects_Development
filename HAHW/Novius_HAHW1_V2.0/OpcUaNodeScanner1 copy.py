import threading
import time
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

class OpcUaDataReceiver:
    def __init__(self, client, node_id, interval=0.1):
        self.client = client
        self.node_id = node_id
        self.interval = interval
        self.running = False
        self.node = None

    def start(self):
        self.node = self.client.get_node(ua.NodeId.from_string(self.node_id))
        self.running = True
        self.thread = threading.Thread(target=self._receive_data)
        self.thread.start()
        print(f"Started receiving data from node {self.node_id} every {self.interval} seconds")

    def stop(self):
        self.running = False
        self.thread.join()
        print(f"Stopped receiving data from node {self.node_id}")

    def _receive_data(self):
        while self.running:
            try:
                value = self.node.get_value()
                print(f"Node ID: {self.node_id}, Value: {value}")
            except Exception as e:
                print(f"Error reading value from node {self.node_id}: {e}")
            time.sleep(self.interval)

if __name__ == "__main__":
    server_url = "opc.tcp://192.168.1.2:4840"  # Replace with your server URL
    node_id = "ns=4;i=103"  # Node ID to receive data from
    interval = 0.1  # Interval in seconds

    scanner = OpcUaNodeScanner(server_url)
    scanner.connect()

    try:
        receiver = OpcUaDataReceiver(scanner.client, node_id, interval)
        receiver.start()
        
        # Keep the main thread running to allow data reception
        try:
            while True:
                time.sleep(1)
        except KeyboardInterrupt:
            print("Stopping data receiver...")
        finally:
            receiver.stop()
    finally:
        scanner.disconnect()
