#Variable = A container for a value (string, integer, float, boolean) 
#           A variable behaves as if it was the value it contains


# Strings

#The purpose of the first_name variable is to store a name (in this case, "Tushar") 
#   that you want to use in the string later.

# These variables hold values that are inserted into the printed messages using f-strings,
#   allowing the output to change dynamically based on the values stored in first_name and food.
first_name = "Tushar"
food = "Kosha mangsho"
instagram_id = "ooftushar"

print (f"Hello, {first_name}")

# Integers 

age = 25
quantity = 2
num_of_students = 20

#Float

price = 10.99
gpa = 3.2
distance = 5.5

#boolean

is_student = False
for_sale = False
is_online = True



    



#The f before the string tells Python to look inside the curly braces {} and 
#     replace that part with the value of the variable first_name.

# In print(f"hello, {first_name}"), 
#     the {} braces are used to put the value of first_name inside the string.