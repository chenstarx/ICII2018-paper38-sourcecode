import json
import numpy as np
import matplotlib.pyplot as plt

Heights = []
Packs = []
CSQs = []


txtFiles = ['2018-08-21 0245.txt']

for txtFile in txtFiles:
    with open(txtFile, 'r') as f:
        tempHeight = ''
        tempCSQ = ''
        height = []
        csq = []
        pack = []
        Data = f.readlines()
        for item in Data:
            item = item.split("; ")
            for items in item:
                items = items.split(": ")
                if (items[0] == "Height"):
                    tempHeight = float(items[1])
                if (items[0] == "CSQ"):
                    tempCSQ = float(items[1])
                    
            if tempHeight not in height:
                height.append(tempHeight)
                csq.append(tempCSQ)
                pack.append(1)
            else:
                pack[height.index(tempHeight)] += 1
                csq[height.index(tempHeight)] += tempCSQ

        for item in height:
            newHeight = int((item + 2.5) / 5) * 5

            if newHeight not in Heights:
                Heights.append(newHeight)
                Packs.append(pack[height.index(item)])
                CSQs.append(csq[height.index(item)])
            else:
                Packs[Heights.index(newHeight)] += pack[height.index(item)]
                CSQs[Heights.index(newHeight)] += csq[height.index(item)]

RSRPs = []
for item in CSQs:
    rsrp = item / Packs[CSQs.index(item)]
    RSRPs.append(rsrp)
    
plt.figure()
plt.xlabel('Height(m)')
plt.ylabel('RSRP(dBm)')
plt.title('Height(m) - RSRP(dBm)')
plt.grid(True)
plt.plot(Heights,RSRPs)
plt.show()
