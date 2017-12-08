A = []
n = input("No of elements")

for i in range(0,n):
    A.insert(i,input("Enter the number"))

A.sort()
i = 0
for i in range(0, n):
    if A[i] >= 0:
        break

if i == 0:
    print abs(A[i]+A[i+1])
elif i == n-1:
    print abs(A[n-1]+A[n-2])
else:
    print abs(A[i]+A[i-1])


