n = input("Enter the no of elements of A and B")
A = []
B = []
print("Elements of A")
for i in range(0,n):
    A.insert(i,input("Enter the number"))

print("Elements of B")
for p in range(0,n):
    B.insert(p,input("Enter the number"))

C = []
for j in range(0,n):
    C.append(A[j] + (float(B[j])/1000000))

count = 0
for k in range(0,n):
    for l in range(0,n):
        if C[k]*C[l] >= C[k]+C[l] and k<l:
            count += 1

if count > 100000000:
    print(100000000)
else:
    print count