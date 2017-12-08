n = input("Enter the no of elements")
arr = list()

for i in range(0,n):
    arr.insert(i,input("Enter the element"))

depth = 0
p = 0
q = -1
r = -1
for i in range(0, n-1):

    if q < 0 and arr[i] <= arr[i+1]:
        print "first if", arr[i], arr[i+1], q, i
        q = i

    if q >= 0 and (arr[i] >= arr[i+1] or i + 2 == len(arr)):
        if arr[i] >= arr[i+1]:
            print "second if", arr[i], arr[i + 1], r, i
            r = i
        else:
            print "second else", arr[i], arr[i + 1], r, i+1
            r = i+1
        depth = max(depth, min((arr[p]-arr[q]),(arr[r]-arr[q])))
        print depth
        p = i
        q = r = -1
print depth