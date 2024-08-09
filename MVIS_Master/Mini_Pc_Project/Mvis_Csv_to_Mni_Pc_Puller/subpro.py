from subprocess import call
import threading
import time
def openpyfile():
    #call(["python", "TrainTransaction.py"])
    time.sleep(60)
    call(["python", "insert_into_Mvis_Events.py"])
    call(["python", "insert_into_Gridviewtbl.py"])
    call(["python", "Csv_File_LogRotator.py"])

#openpyfile()
'''
thread = threading.Thread(target=openpyfile)


thread.start()

thread.join()
'''