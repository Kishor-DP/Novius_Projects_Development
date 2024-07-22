#!/usr/bin/env python3
#railway.py
import sys
import argparse
from jetson_inference import detectNet
from jetson_utils import videoSource, videoOutput, Log
#import threading
#import jetson.inference
from jetson_utils import (videoSource, videoOutput, saveImage, Log,
                        cudaAllocMapped, cudaCrop, cudaDeviceSynchronize)
import os
import numpy as np
#from PIL import Image
from datetime import datetime
from EventLogger2 import app_event, sys_event
from Mvis_Csv import insert_record_into_tblMvis_Events
import datetime
import time
from PIL import Image
import json
from json.decoder import JSONDecodeError  # Import JSONDecodeError


def create_video_source(input_url, options, argv):
    max_retries_input = 10000 # Maximum number of retries for creating input
    retry_count_input = 0  # Counter for retry attempts for creating input
    while True:
        try:
            # Attempt to create the video source
            return videoSource(input_url, options=options, argv=argv)
        except Exception as e:
            if retry_count_input < max_retries_input:
                retry_count_input += 1
                print("Failed to input create video source. Retrying... Attempt", retry_count_input)
                time.sleep(1)  # Add a delay before retrying
            else:
                print("Failed to input create video source after maximum retries.")
                return None

def read_motion_status(max_retries=3, retry_interval=1):
    retries = 0
    while retries < max_retries:
        try:
            with open('motion_status.json', 'r') as json_file:
                motion_data = json.load(json_file)
                return motion_data.get("motion_detected", False)
        except FileNotFoundError:
            print("File not found. Retrying in {} seconds...".format(retry_interval))
        except JSONDecodeError:
            print("Invalid JSON data. Retrying in {} seconds...".format(retry_interval))
        time.sleep(retry_interval)
        retries += 1
    return False

def read_share_assign_time_stamp_status(max_retries=3, retry_interval=1):
    retries = 0
    while retries < max_retries:
        try:
            with open('time_stamp_status.json', 'r') as json_file:
                time_stamp_data = json.load(json_file)
                return time_stamp_data.get("time_stamp", False)
        except FileNotFoundError:
            print("File not found. Retrying in {} seconds...".format(retry_interval))
        except JSONDecodeError:
            print("Invalid JSON data. Retrying in {} seconds...".format(retry_interval))
        time.sleep(retry_interval)
        retries += 1
    return False


'''
def read_motion_status(max_retries=3, retry_interval=1):
    retries = 0
    while retries < max_retries:
        try:
            with open('motion_status.json', 'r') as json_file:
                motion_data = json.load(json_file)
                return motion_data.get("motion_detected", False)
        except FileNotFoundError:
            print("File not found. Retrying in {} seconds...".format(retry_interval))
            time.sleep(retry_interval)
            retries += 1
    return False
'''

'''
# Function to read motion status from JSON file
def read_motion_status():
    try:
        with open('motion_status.json', 'r') as json_file:
            motion_data = json.load(json_file)
            return motion_data.get("motion_detected", False)
    except FileNotFoundError:
        return False
'''

