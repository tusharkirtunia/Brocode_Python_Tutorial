# List comprehension = A concise way to create lists in python
#                      compact and easier to read than traditional loops
#          Formula  =  [expression for valuable in iterable if condition]

#doubles = []
#for s in range(1, 11):
#    doubles.append(x * 2)

#print(doubles)

#The above is lot to write rather we can use a list comprehension

#doubles = [x * 2 for x in range(1, 11)] #consise way to create list in python
#triples = [y * 3 for y in range(1, 11)] 
#squares = [z * z for z in range(1, 11)]

#print (doubles)
#print (triples)
#print (squares)

# WORKING WITH STRINGS :

#fruits = ["apple", "orange", "banana", "coconut"]
#fruits = [fruit.upper() for fruit in fruits] #This line is for making all the elements of the list in uppercas
#fruit_chars = [fruit[0] for fruit in fruits] #This returns the first character of the element of the string : ['a', 'o', 'b', 'c']
#print(fruit_chars)

# WORKING WITH CONDITIONS :

#numbers = [1, -2, 3, -4, 5, -6]
#positive_nums = [num for num in numbers if num >= 0] #Gives the output for only positive numbers 
#nagetive_nums = [num for num in numbers if num <= 0] #Gives the output for only nagetive numbers 
#even_nums = [num for num in numbers if num % 2 == 0] #Gives only the even nos. as output 
#odd_nums = [num for num in numbers if num % 2 == 1] #Gives only the odd nos. as output 

#print(positive_nums)
#print(nagetive_nums)
#print(even_nums)
#print(odd_nums)


# LAST EXERSIZE 

grades = [85, 42, 79, 56, 61, 30]
passing_gardes  = [grade for grade in grades if grade >= 60]

print(passing_gardes)
