import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime

def setup_logger(logger_name, log_filename, max_bytes=51200, backup_count=100):
    try:
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        handler = RotatingFileHandler(log_filename, maxBytes=max_bytes, backupCount=backup_count)
        handler.setFormatter(formatter)
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

current_date = datetime.now().strftime('%Y-%m-%d')

app_event_folder = './events/app_event'
sys_event_folder = './events/sys_event'

ensure_folder_exists(app_event_folder)
ensure_folder_exists(sys_event_folder)

app_event_log_filename = f'{app_event_folder}/app_events_{current_date}.out'
app_event = setup_logger('app_event', app_event_log_filename, max_bytes=51200, backup_count=100)

sys_event_log_filename = f'{sys_event_folder}/sys_event_{current_date}.out'
sys_event = setup_logger('sys_event', sys_event_log_filename, max_bytes=51200, backup_count=100)
