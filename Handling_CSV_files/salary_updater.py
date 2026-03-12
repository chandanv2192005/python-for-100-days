import csv

updated_rows = []

with open("employees_02.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row["Salary"])
        row["Salary"] = int(row["Salary"]) + 5000
        updated_rows.append(row)

with open("updated_employee_02.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["Name", "JobTitle", "Salary"])
    writer.writeheader()
    for row in updated_rows:
        writer.writerow(row)