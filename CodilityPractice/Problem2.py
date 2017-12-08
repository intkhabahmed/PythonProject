n = input("Enter the no of elements")
arr = list()

for i in range(0,n):
    arr.insert(i,input("Enter the element"))

arr1 = list()
k = 0
for i in range(0,n):
    arr1.append(arr[k])
    k = arr[k]
    if k == -1:
        break

print len(arr1)