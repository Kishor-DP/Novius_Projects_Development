from subprocess import call
import threading
def openpyfile():
    call(["python", "MVIS_left.py"])
    call(["python", "gridview.py"])
    call(["python", "TestClient copy.py"])

openpyfile()
'''
thread = threading.Thread(target=openpyfile)


thread.start()

thread.join()
'''