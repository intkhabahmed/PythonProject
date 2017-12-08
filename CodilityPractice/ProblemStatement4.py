n = input("Enter the no of elements")
arr = []
newDict = dict()
for i in range(0, n):
    arr.insert(i, input("Enter the number"))
    if arr[i] in newDict.keys():
        newDict[arr[i]] += 1
    else:
        newDict.update({arr[i]: 1})

maxOccurence = max(newDict.values())

if maxOccurence > n/2:
    for i in newDict.keys():
        if newDict[i] == maxOccurence:
            print i
            break
else:
    print -1