from requests import Session
from requests.auth import HTTPBasicAuth
from signalr import Connection

from threading import Thread
import time
import queue
import os
import sys
from datetime import datetime
import SmartOpcUaClient
tclient = None
from gevent import monkey
monkey.patch_all()
import gevent
def main():
    connected = False
    tempQue = queue.Queue(maxsize=100)
    print ("\033c")
    # temp = Pyrometer()
    # #tempQue = Queue.Queue(maxsize=100)
    # def SetConfig(message):
	# 	try:
	# 		cnf = message.split(',',20)
	# 		temp.Pyro1=[]
	# 		for i in range(len(cnf)):
	# 			if(i==0):
	# 				continue
	# 			temp.Pyro1.append( cnf[i])
	# 		print(temp.Pyro1)
	# 	except:
    #
	# 		chat.server.invoke("send", "Raspi","Error in Head Address config")
				
        
    def GetTemptradd(chat):
        while True:
            try:
                c = tempQue.get()

                # if(c):
                #     for p in c:
                #         if (p != ""):
                #             print(p)
                #             d = p.split(',')
                #             dtime = d[2].split(" ")
                #             tempstr ="$"
                #             tempstr =tempstr+ d[0] +"-"+d[1] +"-"+ dtime[0] +"/"+ str(datetime.today().month) +"/"+ str(datetime.today().year) +"/"+ dtime[1] +":"+dtime[2] +":"+ dtime[3] +":"+ dtime[4] +":"+ dtime[5]
                #
                #        #
                #        # for i in range(1): #len(temp.Pyro1)):
                #
                #             # temp.GetTempByAdd(temp.Pyro1[i])
                #             # tempstr = c #tempstr+ "," + temp.line
                chat.server.invoke("send","Raspi", c)
            except:
                   # chat.server.invoke("send", "Raspi","Tm#Pyrometer  HeaderError")
                   print( sys.exc_info()[0])

    
    def GetServerIP():
                with open("ipCofig.txt", "r") as myfile:
                    lines = myfile.readlines()
                    print (lines[0])
                return lines[0]
#     def myfunc(chat):
#
#
#         print("Getting ready...")
#
#         while True:
#             try:
#                     b= raw_input()
#                     time.sleep(0.1)
#                     if b == "q":
#                         print("stopped")
#                         break
#                     else:
#                         chat.server.invoke("send", "Raspi",b)
#                         continue
#             except:
#                   continue
# #
#
    with Session() as session:
        try:
            
            session.auth = HTTPBasicAuth("known", "user")
            time.sleep(30)
            ServerIP = "http://"+ GetServerIP()+ ":8081/signalr"
            connection = Connection(ServerIP, session)#"http://192.168.0.105:8081/signalr", session)
            chat = connection.register_hub('TestHub')
            #start a connection
            #connection.start()
        except:
            print("Error in connection")
            
        
        
        client=SmartOpcUaClient.server()
        SmartOpcUaClient.startThread(client,chat,tempQue)
        tclient = client

        def print_received_message(message):
            try:
                print('received: ',message)
                if(message == 'Raspi:x'):
                    chat.server.invoke("send", "Raspi","s$"+str(datetime.now())+"$")
                if(message == 'Raspi:z'):
                    chat.server.invoke("send", "Raspi","e$"+str(datetime.now())+"$")    
                
                if(message == 'Raspi:y'):
                   tempQue.put("c$"+str(datetime.now())+"$")
                # if('HBD:CONFIG' in message):
                #     SetConfig(message)
                if('HBD:e' in message):   # Train monitoring completed
                    print ("Terminating train..." )
                    SmartOpcUaClient.reset(tclient, 616)
                    print('Train End')
                            
                if('ALIVE' in message):
                   # temp.GetTempByAdd(temp.Pyro1[0])
                    chat.server.invoke("send", "Raspi","YES")
            except:
                print('Error in processing received message',message, sys.exc_info()[0])

        def print_topic(topic, user):
            print('topic: ', topic, user)

        def print_error(error):
            print('error: ', error)
            print("problem in connectinon")
            
        def Disconnect_error():
            print('Trying to exit app...')
            sys.exit()
            os.execv('/home/pi/SmartTBoxScan/chat1.py', [''])

        chat.client.on("addMessage", print_received_message)
      
        chat.client.on("onDisconnect", Disconnect_error)
        connection.error += print_error
        
        # t = Thread(target=myfunc, args=(chat,))
        # t.daemon = True
        # t.start()
        tmpr = Thread(target= GetTemptradd, args=(chat,))
        tmpr.daemon = True
        tmpr.start()
        with connection:
            #a = raw_input()
            chat.server.invoke("send", "Raspi","RASPI CONNECTED")
            
            connection.wait(None)
            
           
                

if __name__ == "__main__":
    main()




