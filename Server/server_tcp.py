import time
import socket
import datetime
import threading
from pymongo import MongoClient

client = MongoClient()

host = "0.0.0.0"
port = 7670

Latitude = ""
Longitude = ""
Temperature = ""
Height = ""
dataTemp = ""
dataFlag = False

isModule = False

class myThread (threading.Thread):
    def __init__(self, socketInstance, time):
        threading.Thread.__init__(self)
        self.time = time
        self.mySocket = socketInstance
        self.mySocket.settimeout(120)
        
    def run(self):
        
        while True:
            global Latitude
            global Longitude
            global Temperature
            global Height
            global dataTemp
            global dataFlag
            
            try:
                rawData = self.mySocket.recv(8192).decode()

                From = rawData.replace(";",":").split(": ")

                if "Phone" in From:

                    rawData = rawData.split("\r\n")

                    for dataItem in rawData:

                        if dataItem != "":

                            if dataFlag:
                                dataItem = dataTemp + dataItem
                                dataTemp = ""
                                dataFlag = False

                            print(dataItem)
                            
                            data = dataItem.split("; ")

                            dbData = {}

                            for item in data:
                                if item != "":
                                    items = item.split(": ")
                                    if (len(items) == 2 and items[1] != ""):
                                        if (items[0] == "Time"):
                                            dbData['Time'] = items[1]
                                        if (items[0] == "CSQ"):
                                            dbData['CSQ'] = items[1]
                                        if (items[0] == "Index"):
                                            dbData['Index'] = items[1]
                                        if (items[0] == "Height"):
                                            dbData['Height'] = items[1]
                                        if (items[0] == "Lati"):
                                            dbData['Latitude'] = items[1]
                                        if (items[0] == "Long"):
                                            dbData['Longitude'] = items[1]

                            if Latitude != "":
                                dbData['Latitude'] = Latitude
                            if Longitude != "":
                                dbData['Longitude'] = Longitude
                            if Temperature != "":
                                dbData['Temperature'] = Temperature
                            if Height != "":
                                dbData['Height'] = Height

                            if (("Time" in dbData) and ("CSQ" in dbData) and ("Index" in dbData) and ("Height" in dbData)):
                                mongo = client.surf
                                table = mongo[self.time]
                                table.insert_one(dbData)
                            else:
                                dataTemp = dataItem
                                dataFlag = True
                            
                if "Module" in From:

                    isModule = True

                    data = rawData.split("; ")

                    for item in data:

                        items = item.split(": ")

                        if len(items) == 2:

                            if (items[0] == "Latitude" and items[1] != ""):
                                Latitude = items[1]

                            if (items[0] == "Longitude" and items[1] != ""):
                                Longitude = items[1]

                            if (items[0] == "Temperature" and items[1] != ""):
                                Temperature = items[1]

                            if (items[0] == "Height" and items[1] != ""):
                                Height = items[1]

                if rawData == "":
                    self.mySocket.shutdown(2)
                    self.mySocket.close()
                    print("Connection Ended by Client\n")
                    break
                
            except Exception as err:
                self.mySocket.shutdown(2)
                self.mySocket.close()
                print(err)
                break

                
tcps = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

tcps.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1)

tcps.bind((host,port))

tcps.listen(1)

while True:
    print("Waiting for incoming connections\n")
    conn, addr = tcps.accept()

    dt = datetime.datetime.now()
    currentTime = dt.strftime('%m-%d %H:%M')
    
    print("incoming connection from: ", addr,"\n")
    newThread = myThread(conn, currentTime)
    newThread.start()
    