def railway_bogie_detection():
    

    # parse the command line
    parser = argparse.ArgumentParser(description="Locate objects in a live input stream using an object detection DNN.", 
                                     formatter_class=argparse.RawTextHelpFormatter, 
                                     epilog=detectNet.Usage() + videoSource.Usage() + videoOutput.Usage() + Log.Usage())

    parser.add_argument("input", type=str, default="", nargs='?', help="URI of the input stream")
    parser.add_argument("output", type=str, default="", nargs='?', help="URI of the output stream")
    parser.add_argument("--network", type=str, default="ssd-mobilenet-v2", help="pre-trained model to load (see below for options)")
    parser.add_argument("--overlay", type=str, default="box,labels,conf", help="detection overlay flags (e.g. --overlay=box,labels,conf)\nvalid combinations are:  'box', 'labels', 'conf', 'none'")
    parser.add_argument("--threshold", type=float, default=0.5, help="minimum detection threshold to use") 
    parser.add_argument("--snapshots", type=str, default="images/test/detections", help="output directory of detection snapshots")
    parser.add_argument("--timestamp", type=str, default="%Y%m%d-%H%M%S-%f", help="timestamp format used in snapshot filenames")
    try:
        args = parser.parse_known_args()[0]
    except:
        print("")
        parser.print_help()
        sys.exit(0)
    output = videoOutput(args.output, argv=sys.argv)

    net = detectNet(model="/home/jetson/Mvis_Jetson_Nano_Project/network/ssd-mobilenet.onnx", labels="/home/jetson/Mvis_Jetson_Nano_Project/network/labels.txt", 
                    input_blob="input_0", output_cvg="scores", output_bbox="boxes", 
                    threshold=args.threshold)
    
    #input_url="/home/jetson/LHB.mp4"
    input_url = "rtsp://admin:ntipl12345@192.168.1.108:554/cam/realmonitor?channel=1&subtype=1"
    input_options = {'width': 720, 'height': 480, 'framerate': 20, 'flipMethod': 'rotate-0'}
    input_source = create_video_source(input_url, options=input_options, argv=sys.argv)
    
    if input_source is None:
        print("Failed to create video source.")
        return
    

    #input_url = "/dev/video0"#"/dev/video0"
    #input = videoSource(input_url,options={'width': 720, 'height': 480, 'framerate': 20, 'flipMethod': 'rotate-0'}, argv=sys.argv)
   

    # Load class labels from a file (assuming the file contains one class label per line)
    with open('/home/jetson/Mvis_Jetson_Nano_Project/network/labels.txt', 'r') as file:
        class_labels = file.read().splitlines()

    target_class_ids = [0,1, 2, 3, 4, 5, 6, 7, 8, 9,10,11,12,13,14,15,16,17,18,19]
    output_dirs = {class_id: f'images/{class_labels[class_id]}' for class_id in target_class_ids}
    for output_dir in output_dirs.values():
        os.makedirs(output_dir, exist_ok=True)
    max_retries = 10000  # Maximum number of retries
    retry_count = 0  # Counter for retry attempts
    while True:
        # Read motion status from JSON file
        motion_detected = read_motion_status()
        time_stamp=read_share_assign_time_stamp_status()

        img = input_source.Capture()

        if img is None : # timeout
            if retry_count < max_retries:
                retry_count += 1
                #input = videoSource(input_url,options={'width': 720, 'height': 480, 'framerate': 20, 'flipMethod': 'rotate-0'}, argv=sys.argv)
                print("railway.py Failed to capture image. Retrying... Attempt", retry_count)
               # Restart the stream or continue processing from the beginning
                input_source.Close()
                input_source = create_video_source(input_url, options=input_options, argv=sys.argv)
                continue
            else:
                print("railway.py Failed to capture image after maximum retries.")
                break  # Exit the loop if maximum retries exceeded
        else:
            retry_count = 0  # Reset retry count if successful image capture
  

        detections = net.Detect(img, overlay=args.overlay)
        #print("detected {:d} objects in image".format(len(detections)))

        timestamp = datetime.datetime.now().strftime(args.timestamp)

        # Perform actions based on motion status
        if motion_detected == "True":
            print("railway Motion detected!")
            # Start detection or perform actions
            for idx, detection in enumerate(detections):
                # Get the class ID of the detection
                
                print("railway_time_stamp_from_json",time_stamp)
                #print(detection)
        
                # Assuming img is your original image
                snapshot = cudaAllocMapped(width=img.width, height=img.height, format=img.format)
                
                # Convert PIL image to NumPy array
                img_array = np.array(img)
                
                # Ensure that both img_array and snapshot have the same dimensions and data type
                assert img_array.shape == (snapshot.height, snapshot.width, 3), "Image and snapshot dimensions mismatch"
                assert img_array.dtype == np.uint8, "Image data type is not uint8"
                
                # Copy the image data to the snapshot
                snapshot_array = np.array(snapshot)
                snapshot_array[:] = img_array[:]
                
                # Convert the snapshot array to a PIL Image
                snapshot_pil = Image.fromarray(snapshot_array)

                
                
                class_id = int(detection.ClassID)
                
                # Save the image using PIL to the appropriate directory based on class label
                class_label = class_labels[class_id]
                
                snapshot_dir = output_dirs[class_id]
                snapshot_filename = f"{class_label}-{timestamp}-{idx}.jpg"
                snapshot_pil.save(os.path.join(snapshot_dir, snapshot_filename))
                #app_event.debug(f"Saved image: {snapshot_filename}")
                Component = class_label
                if Component == "Track":
                    print("Skipping class ID 5 detection")  # Debugging statement
                    continue
                print(Component)
                insert_record_into_tblMvis_Events(timestamp,time_stamp,Component)
                print("componnrt",Component)
                cudaDeviceSynchronize()
                del snapshot
                #output.Render(img)
                #output.SetStatus("Novius")
                #net.PrintProfilerTimes()
            # Check if the input source is at the end of the stream
            if np.all(img == 0):
                # Restart the stream or continue processing from the beginning
                input_source.Close()
                input_source = create_video_source(input_url, options=input_options, argv=sys.argv)
                continue
            output.Render(img)
            output.SetStatus("Novius")
            if not input_source.IsStreaming() or not output.IsStreaming():
                break    
        else:
            print("railway No motion detected.")
            # Stop detection or perform actions

        # Sleep for some time before checking again
        #time.sleep(1)
        

        

if __name__ == "__main__":
    railway_bogie_detection()
