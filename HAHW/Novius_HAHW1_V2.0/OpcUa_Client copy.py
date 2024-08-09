import time
from opcua import Client, ua
from EventLogger import app_event, sys_event
from PLCdb import insert_event

class Opc_UaClient:
    def __init__(self, endpoint):
        self.client = Client(endpoint)
        self.c1_node = None
        self.axle_counter = 0

    def connect(self):
        try:
            self.client.connect()
            print("Client connected successfully")
            app_event.debug("Client connected successfully")
        except Exception as e:
            print(f"Failed to connect to the OPC UA server: {e}")
            sys_event.error(f"Failed to connect to the OPC UA server: {e}")

    def disconnect(self):
        self.client.disconnect()
        print("Client disconnected")
        app_event.debug("Client disconnected")

    def collect_node(self):
        try:
            self.c1_node = self.client.get_node(ua.NodeId(9, 4))
            print('Node collected successfully')
            app_event.debug('Node collected successfully')
        except Exception as e:
            print(f"Failed to collect node: {e}")
            sys_event.error(f"Failed to collect node: {e}")

    def read_node_continuously(self, interval=0.1):
        if not self.c1_node:
            print("Node not collected")
            return

        try:
            while True:
                try:
                    value = self.c1_node.get_value()
                    C1 = value
                    self.axle_counter += 1  # Increment the counter
                    axle_no = self.axle_counter
                    Axle_No = axle_no

                    print(f"Node {self.c1_node.nodeid}: {value}, Axle No: {axle_no}")
                    
                    insert_event(C1, Axle_No)  # Insert data to database with counter
                    
                    app_event.debug(f"Node {self.c1_node.nodeid}: {value}, Axle No: {axle_no}")
                except Exception as e:
                    sys_event.error(f"Failed to read value from node {self.c1_node.nodeid}: {e}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Continuous reading stopped by user")
            app_event.debug("Continuous reading stopped by user")

# Usage
endpoint = "opc.tcp://192.168.1.2:4840"
plc_data_reader = Opc_UaClient(endpoint)
plc_data_reader.connect()
plc_data_reader.collect_node()
plc_data_reader.read_node_continuously(0.1)
plc_data_reader.disconnect()



'''
import time
from opcua import Client, ua
from EventLogger import app_event, sys_event
from PLCdb import insert_event

class Opc_UaClient:
    def __init__(self, endpoint):
        self.client = Client(endpoint)
        self.c1_node = None

    def connect(self):
        try:
            self.client.connect()
            print("Client connected successfully")
            app_event.debug("Client connected successfully")
        except Exception as e:
            print(f"Failed to connect to the OPC UA server: {e}")
            sys_event.error(f"Failed to connect to the OPC UA server: {e}")

    def disconnect(self):
        self.client.disconnect()
        print("Client disconnected")
        app_event.debug("Client disconnected")

    def collect_node(self):
        try:
            self.c1_node = self.client.get_node(ua.NodeId(4, 4))
            print('Node collected successfully')
            app_event.debug('Node collected successfully')
        except Exception as e:
            print(f"Failed to collect node: {e}")
            sys_event.error(f"Failed to collect node: {e}")

    def read_node_continuously(self, interval=0.1):
        if not self.c1_node:
            print("Node not collected")
            return

        try:
            while True:
                try:
                    value = self.c1_node.get_value()
                    print(f"Node {self.c1_node.nodeid}: {value}")
                    C1 = value
                    insert_event(C1) # insert data to database
                    
                    app_event.debug(f"Node {self.c1_node.nodeid}: {value}")
                except Exception as e:
                    sys_event.error(f"Failed to read value from node {self.c1_node.nodeid}: {e}")
                time.sleep(interval)
        except KeyboardInterrupt:
            print("Continuous reading stopped by user")
            app_event.debug("Continuous reading stopped by user")

# Usage
endpoint = "opc.tcp://192.168.1.2:4840"
plc_data_reader = Opc_UaClient(endpoint)
plc_data_reader.connect()
plc_data_reader.collect_node()
plc_data_reader.read_node_continuously(0.1)
plc_data_reader.disconnect()
'''