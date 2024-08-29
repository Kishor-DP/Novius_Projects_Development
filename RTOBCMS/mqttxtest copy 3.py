import paho.mqtt.client as mqtt
from datetime import datetime
import pyodbc
import json
# Database connection
conn = pyodbc.connect('DRIVER={SQL Server};SERVER=4MVDUGL\\SQLEXPRESS;DATABASE=LoraWan;Trusted_Connection=yes;')
cursor = conn.cursor()

# Callback when a message is received
def on_message(client, userdata, msg):
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
    cursor.execute("""
        INSERT INTO SensorData (gateway_id, sensor_id, location, status, timestamp)
        VALUES (?, ?, ?, ?, ?)
    """, (gateway_id, sensor_id, location, status, timestamp))
    
    conn.commit()
    print(f"(gateway_id, sensor_id, location, status, timestamp)){gateway_id, sensor_id, location, status, timestamp}")
# Callback when the client connects to the broker
def on_connect(client, userdata, flags, rc):
    print(f"Connected with result code {rc}")
    client.subscribe('application/de6f74d2-b917-44b9-b0cf-e5e61c9ea819/device/0080e1150536aeca/event/up')

# MQTT setup
client = mqtt.Client()
client.on_message = on_message
client.on_connect = on_connect

client.connect('localhost', 1883, 60)

# Start the MQTT client loop
client.loop_forever()







# import paho.mqtt.client as mqtt
# import pyodbc
# from datetime import datetime

# # Database connection
# conn = pyodbc.connect('DRIVER={SQL Server};SERVER=4MVDUGL\SQLEXPRESS;DATABASE=LoraWan;Trusted_Connection=yes;')
# cursor = conn.cursor()

# # MQTT callback function
# def on_message(client, userdata, msg):
#     topic_parts = msg.topic.split('/')
#     gateway_id = topic_parts[1]
#     sensor_id = topic_parts[2]
#     location = "XYZ"  # You can dynamically set this based on your setup
#     status = msg.payload.decode()
#     timestamp = datetime.now()

#     cursor.execute("""
#         INSERT INTO SensorData (gateway_id, sensor_id, location, status, timestamp)
#         VALUES (?, ?, ?, ?, ?)
#     """, (gateway_id, sensor_id, location, status, timestamp))
#     conn.commit()

# # MQTT setup
# client = mqtt.Client()
# client.on_message = on_message

# client.connect('a84041ffff27ca3c', 1883, 60)
# client.subscribe('application/11/device/0080e11505357a95/event/up')

# client.loop_forever()
