# Reading a file line by line
print("--- My Shopping List ---")
with open("shopping_list.txt", "r") as file:
    for line in file:
        print(f"- {line.strip()}")
