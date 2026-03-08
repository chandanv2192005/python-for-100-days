import csv
with open("students.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        # Access by column name — no index guessing!
        name = row["name"]
        grade = float(row["grade"])
        subject = row["subject"]
        city = row["city"]
        status = "Pass" if grade >= 50 else "Fail"
        print(f"{name:<10} {subject:<10} {grade:<6} {status}")
# Load ALL rows into a list at once
with open("students.csv", "r") as file:
    all_students = list(csv.DictReader(file))

print(f"Total: {len(all_students)} students")
print(f"First: {all_students[0]}")
print(f"Last: {all_students[-1]}")