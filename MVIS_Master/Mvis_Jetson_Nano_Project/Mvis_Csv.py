import csv
import os
from datetime import datetime

# Define the filenames for the CSV files
mvis_events_file = '/home/jetson/Documents/Mvis_Events.csv'
gridviewtbl_file = '/home/jetson/Documents/Gridviewtbl.csv'

def check_and_create_file(file_path, headers):
    if not os.path.exists(file_path):
        with open(file_path, mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(headers)
        print(f'{os.path.basename(file_path)} CSV file created')

# Check and create the CSV files with headers if they don't exist
check_and_create_file(mvis_events_file, ['Time_stamp', 'Code', 'Component', 'Parameter', 'Status'])
check_and_create_file(gridviewtbl_file, ['Time_Stamp_Gridviewtbl', 'Code'])

print('CSV files checked/created')

def insert_record_into_tblMvis_Events(time_stamp, code, component):
    check_and_create_file(mvis_events_file, ['Time_stamp', 'Code', 'Component', 'Parameter', 'Status'])
    with open(mvis_events_file, mode='a', newline='') as file:
        parameter = "Good"
        status = 'ok'
        writer = csv.writer(file)
        writer.writerow([time_stamp, code, component, parameter, status])
    print('Record inserted into Mvis_Events')

def insert_into_tblGridview_to_start_train(Code):
    check_and_create_file(gridviewtbl_file, ['Time_Stamp_Gridviewtbl', 'Code'])
    record_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(gridviewtbl_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerow([record_datetime, Code])
    print('Record inserted into Gridviewtbl')

# Example of how to insert a record
# insert_into_tblGridview_to_start_train('78')
# insert_record_into_tblMvis_Events('2024-07-10 12:34:56', 123, 'Active')















'''
import csv
import os
from datetime import datetime
# Define the filenames for the CSV files
mvis_events_file = '/home/jetson/Documents/Mvis_Events.csv'
gridviewtbl_file = '/home/jetson/Documents/Gridviewtbl.csv'

#mvis_events_file = '/mnt/shared/Mvis_Events.csv'
#gridviewtbl_file = '/mnt/shared/Gridviewtbl.csv'

# Check if the CSV files exist and create them with headers if they don't
if not os.path.exists(mvis_events_file):
    with open(mvis_events_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time_stamp', 'Code', 'Component', 'Parameter', 'Status'])
    print('Mvis_Events CSV file created')

if not os.path.exists(gridviewtbl_file):
    with open(gridviewtbl_file, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Time_Stamp_Gridviewtbl', 'Code'])
    print('Gridviewtbl CSV file created')

print('CSV files checked/created')

def insert_record_into_tblMvis_Events(time_stamp, code, component):
    with open(mvis_events_file, mode='a', newline='') as file:
        parameter = "Good"
        status='ok'
        writer = csv.writer(file)
        writer.writerow([time_stamp, code, component, parameter, status])
    print('Record inserted into Mvis_Events')

def insert_into_tblGridview_to_start_train(Code):
    record_datetime=datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    with open(gridviewtbl_file, mode='a', newline='') as file:
        writer = csv.writer(file)
        
        writer.writerow([record_datetime,Code])
    print('Record inserted into Mvis_Events')

# Example of how to insert a record
#insert_into_tblGridview_to_start_train('78')
#insert_record_into_tblMvis_Events('2024-07-10 12:34:56', 123, 'Active')

# No need to close files explicitly since we are using 'with' context manager
'''