import json
import numpy as np
import matplotlib.pyplot as plt

txtHeights = []
txtPacks = []

jsonHeights = []
jsonPacks = []

txtFiles = ['2018-08-27 2239.txt','2018-08-27 2258.txt']
jsonFiles = ['08-27 2238.json','08-27 2258.json']

for txtFile in txtFiles:
    with open(txtFile, 'r') as f:
        tempHeight = ''
        height = []
        packs = []
        Data = f.readlines()
        for item in Data:
            item = item.split("; ")
            for items in item:
                items = items.split(": ")
                if (items[0] == "Height"):
                    tempHeight = float(items[1])
                    
            if tempHeight not in height:
                height.append(tempHeight)
                packs.append(1)
            else:
                packs[height.index(tempHeight)] += 1

        for item in height:
            newHeight = int((item + 5) / 10) * 10

            if newHeight not in txtHeights:
                txtHeights.append(newHeight)
                txtPacks.append(packs[height.index(item)])
            else:
                txtPacks[txtHeights.index(newHeight)] += packs[height.index(item)]

for jsonFile in jsonFiles:
    with open(jsonFile, 'r') as f:
        tempHeight = ''
        height = []
        packs = []
        Data = json.loads(f.read())
        for item in Data:
            if "Height" in item:
                tempHeight = float(item["Height"])
                    
            if tempHeight not in height:
                height.append(tempHeight)
                packs.append(1)
            else:
                packs[height.index(tempHeight)] += 1
                
        for item in height:
            newHeight = int((item + 5) / 10) * 10

            if newHeight not in jsonHeights:
                jsonHeights.append(newHeight)
                jsonPacks.append(packs[height.index(item)])
            else:
                jsonPacks[jsonHeights.index(newHeight)] += packs[height.index(item)]

lossRates = []
for item in txtPacks:
    lossPack = item - jsonPacks[txtPacks.index(item)]
    lossRate = lossPack / item
    lossRates.append(100*lossRate)

plt.figure()
plt.xlabel('Height')
plt.ylabel('Packet Loss Rate')
plt.title('Height (Meters) - Packet Loss Rate (Percent)')
plt.grid(True)
plt.plot(txtHeights,lossRates)
plt.show()