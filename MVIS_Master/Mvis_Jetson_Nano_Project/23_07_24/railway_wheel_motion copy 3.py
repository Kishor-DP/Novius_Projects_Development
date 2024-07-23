#railway_wheel_motion
import cv2
import sys
#import numpy as np
import jetson.utils
import json
from jetson_utils import videoSource, videoOutput
from railway import railway_bogie_detection
import threading
import time
from train_entry_timestamp import generated_code,generate_code
from Mvis_Csv import insert_into_tblGridview_to_start_train
from EventLogger2 import app_event
import numpy as np
from Monitor_Folder import FileRotator
from functools import wraps

def retry(exceptions, tries=31536063734300000, delay=1, backoff=2):
    def decorator_retry(func):
        @wraps(func)
        def wrapper_retry(*args, **kwargs):
            _tries, _delay = tries, delay
            while _tries > 1:
                try:
                    return func(*args, **kwargs)
                except exceptions as e:
                    print(f"Retrying func2 in {_delay} seconds... ({_tries-1} tries left) due to {e}")
                    time.sleep(_delay)
                    _tries -= 1
                    #_delay *= backoff
            return func(*args, **kwargs)
        return wrapper_retry
    return decorator_retry

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
                print("Failed to create video source. Retrying... Attempt", retry_count_input)
                time.sleep(1)  # Add a delay before retrying
            else:
                print("Failed to create video source after maximum retries.")
                return None

# Function to write motion status to JSON file with retry
def write_motion_status(status, max_retries=3, retry_interval=1):
    retries = 0
    while retries < max_retries:
        try:
            motion_data = {"motion_detected": status}
            with open('motion_status.json', 'w') as json_file:
                json.dump(motion_data, json_file)
            return  # Exit function if writing succeeds
        except Exception as e:
            print(f"Error writing JSON file (retry {retries + 1}/{max_retries}):", e)
            retries += 1
            time.sleep(retry_interval)
    print("Failed to write JSON file after maximum retries")

# Function to write motion status to JSON file with retry
def write_share_assign_time_stamp_status(status2, max_retries=3, retry_interval=1):
    retries = 0
    while retries < max_retries:
        try:
            time_stamp_data = {"time_stamp": status2}
            with open('time_stamp_status.json', 'w') as json_file:
                json.dump(time_stamp_data, json_file)
            return  # Exit function if writing succeeds
        except Exception as e:
            print(f"Error writing JSON file (retry {retries + 1}/{max_retries}):", e)
            retries += 1
            time.sleep(retry_interval)
    print("Failed to write JSON file after maximum retries")
    
@retry(Exception)
def capture_image(input_source):
    return input_source.Capture()
