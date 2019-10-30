cords = []
csqs = []
counts = []

latiTemp = ''
longTemp = ''
csqTemp = ''
heightTemp = ''

count = 0

hRange = [40, 50] #高度范围
fileNames = ['2018-08-24 1823.txt','2018-08-24 1844.txt','2018-08-24 1906.txt','2018-08-24 2346.txt','2018-08-25 0005.txt','2018-08-26 0010.txt','2018-08-26 0027.txt']

for fileName in fileNames:
    with open(fileName, 'r') as f:
        Data = f.readlines()
        for item in Data:
            item = item.split("; ")
            for items in item:
                items = items.split(": ")
                if (items[0] == "CSQ"):
                    csqTemp = int(items[1])
                if (items[0] == "Lati"):
                    latiTemp = items[1]
                if (items[0] == "Long"):
                    longTemp = items[1]
                if (items[0] == "Height"):
                    heightTemp = items[1]

            if (float(heightTemp) > hRange[0] and float(heightTemp) < hRange[1]):
                cord = latiTemp + "," + longTemp
                if cord in cords:
                    csqs[cords.index(cord)] += csqTemp
                    counts[cords.index(cord)] += 1
                else:
                    cords.append(cord)
                    csqs.append(csqTemp)
                    counts.append(1)

        f.close()

latitude = []
longitude = []
csq = []

count = 0
for item in csqs:
    item = item/counts[count]
    csq.append('%.2f' % item)
    count += 1

for item in cords:
    item = item.split(",")
    latitude.append(item[0])
    longitude.append(item[1])

print(latitude)
print(longitude)
print(csq)


with open('csq-raw.txt', 'w') as f:
    f.write(str(csq).replace("'",'').replace('[','').replace(']','').replace(', ',' '))
    f.close()
with open('long-raw.txt', 'w') as f:
    f.write(str(longitude).replace("'",'').replace('[','').replace(']','').replace(', ',' '))
    f.close()
with open('lat-raw.txt', 'w') as f:
    f.write(str(latitude).replace("'",'').replace('[','').replace(']','').replace(', ',' '))
    f.close()
