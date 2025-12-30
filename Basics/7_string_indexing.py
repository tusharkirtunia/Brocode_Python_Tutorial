# indexing = accessing elements of a sequence using [] (indexing operator)
#            [start : end : step]

roll_number = "abc-123-456-789"

# print(roll_number[0])    # prints the 1st character
# print(roll_number[:4])   # prints everything before the 5th character i.e. "abc-"
# print(roll_number[5:9])  # prints everything between 5th and 10th character i.e. "23-4"
# print(roll_number[5:])   # prints everything after 5th character i.e. "23-456-789"
# print(roll_number[-1])   # prints everything from the back side i.e. "9"

# print(roll_number[::2])  # prints every 2nd character i.e. "ac134679"

last_digit = roll_number[-3:]
print(f"XXX-XXX-XXX-{last_digit}")


# NORMAL INDEXING

# index operator [] = gives to a sequence's element (str, list, tuples)

name =  "tushar Kirtunia!"

#if (name[0].islower()):
#    name = name.capitalize()

first_name = name[0:3].upper() # [0:3]--Starting position : Ending position
last_name = name[4:].lower()
last_character = name[-1]

print(first_name)
print(last_name)
print(last_character)