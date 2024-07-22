import cv2
import os
from datetime import datetime
import time
import json

class VideoRecorder:
    def __init__(self):
        self.video_path = "rtsp://admin:ntipl12345@192.168.1.108:554"#video_path
        self.motion_status_file_path = "motion_status.json"#motion_status_file_path
        self.timestamp_status_file_path = "time_stamp_status.json"#timestamp_status_file_path
        self.folder_location = "/home/jetson/Documents/"#folder_location
        self.vs = None
        self.writer = None
        self.recording = False
        self.last_false_time = None

    def read_time_stamp_status(self):
        try:
            with open(self.timestamp_status_file_path, 'r') as file:
                data = json.load(file)
                read_time_stamp = data.get('time_stamp')
                return read_time_stamp
        except FileNotFoundError:
            print("Time stamp status file not found.")
            return False
        except json.JSONDecodeError:
            print("Error decoding JSON in time stamp status file.")
            return False

    def read_motion_status(self):
        try:
            with open(self.motion_status_file_path, 'r') as file:
                data = json.load(file)
                motion_detected = data.get('motion_detected', "False").lower() == "true"
                return motion_detected
        except FileNotFoundError:
            print("Motion status file not found.")
            return False
        except json.JSONDecodeError:
            print("Error decoding JSON in motion status file.")
            return False

    def start_recording(self):
        if self.video_path == "":
            print("[webcam start]")
            self.vs = cv2.VideoCapture(0)  # Use webcam
        else:
            print("[video start]")
            self.vs = cv2.VideoCapture(self.video_path)

        # Check if video capture is successful
        if not self.vs.isOpened():
            print("Error: Unable to open video source.")
            return

        while True:
            # Read the recording status from the JSON file
            motion_detected = self.read_motion_status()
            print(f"Motion detected: {motion_detected}")
            folder_name_as_trainid = self.read_time_stamp_status()
            print("folder_name:", folder_name_as_trainid)

            ret, frame = self.vs.read()
            if not ret:
                print("Error: Unable to read frame.")
                break
            frame = cv2.resize(frame, (720, 480))

            if motion_detected:
                self.last_false_time = None
                if not self.recording:
                    self.recording = True
                    print("Recording started.")

                if self.writer is None:
                    print("folder_location:", self.folder_location)
                    now = datetime.now()
                    folder_name = folder_name_as_trainid
                    video_name = folder_name_as_trainid
                    full_path = os.path.join(self.folder_location, folder_name)

                    if not os.path.exists(full_path):
                        try:
                            os.makedirs(full_path)
                            print(f"Folder created at: {full_path}")
                        except OSError as e:
                            print(f"Error creating folder: {e}")

                    result_path = os.path.join(full_path, f"{video_name}.avi")
                    fourcc = cv2.VideoWriter_fourcc(*"MJPG")
                    self.writer = cv2.VideoWriter(result_path, fourcc, 25, (frame.shape[1], frame.shape[0]), True)

            else:
                if self.last_false_time is None:
                    self.last_false_time = time.time()
                else:
                    time_diff = time.time() - self.last_false_time
                    if time_diff >= 20:
                        if self.recording:
                            if self.writer is not None:
                                self.writer.release()
                                self.writer = None
                                print("Video writer released.")
                            self.recording = False
                            print("Recording stopped.")
                        self.last_false_time = None

            if self.recording and self.writer is not None:
                self.writer.write(frame)
                cv2.putText(frame, 'Recording...', (10, 30), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 2, cv2.LINE_AA)

            cv2.imshow('Frame', frame)

            if cv2.waitKey(1) & 0xFF == ord('q'):
                break

        self.vs.release()
        cv2.destroyAllWindows()

    #from video_recorder import VideoRecorder

def main():
    #video_path = "rtsp://admin:ntipl12345@192.168.1.108:554"
    #motion_status_file_path = "motion_status.json"
    #timestamp_status_file_path = "time_stamp_status.json"
    #folder_location = "/home/jetson/Documents/"
    
    recorder = VideoRecorder()
    recorder.start_recording()

if __name__ == "__main__":
   main()
