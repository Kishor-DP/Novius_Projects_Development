from subprocess import Popen
import threading
import time
def openpyfile():
    #Popen(["python", "simulateserver.py"])
    time.sleep(2)
    Popen(["python", "main.py"])
    time.sleep(2)
    Popen(["python", "Insert_Into_tblTemperatureLog.py"])
    time.sleep(2)
    Popen(["python", "db_S_sensor.py"])
    time.sleep(2)
    Popen(["python", "coach_type.py"])
openpyfile()
# Running openpyfile in a thread
# thread = threading.Thread(target=openpyfile)
# thread.start()
# thread.join()