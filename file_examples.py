import os
try:
    file_nmae = "numbers.txt"
    if os.path.exists(file_nmae):
        with open(file_nmae, "r") as file:
            content = file.read()
            print(content)
    else:
        print("File not found!")
except FileNotFoundError:
    print("File not found!")


    