with open("students.csv", "r") as file:
    lines = file.readlines()

header = lines[0].strip().split(",")

for line in range(1, len(lines)):
    values = lines[line].strip().split(",")#read the line and split it into values
    name = values[0]
    age = int(values[1])
    grade = float(values[2])
    subject = values[3]
    city = values[4]
    print(name, age, grade, subject, city)