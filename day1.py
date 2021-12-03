incCount = 0

for i in range(len(data)-1):
    if data[i+1] > data[i]:
        incCount +=1

print("incCount variable is: {}".format(incCount))