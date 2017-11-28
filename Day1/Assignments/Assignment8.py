def fibonacci(no):
    fibonaccis = []
    if no == 0:
        return fibonaccis
    num1 = 1
    num2 = 1
    fibonaccis.append(num1)
    fibonaccis.append(num2)
    for i in range(1,no-1):
        num3 = num1 + num2
        fibonaccis.append(num3)
        num1 = num2
        num2 = num3
    return fibonaccis

num = input("Enter how many fibonacci numbers you want to print")
fibonaccis = fibonacci(num)
print fibonaccis