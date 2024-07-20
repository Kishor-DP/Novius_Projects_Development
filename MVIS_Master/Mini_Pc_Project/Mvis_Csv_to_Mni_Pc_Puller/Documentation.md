Monitor_Csv.py:-observes latest date modified in Gridviewtbl.csv file
in \\192.168.1.253\Documents\Gridviewtbl.csv gets this file path from config.json
packed in class CodeFetcher:


def get_row_count(self):
used to count rows in Gridviewtbl.csv using pandas read rows


def get_last_mod_time(self):
reads last modified time from jetson time 


def fetch_last_code(self):
last row Code column fetches and saves in last_code.json

def observe_new_row(self, interval=1):
observes new row inserted or not on basis of time of modified

set trigger for subpro.openpyfile() which excute files once every iteration

call(["python", "insert_into_Mvis_Events.py"])
call(["python", "insert_into_Gridviewtbl.py"])
call(["python", "Csv_File_LogRotator.py"])

def convert_mod_time(self, mod_time):
this function is used to convert jetson time format into readable format only