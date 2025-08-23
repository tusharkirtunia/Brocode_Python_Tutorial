# nested loop = A loop within another loop (outer, inner)
#                   outer loop:
#                       inner loop:

# PROJECT

rows = int(input("Enter the # of the rows: "))
columns = int(input("Enter the # of the columns: "))
symbols = (input("Enter a symbols to use: "))

for x in range(rows):
    for y in range(columns):
        if x == 0 or x == rows - 1 or y == 0 or y == columns - 1:
            print(symbols, end="")
        else:
            print(" ", end="")
    print()