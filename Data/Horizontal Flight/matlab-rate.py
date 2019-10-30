import json

cords = []
counts = []

latiTemp = ''
longTemp = ''

mLati = 0
mLong = 0
sLati = 180
sLong = 180

hRange = [40, 50] #Height Rage
txtFiles = ['2018-08-24 1823.txt','2018-08-24 1844.txt','2018-08-24 1906.txt','2018-08-24 2346.txt','2018-08-25 0005.txt','2018-08-26 0010.txt','2018-08-26 0027.txt']
jsonFiles = ['08-24 1823.json','08-24 1844.json','08-24 1905.json','08-24 2346.json','08-25 0005.json','08-26 0010.json','08-26 0027.json']


for txtFile in txtFiles:
    with open(txtFile, 'r') as f:
        Data = f.readlines()
        for item in Data:
            item = item.split("; ")
            for items in item:
                items = items.split(": ")
                if (items[0] == "Lati"):
                    latiTemp = items[1]
                if (items[0] == "Long"):
                    longTemp = items[1]
                if (items[0] == "Height"):
                    heightTemp = items[1]
            
            if (float(heightTemp) > hRange[0] and float(heightTemp) < hRange[1]):
                cord = latiTemp + "," + longTemp
                if cord in cords:
                    counts[cords.index(cord)] += 1
                else:
                    cords.append(cord)
                    counts.append(1)

        f.close()

latitude = []
longitude = []

points = []
for item in cords:
    item = item.split(",")
    latitude.append(float(item[0]))
    longitude.append(float(item[1]))
    point = {}
    point["latitude"] = float(item[0])
    point["longitude"] = float(item[1])
    points.append(point)

mLati = 31.27578652
sLati = 31.27395652
mLong = 120.7376832
sLong = 120.7355832

latiIncre = (mLati - sLati) / 8
longIncre = (mLong - sLong) / 8

lati1 = sLati + 0.5 * latiIncre
lati2 = sLati + 1.5 * latiIncre
lati3 = sLati + 2.5 * latiIncre
lati4 = sLati + 3.5 * latiIncre
lati5 = sLati + 4.5 * latiIncre
lati6 = sLati + 5.5 * latiIncre
lati7 = sLati + 6.5 * latiIncre
lati8 = sLati + 7.5 * latiIncre

latiA = sLati + latiIncre
latiB = sLati + 2 * latiIncre
latiC = sLati + 3 * latiIncre
latiD = sLati + 4 * latiIncre
latiE = sLati + 5 * latiIncre
latiF = sLati + 6 * latiIncre
latiG = sLati + 7 * latiIncre


long1 = sLong + 0.5 * longIncre
long2 = sLong + 1.5 * longIncre
long3 = sLong + 2.5 * longIncre
long4 = sLong + 3.5 * longIncre
long5 = sLong + 4.5 * longIncre
long6 = sLong + 5.5 * longIncre
long7 = sLong + 6.5 * longIncre
long8 = sLong + 7.5 * longIncre

longA = sLong + longIncre
longB = sLong + 2 * longIncre
longC = sLong + 3 * longIncre
longD = sLong + 4 * longIncre
longE = sLong + 5 * longIncre
longF = sLong + 6 * longIncre
longG = sLong + 7 * longIncre

txtCounts = []
txtPoints = []
txtCSQs = []
for item in points:
    txtPoint = {}
    if item["latitude"] <= lati1:
        txtPoint["latitude"] = sLati
    if item["latitude"] > lati1 and item["latitude"] <= lati2:
        txtPoint["latitude"] = latiA
    if item["latitude"] > lati2 and item["latitude"] <= lati3:
        txtPoint["latitude"] = latiB
    if item["latitude"] > lati3 and item["latitude"] <= lati4:
        txtPoint["latitude"] = latiC
    if item["latitude"] > lati4 and item["latitude"] <= lati5:
        txtPoint["latitude"] = latiD
    if item["latitude"] > lati5 and item["latitude"] <= lati6:
        txtPoint["latitude"] = latiE
    if item["latitude"] > lati6 and item["latitude"] <= lati7:
        txtPoint["latitude"] = latiF
    if item["latitude"] > lati7 and item["latitude"] <= lati8:
        txtPoint["latitude"] = latiG
    if item["latitude"] > lati8:
        txtPoint["latitude"] = mLati

    if item["longitude"] <= long1:
        txtPoint["longitude"] = sLong
    if item["longitude"] > long1 and item["longitude"] <= long2:
        txtPoint["longitude"] = longA
    if item["longitude"] > long2 and item["longitude"] <= long3:
        txtPoint["longitude"] = longB
    if item["longitude"] > long3 and item["longitude"] <= long4:
        txtPoint["longitude"] = longC
    if item["longitude"] > long4 and item["longitude"] <= long5:
        txtPoint["longitude"] = longD
    if item["longitude"] > long5 and item["longitude"] <= long6:
        txtPoint["longitude"] = longE
    if item["longitude"] > long6 and item["longitude"] <= long7:
        txtPoint["longitude"] = longF
    if item["longitude"] > long7 and item["longitude"] <= long8:
        txtPoint["longitude"] = longG
    if item["longitude"] > long8:
        txtPoint["longitude"] = mLong

    if txtPoint in txtPoints:
        txtCounts[txtPoints.index(txtPoint)] += counts[points.index(item)]
    else:
        txtPoints.append(txtPoint)
        txtCounts.append(counts[points.index(item)])

