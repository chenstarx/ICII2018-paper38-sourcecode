fileNames = ['2018-08-27 2239.txt','2018-08-27 2258.txt']

count = 0
for fileName in fileNames:
    with open(fileName, 'r') as f:
        Data = f.readlines()
        count += len(Data)

print(count)
