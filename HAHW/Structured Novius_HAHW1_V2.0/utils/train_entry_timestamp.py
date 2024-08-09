from datetime import datetime
from utils.event_logger import app_event

def train_entry_timestamp():
    record_datetime = datetime.now().strftime('%Y_%m_%d_%H_%M_%S_2000')
    trainId_as_datetime = f"{record_datetime}"
    app_event.debug("train_entry_timestamp: %s", trainId_as_datetime)
    return trainId_as_datetime
