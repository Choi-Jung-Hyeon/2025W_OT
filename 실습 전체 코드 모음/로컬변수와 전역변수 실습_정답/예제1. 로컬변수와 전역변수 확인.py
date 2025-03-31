a = 100

def f1():
    global a
    print("a:", a)
    a = 200
    print("a:", a)
    
def f2():
    a = 50
    print("a:", 50)    
    
def f3():
    global a
    if a == 100:
        print("Yes! a is 100")
    else:
        print("No! a is not 100")
        a = 100

f1()
f3()
f2()
f3()
a = 100
f3()
