# dictionary =  a collection of {key:value} pairs
#               ordered and changeable. No duplicates

capitals = {"USA": "Washington D.C.",
            "India": "New Delhi",
            "China": "Beijing",
            "Russia": "Moscow"}

#print(capitals.get("USA"))

#if capitals.get("Japan"):
#    print("That capital exists")
#else:
#    print("The capital doesn't exist")

capitals.update({"Germany": "Berlin"})
capitals.update({"France": "Rome"})

print(capitals)
