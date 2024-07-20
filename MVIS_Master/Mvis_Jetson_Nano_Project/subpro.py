#!/usr/bin/env python3
import time
import subprocess
import threading

def run_script(script_path):
    try:
        subprocess.run(['python3', script_path], check=True)
        print(f"Script {script_path} executed successfully")
    except subprocess.CalledProcessError as e:
        print(f"Error executing script {script_path}: {e}")

# List of scripts to run
scripts_to_run = ['rtsp_stream.py']

# Run each script in a separate thread
threads = []
for script in scripts_to_run:
    thread = threading.Thread(target=run_script, args=(script,))
    threads.append(thread)
    thread.start()

# Wait for all threads to finish
for thread in threads:
    thread.join()


