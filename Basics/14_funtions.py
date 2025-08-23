 # function = A block of reusable code and executed only when it is called.
#            place () after the function name ti invoke it

#def happy_birthday(name, age):
#    print(f"Happy birthday to {name}")
#    print(f"You are old {age} years old")

#happy_birthday("tushar", 20)

#def display_invoice(username, amount, due_date):
#    print(f"hello {username}")
#    print(f"Your bill amount of {amount:.2f} is due {due_date}")

#display_invoice("Tushar", 24.24, "01/01")




# return = statement used to ed a function
#          and send a result back to the caller

def add(a, b):
    z = a + b
    return z

def sub(a, b):
    z = a - b
    return z

def mul(a, b):
    z = a * b
    return z

def div(a, b):
    z = a / b
    return z

print(add(1,2))
print(sub(1,2))
print(mul(1,2))
print(div(1,2))