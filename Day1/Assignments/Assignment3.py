for var in range(1,50,1):
    if var%3 == 0 and var%5 ==0:
        print "FizzBuzz"
    elif var%5 == 0:
        print "Buzz"
    elif var%3 == 0:
        print "Fizz"