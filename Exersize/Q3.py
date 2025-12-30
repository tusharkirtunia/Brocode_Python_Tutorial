# Validate user input exercise
# 1. username is no more than 12 characters
# 2. username must not contain spaces
# 3. username must not contain digits

username = input("Enter a username: ")

if len(username) > 12:
    #Check if the username is too long
    print("Your username can't be longer than 12 characters.")
elif not username.find(" ") == -1:
    #Check if the username is empty (contains only spaces)
    print ("Your username can't be empty.")
elif not username.isalpha():
    #Check if the username contains digits
    print ("Your username can't contain any digits.")
else:
    print(f"Welcome {username}")