# MODULE = A file containing code you want to include in your program use 'import' to include a module (built-in or your own)
#          usefull to break up a large program reusable separate files.

#print(help("modules"))

#import math
#import math as m    # The 'm' ats as a nickname, like whenever we call this moduele just 'm' is enough
#from math import e  # Not much recommended

#a, b, c, d = 1, 2, 3, 4

#print (math.e ** a)    # To access each module we can use math."anything of this module"
#print (math.e ** b)
#print (math.e ** c)
#print (math.e ** d)

#pi = 3.14159


# CREATING PERSONAL MODULE : 1. Create this in the same branch as the calling portion and then define the functionality and call it when needed later
#def square(x):
#    return x ** 2

#def cube(x):
#    return x ** 3

#def circumference(radius):
#    return 2 * pi * radius

#def area(radius):
#    return pi * radius ** 2


# 2. Write this in a saperate portion for calling this out.
#import example 
#result = example.pi
#result = example.square(3)

#print (result)