#!/usr/bin/env python3
#rtsp_stream.py
import os
import subprocess
import time
import json
with open('cam.json') as f:
  config = json.load(f)

MAX_RETRIES = 28000
RETRY_DELAY = 5  # in seconds

  
while True:
    for i in range(1, MAX_RETRIES + 1):
        print(f"Attempt {i}")
        #camip = config.get("camip", "")
        #print("camip--------",camip)
        # Check if the server is reachable
        if subprocess.call(["ping", "-c", "1", "-W", "2", config["camip"]]) != 0:
            print("Server not reachable. Retrying in 10 seconds...")
            time.sleep(10)
            continue

        # Execute the modprobe command
        subprocess.call(["sudo", "modprobe", "v4l2loopback", "exclusive_caps=1"])

        # Execute the ffmpeg command
        subprocess.call(["ffmpeg", "-rtsp_transport", "tcp", "-stimeout", "60000000", "-stream_loop", "-1", "-i", config["url"], "-vf", "format=pix_fmts=yuv420p", "-f", "v4l2", "/dev/video0"])

        if subprocess.call(["echo", "$?"]) == 0:
            print("Stream completed successfully.")
            break
        else:
            print(f"Stream failed. Retrying in {RETRY_DELAY} seconds...")
            time.sleep(RETRY_DELAY)

    print("Restarting the script in 10 seconds...")
    time.sleep(10)
