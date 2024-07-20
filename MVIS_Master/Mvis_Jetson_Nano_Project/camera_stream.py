# camera_stream.py

import cv2

def stream_rtsp():
    # Open the RTSP stream
    rtsp_stream = cv2.VideoCapture('rtsp://admin:ntipl12345@192.168.1.108:554')

    while True:
        ret, frame = rtsp_stream.read()
        if not ret:
            print("Error reading frame from RTSP stream")
            break
        yield frame

    rtsp_stream.release()

