#insert.py
from jninsert import read_config, insert_into_ICF_Detected, establish_connection
from datetime import datetime
from EventLogger2 import app_event, sys_event




def insert_into_ICF_Detected_function(Component,Status,generated_code):
    # Read connection info from config
    config = read_config()

    # Establish database connection
    conn = establish_connection(config)
    
    # Assuming you have the name and email data you want to insert
    #generated_code=None
    Time_stamp = "ok"
    Code = generated_code
    #Component = Component
    Parameter = "Good"
    #Status = "ok"
    
    
   # Axle_Box_Cover = "Example Axle Box Cover"
    
    # Call insert_into_ICF_Detected function directly with the database connection and all arguments
    insert_into_ICF_Detected(conn, Time_stamp,  Code, Component, Parameter, Status)
    #app_event.debug("insert_into_ICF_Detected: %s",Time_stamp,  Code, Component, Parameter, Status)
    # Log the event
 #    app_event.debug(f"Data inserted - Sr_No: {Sr_No}, Brake Block: {Code}, Side Frame: {Component}, Lower Spring Beam: {Parameter}, Secondary Suspension: {Status}, Shock Absorber: {Time_stamp}, : {},  Suspension Hanger: {Bolster_Suspension_Hanger}, Primary Suspension: {}")
    
    # Close the database connection
    conn.close()
Code=None
Component=None
Status=None
# Call insert_into_ICF_Detected_function to perform the insertion
#insert_into_ICF_Detected_function(Component,Status,Code)
