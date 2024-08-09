#!/bin/bash
sleep 60  # Wait for 120 seconds
export DISPLAY=:0
xterm -hold -e /usr/bin/python3 /home/jetson/Novius_Projects_Development/MVIS_Master/Mvis_Jetson_Nano_Project/railway_wheel_motion.py
