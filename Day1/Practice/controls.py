if(9<8): #comparing 9 and 8
    print("9 is less than 8") #if true then print this statement
else:
    print("9 is greater than 8")#if false then print this statement

for num in range(0,10,2): #start=0, end=10, step=2
    print(num)
    if(num==6):
        break
    else:
        continue
