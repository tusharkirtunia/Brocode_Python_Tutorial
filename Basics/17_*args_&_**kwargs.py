# *args         = allows you to pass multiple non-key arguments
# **kwargs      = allows you to pass multiple keyword-arguments
#               * unpacking operator
#               1. positional 2. default 3. keyword 4. ARBITRARY



#               *args

#def add(*args):
#    total = 0
#    for agr in args:
#        total += agr
#    return total

#print(add(1, 15))

#def display_name(*args):
#    for agr in args:
#        print(agr, end=" ")

#display_name("Tushar","Kirtunia")


#               **kwargs

#def print_address(**kwargs):
#    for key, value in kwargs.items():
#        print(f"{key}: {value}")

#print_address(House_no="B-17/71",
#              city="Kalyani",
#              state="West bengal",
#              pin="741235")


def shipping_label(*args, **kwargs):
        for arg in args:
            print(arg, end=" ")
        print()

        if "apt" in kwargs:
            print(f"{kwargs.get('House_no')} {kwargs.get('apt')}")
        else:
            print(f"{kwargs.get('House_no')}")

        print(f"{kwargs.get('city')} {kwargs.get('state')} {kwargs.get('pin')}")

shipping_label("Dr.", "Tushar", "Kirtunia",
                House_no="B-17/71",w
                city="Kalyani",
                state="West bengal",
                pin="741235")
