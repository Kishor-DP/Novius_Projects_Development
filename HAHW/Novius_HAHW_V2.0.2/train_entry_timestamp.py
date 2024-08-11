#train_entry_timestamp.py
from datetime import datetime
from EventLogger2 import app_event



def train_entry_timestamp():
    #global trainId_as_datetime
    
    # Append current time to the generated code
    record_datetime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S_2000')
    #current_time = datetime.now().strftime("%Y%m%d%H%M%S")
    trainId_as_datetime = f"{record_datetime}"
    
    
    #app_event.debug("train_entry_timestamp: %s", trainId_as_datetime)
    
    return trainId_as_datetime

# Example usage:
#trainId_as_datetime = train_entry_timestamp()
# Each time you call generated_code_trigger(), it will generate and return a new code with the current time
#print("train_entry_timestamp:", trainId_as_datetime)
