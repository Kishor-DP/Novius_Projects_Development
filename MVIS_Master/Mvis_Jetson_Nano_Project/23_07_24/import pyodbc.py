import pyodbc


def Connect_to_db(intTempLogId, intTrainId):
    
    print("connect:",intTempLogId, intTrainId)

def write_tblTemperatureLog( intTempLogId, intTrainId):
    print( "write:",intTempLogId, intTrainId)

######################################################################################################################

intTempLogId="hjjhjjgkj" 
intTrainId="111111"
Connect_to_db(intTempLogId, intTrainId)
write_tblTemperatureLog( intTempLogId, intTrainId)
