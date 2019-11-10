import time
import socket
import datetime
import threading
from pymongo import MongoClient

client = MongoClient()

host = "0.0.0.0"
port = 7671

class myThread (threading.Thread):
    def __init__(self, data, time):
        threading.Thread.__init__(self)
        self.time = time
        self.data = data.decode('utf-8')
        
    def run(self):
        try:
            # print(self.data)
            # print(self.time)

            rawData = self.data.split("\r\n")
            rawData.pop()

            for dataItem in rawData:
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

                if (("Time" in dbData) and ("CSQ" in dbData) and ("Index" in dbData) and ("Height" in dbData)):
                    mongo = client.surf
                    table = mongo[self.time]
                    table.insert_one(dbData)
            
        except Exception as err:
            print(err)

udps = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

udps.bind((host,port))

lastAddr = ''

while True:
    data, addr = udps.recvfrom(8192)

    if addr != lastAddr:
        dt = datetime.datetime.now()
        currentTime = dt.strftime('%m-%d %H:%M') + " UDP"
    lastAddr = addr

    newThread = myThread(data, currentTime)

    newThread.start()

udps.close()
