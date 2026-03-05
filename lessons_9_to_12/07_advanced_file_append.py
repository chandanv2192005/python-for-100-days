# Appending to an existing file ("a" mode)
with open("shopping_list.txt", "a") as file:
    file.write("Eggs\n")
    file.write("Bread\n")

print("Items appended successfully!")
