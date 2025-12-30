#while loop = execute some code WHILE some condition remains true
#while Loop
#	•	The while loop is a type of conditional loop in Python.
#	•	It repeatedly executes the code inside its block as long as the condition is True.

#name = input("Enter your name: ")

#while name == "":
#    print("You did not enter a name")
#    name = input("Enter your name: ")

#print(f"Hello {name}")


age = int(input("Enter your age: "))

while age < 0:
    print("Age cannot be negative")
    age = int(input("Enter your age: "))

print(f"You are {age} years old")


# LOGICAL OPERATORS
#food = input("Enter a food u like (q to quite): ")

#while not food == "q":

# not Operator
# 	•	The not operator inverts the result of the condition.
# 	•	If food == "q" evaluates to True, not turns it into False.
# 	•	If food == "q" evaluates to False, not turns it into True.
#             OR
#while food != "q": # does same thing as while not operator but in a sophisticated way
#    print(f"You like {food}")
#    food = input("Enter another food you like (q to quite): ")

#print("bye")


#    OR function
#num = int(input("Enter a # between 1 - 10: "))

#while num < 1 or num > 10:
#    print(f"{num} is not valid")
#    num = int(input("Enter a # between 1 - 10:"))

#print(f"Your number is {num}")
