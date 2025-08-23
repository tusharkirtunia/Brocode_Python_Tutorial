# keyword arguments = an argument preceded by an identifier
#                     helps with readability
#                     order of argument doesn't matter
#                     1. position, 2. default, 3. KEYWORD, 4. arbitrary

#def hello(greeting, title, first, last):
#    print(f"{greeting} {title}{first} {last}")

#hello("Hello", "Mr.","Tushar", "Kirtunia")

#for x in range(1, 11):
#    print(x, end=" ") #end here is a keyword argument

def get_phone(country, area, first, last):
    return f"{country}-{area}-{first}-{last}"

phone_num =  get_phone('91', '123', '456', '1891')

print(phone_num)