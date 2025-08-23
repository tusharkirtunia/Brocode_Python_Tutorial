
groceries = [["","apple", "banana", "cherry"],
             ["","celery", "carrots", "potatoes"],
             ["","chicken", "fish", "turkey"]]

for collection in groceries:
    for food in collection:
        print(food, end=" ")
    print()