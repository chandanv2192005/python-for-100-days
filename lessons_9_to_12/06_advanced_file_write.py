# Writing to a file (creates it if it doesn't exist, overwrites if it does)
with open("shopping_list.txt", "w") as file:
    file.write("Apples\n")
    file.write("Bananas\n")
    file.write("Milk\n")

print("File written successfully using 'with' statement!")
