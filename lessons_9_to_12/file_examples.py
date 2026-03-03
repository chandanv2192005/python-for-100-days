import os
try:
    file_nmae = "employees_100.csv"
    if os.path.exists(file_nmae):
        with open(file_nmae, "r") as file:
            content = file.readlines()
            n = len(content)-1
            print(f"numbers of employees in the file: {n}")

            for i in range(1, n):
                print(content[i].strip())
    else:
        print("File not found!")
except FileNotFoundError:
    print("File not found!")


    