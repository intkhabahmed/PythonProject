def func1():
    func2()

def func2():
    func1()

try:
    func1()
except RuntimeError:
    print "Stack Overflow Error"
