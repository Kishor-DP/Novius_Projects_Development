import paho.mqtt.client as mqtt
from datetime import datetime
import pyodbc
import json

class MqttToDatabase:
    def __init__(self, db_connection_string, mqtt_broker, mqtt_port, mqtt_topic):
        # Initialize database connection
        self.conn = pyodbc.connect(db_connection_string)
        self.cursor = self.conn.cursor()
        
        # Initialize MQTT client
        self.client = mqtt.Client()
        self.client.on_message = self.on_message
        self.client.on_connect = self.on_connect

        self.mqtt_broker = mqtt_broker
        self.mqtt_port = mqtt_port
        self.mqtt_topic = mqtt_topic

    # Callback when a message is received
    def on_message(self, client, userdata, msg):
        topic_parts = msg.topic.split('/')
        gateway_id = topic_parts[1]
        sensor_id = topic_parts[2]
        location = "XYZ"  # Update as needed
        status = msg.payload.decode()
        timestamp = datetime.now()

        # Save status to JSON file
        status_data = {
            "gateway_id": gateway_id,
            "sensor_id": sensor_id,
            "location": location,
            "status": status,
            "timestamp": timestamp.isoformat()
        }
        with open('status.json', 'w') as json_file:
            json.dump(status_data, json_file, indent=4)
        
        # Insert data into the database
        self.cursor.execute("""
            INSERT INTO SensorData (gateway_id, sensor_id, location, status, timestamp)
            VALUES (?, ?, ?, ?, ?)
        """, (gateway_id, sensor_id, location, status, timestamp))
        
        self.conn.commit()
        print(f"(gateway_id, sensor_id, location, status, timestamp) {gateway_id, sensor_id, location, status, timestamp}")

    # Callback when the client connects to the broker
    def on_connect(self, client, userdata, flags, rc):
        print(f"Connected with result code {rc}")
        client.subscribe(self.mqtt_topic)

    # Start the MQTT client loop
    def start(self):
        self.client.connect(self.mqtt_broker, self.mqtt_port, 60)
        self.client.loop_forever()
    
# Usage example
if __name__ == "__main__":
    db_connection_string = 'DRIVER={SQL Server};SERVER=4MVDUGL\\SQLEXPRESS;DATABASE=LoraWan;Trusted_Connection=yes;'
    mqtt_broker = 'localhost'
    mqtt_port = 1883
    mqtt_topic = 'application/de6f74d2-b917-44b9-b0cf-e5e61c9ea819/device/0080e1150536aeca/event/up'
    
    mqtt_to_db = MqttToDatabase(db_connection_string, mqtt_broker, mqtt_port, mqtt_topic)
    mqtt_to_db.start()
