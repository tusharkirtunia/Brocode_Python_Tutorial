#collection = single "variable" used to store multiple values
#  List  = [] An ordered, mutable collection that allows duplicate values.
#  Set   = {} An unordered, mutable collection that does not allow duplicates.
#  Tuple = () An ordered, immutable collection that allows duplicate values.

#In this context, immutable means that once a tuple is created, its elements cannot be changed, added, or removed.


#fruits = ["apple", "banana", "cherry"]

#fruits = {"apple", "banana", "cherry"}

fruits = ("apple", "banana", "cherry")

    #The purpose of the [] is to accommodate as many strings I want.
#print(dir(fruits[2]))
    #We can add [] in print,here the square brackets [] are used to access an element from the list by its index.
    #The dir() function is used to list all the attributes and methods associated with an object.
#print(help(fruits))
#print("apple" in fruits)
    #This statement returns a boolean

#fruits.add("pineapple")
#fruits.remove("apple")

fruits[2] = "Tushar"
    #Lists can be changed, so this updates the value at index 2, in place of cherry there will be banana from now.
for fruit in fruits:
    print(fruit)