'''
# Function to write motion status to JSON file
def write_motion_status(status):
    motion_data = {"motion_detected": status}
    try:
        with open('motion_status.json', 'w') as json_file:
            json.dump(motion_data, json_file)
    except Exception as e:
        print("Error writing JSON file:", e)
'''
share_assign_time_stamp = generate_code(10)
assign_time_stamp = 0
#write_motion_status("True")
def railway_wheel_motion():
    global share_assign_time_stamp
    # Define input and output URIs
    #input_url="/home/jetson/LHB.mp4"
    input_url = "rtsp://admin:ntipl12345@192.168.1.108:554/cam/realmonitor?channel=1&subtype=0"
    input_options = {'width': 720, 'height': 480, 'framerate': 20, 'flipMethod': 'rotate-0'}
    input_source = create_video_source(input_url, options=input_options, argv=sys.argv)
    
    if input_source is None:
        print("Failed to create video source.")
        return
    #output_uri = "123filename.mp4"
    output_uri="display://0"
    # Create video source & output
    #input_source = videoSource(input_uri, options={'width': 720, 'height':480, 'framerate': 25, 'flipMethod': 'rotate-0'})
    #output = videoOutput( options={'codec': 'h264', 'bitrate': 4000000})
    output = videoOutput(output_uri, options={'codec': 'h264', 'bitrate': 4000000})

    # Define motion detection parameters
    motion_threshold = 500000  # Adjust according to your needs

    # Create background subtractor
    background_subtractor = cv2.createBackgroundSubtractorMOG2()

    # Define the regions of interest (ROIs) for motion detection
    # Format: (x, y, width, height)
    roi_1 = (0, 0, 240, 240)  # Define the first ROI
    roi_2 = (240, 0, 240, 240)  # Define the second ROI

    # Define the colors for drawing the ROIs (BGR format)
    roi_color_1 = (0, 255, 0)  # Green
    roi_color_2 = (0, 0, 255)  # Red

    max_retries = 10000  # Maximum number of retries
    retry_count = 0  # Counter for retry attempts
    last_motion_time = time.time()  # Initialize the variable to track the time of the last motion detection
    
    #KP COMMENT BELOW LINE WHEN IMPLEMENTATION DONE ON SITE
    insert_into_tblGridview_to_start_train(share_assign_time_stamp)
    
    # Capture frames until end-of-stream (or the user exits)
    while True:
        try:
            image = capture_image(input_source)
            if image is None:
                raise Exception("End of Stream")
        except Exception as e:
            print(f"Failed to capture image after maximum retries: {e}")
            break

        retry_count = 0
        
        
        # Convert CUDA image to NumPy array
        image_np = jetson.utils.cudaToNumpy(image)
        '''
        train motion region can be corrected here
        # Define the regions of interest (ROIs) for motion detection
        # Format: (x, y, width, height)
        '''
        roi_hight_setting1 = 300
        roi_hight_setting2 = 300
        roi_1 = (450, roi_hight_setting1, 200, 50)  # Adjust coordinates and size of the first ROI
        roi_2 = (100, roi_hight_setting2, 200, 50)  # Adjust coordinates and size of the second ROI


        # Extract ROIs from the image
        roi_1_image = image_np[roi_1[1]:roi_1[1]+roi_1[3], roi_1[0]:roi_1[0]+roi_1[2]]
        roi_2_image = image_np[roi_2[1]:roi_2[1]+roi_2[3], roi_2[0]:roi_2[0]+roi_2[2]]

        # Apply background subtraction to detect motion in each ROI
        motion_mask_roi_1 = background_subtractor.apply(roi_1_image)
        motion_mask_roi_2 = background_subtractor.apply(roi_2_image)

        # Calculate the sum of pixel values in the motion masks for each ROI
        motion_value_roi_1 = motion_mask_roi_1.sum()
        motion_value_roi_2 = motion_mask_roi_2.sum()

        # Draw rectangles around the ROIs on the output image
        cv2.rectangle(image_np, (roi_1[0], roi_1[1]), (roi_1[0]+roi_1[2], roi_1[1]+roi_1[3]), roi_color_1, 2)
        cv2.rectangle(image_np, (roi_2[0], roi_2[1]), (roi_2[0]+roi_2[2], roi_2[1]+roi_2[3]), roi_color_2, 2)

        # If the motion value exceeds the threshold in any ROI, motion is detected
        if motion_value_roi_1 > motion_threshold or motion_value_roi_2 > motion_threshold:
            print("Motion detected!")
            last_motion_time = time.time()  # Update the last motion time
            if assign_time_stamp == 0:
                print("assign_time_stamp can be added here kp")
                print("share_assigned_time_stamp_is_here",share_assign_time_stamp)
                
                motion_detected = "True" # Change this to the actual condition
                # Write motion status to JSON file
                write_motion_status(motion_detected)
                time_stamp = share_assign_time_stamp
                write_share_assign_time_stamp_status(time_stamp)
                last_motion_time_one_time_iterate = 0
                
            # Perform actions when motion is detected
        else:
            print("No motion detected.")
            #motion_detected = "False"
            #write_motion_status(motion_detected)
            # Check if no motion has been detected for 30 seconds
            
            if time.time() - last_motion_time >= 120:
                if last_motion_time_one_time_iterate == 0:
                    motion_detected = "False"
                    write_motion_status(motion_detected)
                    print("No motion detected for 120 seconds.")
                    share_assign_time_stamp = generate_code(10)
                    print("insert_into_tblGridview_to_start_train",share_assign_time_stamp)
                    insert_into_tblGridview_to_start_train(share_assign_time_stamp)
                    last_motion_time_one_time_iterate = 1
                # Perform actions when no motion is detected for 30 seconds
                # Perform actions when no motion is detected
        

            # Render the image
            output.Render(jetson.utils.cudaFromNumpy(image_np))

            # Update the title bar
            output.SetStatus("Novius MVIS Viewer")

        
        # Exit on input/output EOS
        #if not input_source.IsStreaming() or not output.IsStreaming():
        #    break
        #time.sleep(1)
#FileRotator.monitor_folder_runner()
# Define a function to run railway_wheel_motion in a separate thread
def run_railway_wheel_motion():    
    railway_wheel_motion()

# Define a function to run railway_bogie_detection in a separate thread
def run_railway_bogie_detection():    
    railway_bogie_detection()

def run_Monitor_Folder_runner():
    FileRotator.monitor_Folder_runner()

# Create threads for each function
wheel_motion_thread = threading.Thread(target=run_railway_wheel_motion)
bogie_detection_thread = threading.Thread(target=run_railway_bogie_detection)
#Monitor_Folder_thread=threading.Thread(target=run_Monitor_Folder_runner)
# Start both threads
wheel_motion_thread.start()
bogie_detection_thread.start()
#Monitor_Folder_thread.start()


# Wait for both threads to finish
wheel_motion_thread.join()
bogie_detection_thread.join()
#Monitor_Folder_thread.join()

