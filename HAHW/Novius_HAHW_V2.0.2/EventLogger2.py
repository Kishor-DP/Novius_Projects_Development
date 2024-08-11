#EventLogger2.py
import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
import glob
def setup_logger(logger_name, log_filename, max_bytes=51200, backup_count=100):
    try:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

        handler = RotatingFileHandler(log_filename, maxBytes=max_bytes, backupCount=backup_count)
        handler.setFormatter(formatter)
        handler.addFilter(logging.Filter(name=logger_name))
        handler.addFilter(logging.Filter(name=''))

        logger.addHandler(handler)

        return logger
    except Exception as e:
        print(f"Error setting up logger for {logger_name}: {e}")

def ensure_folder_exists(path):
    if not os.path.exists(path):
        os.makedirs(path)
        print(f"Created folder: {path}")
    else:
        print(f"Folder already exists: {path}")

# Get the current date in the format YYYY-MM-DD
current_date = datetime.now().strftime('%Y-%m-%d')

# Define the paths for app_event and sys_event logs
app_event_folder = './events/app_event'
sys_event_folder = './events/sys_event'

# Ensure the folders exist
ensure_folder_exists(app_event_folder)
ensure_folder_exists(sys_event_folder)

# Set up logger for app_event with maxBytes limit and backupCount
app_event_log_filename = f'{app_event_folder}/app_events_{current_date}.out'
app_event = setup_logger('app_event', app_event_log_filename, max_bytes=51200, backup_count=100)

# Set up logger for sys_event with maxBytes limit and backupCount
sys_event_log_filename = f'{sys_event_folder}/sys_event_{current_date}.out'
sys_event = setup_logger('sys_event', sys_event_log_filename, max_bytes=51200, backup_count=100)

'''
# Log some messages
for i in range(2000):
    app_event.debug('app_event: i = %d' % i)
    sys_event.debug('sys_event: i = %d' % i)

# See what files are created for app_event
app_event_logfiles = glob.glob(f'{app_event_log_filename}*')
print("Files for app_event:")
for filename in app_event_logfiles:
    print(filename)

# See what files are created for sys_event
sys_event_logfiles = glob.glob(f'{sys_event_log_filename}*')
print("\nFiles for sys_event:")
for filename in sys_event_logfiles:
    print(filename)
'''