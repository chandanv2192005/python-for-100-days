import os

filename = "important_data.txt"

# Checking if a file exists before opening
if os.path.exists(filename):
    with open(filename, "r") as file:
        print(file.read())
else:
    print(f"Warning: The file '{filename}' does not exist yet!")
