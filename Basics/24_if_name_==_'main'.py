# if __name__ == __main__ :(this scripts can be imported OR run standalone)
#                   Function and classes in the module can be reused
#                   without the main block of code excuting 
# It's a Good practice because - 1. Code is Modular
#                                2. Helps readability
#                                3. Leaves no global variables
#                                4. Avoid unintented execution

#  example - library = Import library for functionallity
#                 When running library directly, display a help page



# For this particular leason create folder containing 2 different .py files, and make them interlinked 

# In script1.py

def favorite_food(food):
    print(f"Your favorite food is {food}")

def main():
    print("This is script1")
    favorite_food("Pizza")
    print("Goodbye")

if __name__ == '__main__':
    main()


# In script2.py

#from script1 import *

def favorite_drink(drink):
    print(f"Your favorite drink is {drink}")

def main():
    print("This is script2")
    favorite_food("Biriwani")
    favorite_drink("Lassi")
    print("Goodbye! ")

if __name__=='__main__':
    main()

