import csv
with open("students.csv", "r") as file:
    reader = csv.reader(file)
    header = next(reader) # skip header row
    print("Header:", header)
    for row in reader:
        name, age, grade, subject, city = row
        print(f"{name} from {city} — Grade: {grade}")