cords = []
counts = []

latiTemp = ''
longTemp = ''

for jsonFile in jsonFiles:
    with open(jsonFile, 'r') as f:
        Data = json.loads(f.read())
        for item in Data:
            try:
                latiTemp = item["Latitude"]
                longTemp = item["Longitude"]
                heightTemp = item["Height"]
            except Exception as e:
                print(e)
            cord = latiTemp + "," + longTemp
            if (float(heightTemp) > hRange[0] and float(heightTemp) < hRange[1]):
                if cord in cords:
                    counts[cords.index(cord)] += 1
                else:
                    cords.append(cord)
                    counts.append(1)

points = []
for item in cords:
    item = item.split(",")
    latitude.append(float(item[0]))
    longitude.append(float(item[1]))
    point = {}
    point["latitude"] = float(item[0])
    point["longitude"] = float(item[1])
    points.append(point)


jsonCounts = []
jsonPoints = []
for item in points:
    jsonPoint = {}
    if item["latitude"] <= lati1:
        jsonPoint["latitude"] = sLati
    if item["latitude"] > lati1 and item["latitude"] <= lati2:
        jsonPoint["latitude"] = latiA
    if item["latitude"] > lati2 and item["latitude"] <= lati3:
        jsonPoint["latitude"] = latiB
    if item["latitude"] > lati3 and item["latitude"] <= lati4:
        jsonPoint["latitude"] = latiC
    if item["latitude"] > lati4 and item["latitude"] <= lati5:
        jsonPoint["latitude"] = latiD
    if item["latitude"] > lati5 and item["latitude"] <= lati6:
        jsonPoint["latitude"] = latiE
    if item["latitude"] > lati6 and item["latitude"] <= lati7:
        jsonPoint["latitude"] = latiF
    if item["latitude"] > lati7 and item["latitude"] <= lati8:
        jsonPoint["latitude"] = latiG
    if item["latitude"] > lati8:
        jsonPoint["latitude"] = mLati

    if item["longitude"] <= long1:
        jsonPoint["longitude"] = sLong
    if item["longitude"] > long1 and item["longitude"] <= long2:
        jsonPoint["longitude"] = longA
    if item["longitude"] > long2 and item["longitude"] <= long3:
        jsonPoint["longitude"] = longB
    if item["longitude"] > long3 and item["longitude"] <= long4:
        jsonPoint["longitude"] = longC
    if item["longitude"] > long4 and item["longitude"] <= long5:
        jsonPoint["longitude"] = longD
    if item["longitude"] > long5 and item["longitude"] <= long6:
        jsonPoint["longitude"] = longE
    if item["longitude"] > long6 and item["longitude"] <= long7:
        jsonPoint["longitude"] = longF
    if item["longitude"] > long7 and item["longitude"] <= long8:
        jsonPoint["longitude"] = longG
    if item["longitude"] > long8:
        jsonPoint["longitude"] = mLong

    if jsonPoint in jsonPoints:
        jsonCounts[jsonPoints.index(jsonPoint)] += counts[points.index(item)]
    else:
        jsonPoints.append(jsonPoint)
        jsonCounts.append(counts[points.index(item)])
            
latitude = []
longitude = []

for item in txtPoints:
    latitude.append(item["latitude"])
    longitude.append(item["longitude"])

rates = []
print(txtCounts)
print(jsonCounts)
for item in txtCounts:
    loss = item - jsonCounts[txtCounts.index(item)]
    rate = loss / item
    rates.append(100*rate)

print(len(rates))

with open('rate.txt', 'w') as f:
    f.write(str(rates).replace("'",'').replace('[','').replace(']','').replace(', ',' '))
    f.close()
with open('long-rate.txt', 'w') as f:
    f.write(str(longitude).replace("'",'').replace('[','').replace(']','').replace(', ',' '))
    f.close()
with open('lat-rate.txt', 'w') as f:
    f.write(str(latitude).replace("'",'').replace('[','').replace(']','').replace(', ',' '))
    f.close()

