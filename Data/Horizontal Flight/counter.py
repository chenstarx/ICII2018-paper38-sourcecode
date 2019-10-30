fileNames = ['2018-08-24 1823.txt','2018-08-24 1844.txt','2018-08-24 1906.txt','2018-08-24 2346.txt','2018-08-25 0005.txt','2018-08-26 0010.txt','2018-08-26 0027.txt']

count = 0
for fileName in fileNames:
    with open(fileName, 'r') as f:
        Data = f.readlines()
        count += len(Data)

print(count)
