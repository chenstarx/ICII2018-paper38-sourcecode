import numpy as np
import matplotlib.pyplot as plt

height = []
time = []

tempHeight = ''
tempHeightLast = ''
tempIndex = ''

fileName = '2018-08-27 2239.txt'


with open(fileName, 'r') as f:
    Data = f.readlines()
    for item in Data:
        item = item.split("; ")
        for items in item:
            items = items.split(": ")
            if (items[0] == "Index"):
                tempIndex = items[1]
            if (items[0] == "Height"):
                tempHeight = items[1]
        
        if tempHeightLast != tempHeight:
            height.append(float(tempHeight))
            time.append(int((int(tempIndex)/187.8) + 0.5))
        
        tempHeightLast = tempHeight


plt.figure()
plt.xlabel('Time(s)')
plt.ylabel('Height(m)')
plt.title('Time (Seconds) - Height (Meters)')
plt.grid(True)
plt.plot(time,height)
plt.show()