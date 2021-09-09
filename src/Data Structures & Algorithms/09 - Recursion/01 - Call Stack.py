def Func3():
    print("func3")


def Func2():
    Func3()
    print("func2")


def Func1():
    Func2()
    print("func1")


Func1()
