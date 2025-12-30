# VARIABLE SCOPE = Where a variable is visible and accessible
# SCOPE RESOLUTION = (LEGB) Local -> Enclosed -> Global -> Built-in


# LOCAL

#def func1():
#    x=1

#def func2():
#    x=2
#    print(x)

#func1()
#func2()


# ENCLOSED

#def func1():
#    x = 1
#    def func2():
#        x = 2
#        print(x)
#    func2()

#func1()


# GLOBAL - Outside of any functions, only used when there is no local or enclosed version to be used 

#def func1():
#    print(x)

#def func2():
#    print(x)

#x = 3

#func1()
#func2()


# BUILT-IN

from math import e

def func1():
    print(e)

e = 3

func1()




