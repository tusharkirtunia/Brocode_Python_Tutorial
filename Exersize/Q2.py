# exercise 2 shopping cart program

item = input("What item would you like to buy?: ")
price = float(input("What is the price of the item? "))
quantity = int(input("How many of the items would you like to buy: "))
total = price * quantity

print(f"You bought {quantity} x {item} in total.")
print("The total price is $" + str(total))