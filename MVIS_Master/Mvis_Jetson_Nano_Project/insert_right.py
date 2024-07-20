#insert.py
from jninsert_right import read_config, insert_into_ICF_Detected, establish_connection
from datetime import datetime
from EventLogger2 import app_event, sys_event

import random
import string

# Define a function to generate random code
def generate_code(length):
    # Define the character set from which to generate the code
    characters = string.ascii_letters + string.digits
    # Generate a random code of specified length
    return ''.join(random.choice(characters) for _ in range(length))

# Specify the length of the code
code_length = 10

# Generate the code
generated_code = generate_code(code_length)

# Assign the generated code to the Code variable
#Code = generated_code

# Print the generated code
print("Generated Code:", generated_code)


def insert_into_ICF_Detected_function(Component,Parameter,Status):
    # Read connection info from config
    config = read_config()

    # Establish database connection
    conn = establish_connection(config)
    
    # Assuming you have the name and email data you want to insert
    
    Time_stamp = "ok"
    Code = generated_code
    #Component = Component
    #Parameter = "Good"
    #Status = "ok"
    
    
   # Axle_Box_Cover = "Example Axle Box Cover"
    
    # Call insert_into_ICF_Detected function directly with the database connection and all arguments
    insert_into_ICF_Detected(conn, Time_stamp,  Code, Component, Parameter, Status)
    
    # Log the event
 #    app_event.debug(f"Data inserted - Sr_No: {Sr_No}, Brake Block: {Code}, Side Frame: {Component}, Lower Spring Beam: {Parameter}, Secondary Suspension: {Status}, Shock Absorber: {Time_stamp}, : {},  Suspension Hanger: {Bolster_Suspension_Hanger}, Primary Suspension: {}")
    
    # Close the database connection
    conn.close()
Component=None
Parameter=None
Status=None
# Call insert_into_ICF_Detected_function to perform the insertion
insert_into_ICF_Detected_function(Component,Parameter,Status)
