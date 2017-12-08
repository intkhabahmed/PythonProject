n = input("No of elements")
A = []
for i in range(0,n):
    A.insert(i,input("Enter the element"))

count = 0
A.sort()
for i in range(0, n):
    for j in range(0, n):
        if A[i] == A[j] and i<j:
            count += 1

print count