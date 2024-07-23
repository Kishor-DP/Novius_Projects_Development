import cv2
import os
from datetime import datetime
import time
import json

def read_time_stamp_status(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            read_time_stamp = data.get('time_stamp')
            print(read_time_stamp)
            return read_time_stamp
    except FileNotFoundError:
        print("Motion status file not found.")
        return False
    except json.JSONDecodeError:
        print("Error decoding JSON in motion status file.")
        return False
file_path="time_stamp_status.json"
read_time_stamp_status(file_path)
# Function to read the recording status from the JSON file
def read_motion_status(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
            motion_detected = data.get('motion_detected', "False").lower() == "true"
            return motion_detected
    except FileNotFoundError:
        print("Motion status file not found.")
        return False
    except json.JSONDecodeError:
        print("Error decoding JSON in motion status file.")
        return False

# Path to the motion_status.json file
motion_status_file_path = r"motion_status.json"

# Initialize video capture
video_path = "rtsp://admin:ntipl12345@192.168.1.108:554"  # Set to the path of your video file
if video_path == "":
    print("[webcam start]")
    vs = cv2.VideoCapture(0)  # Use webcam
else:
    print("[video start]")
    vs = cv2.VideoCapture(video_path)

# Check if video capture is successful
if not vs.isOpened():
    print("Error: Unable to open video source.")
    exit()

# Initialize video writer
writer = None
recording = False
pause_time = None
last_false_time = None  # Track the time since motion status remained False

while True:
    # Read the recording status from the JSON file
    motion_detected = read_motion_status(motion_status_file_path)
    print(f"Motion detected: {motion_detected}")
    file_path="time_stamp_status.json"
    folder_name_as_trainid=read_time_stamp_status(file_path)
    print("folder_name:",folder_name_as_trainid)

    ret, frame = vs.read()
    if not ret:
        print("Error: Unable to read frame.")
        break
    frame = cv2.resize(frame, (720, 480))

    if motion_detected:
        last_false_time = None
        if not recording:
            recording = True
            print("Recording started.")
        
        if writer is None:
            folder_location = r"/home/jetson/Documents/"
            print("folder_location:",folder_name_as_trainid)
            now = datetime.now()
            datestamp = now.strftime('%Y%m%d')
            timestamp = now.strftime('%H%M%S')
            folder_name = folder_name_as_trainid
            video_name = folder_name_as_trainid#f"{datestamp}_{timestamp}"
            full_path = os.path.join(folder_location, folder_name)

            if not os.path.exists(full_path):
                try:
                    os.makedirs(full_path)
                    print(f"Folder created at: {full_path}")
                except OSError as e:
                    print(f"Error creating folder: {e}")

            result_path = os.path.join(full_path, f"{video_name}.avi")
            fourcc = cv2.VideoWriter_fourcc(*"MJPG")
            writer = cv2.VideoWriter(result_path, fourcc, 25, (frame.shape[1], frame.shape[0]), True)

    else:
        if last_false_time is None:
            last_false_time = time.time()
        else:
            time_diff = time.time() - last_false_time
            if time_diff >= 20:
                if recording:
                    if writer is not None:
                        writer.release()
                        writer = None
                        print("Video writer released.")
                    recording = False
                    print("Recording stopped.")
                last_false_time = None

    if recording and writer is not None:
        writer.write(frame)
        cv2.putText(frame, 'Recording...', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

    cv2.imshow('Frame', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

vs.release()
cv2.destroyAllWindows()
