m = input("Enter the size of array")
arr = []
for i in range(0,m):
    arr.append(input("Enter the element"))

arr1 = list(arr)
arr1.sort()
count = 0
for i in range(0,m):
    if arr[i] != arr1[i]:
        count += 1

if count > 2:
    print "False"
else:
    print "True"