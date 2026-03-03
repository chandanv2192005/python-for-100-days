import csv
import random

departments = ["HR", "Engineering", "Sales", "Marketing", "Finance", "Legal"]
first_names = ["Alice", "Bob", "Charlie", "Diana", "Eve", "Frank", "Grace", "Heidi", "Ivan", "Judy", "Mallory", "Victor", "Peggy", "Trent", "Sybil"]
last_names = ["Smith", "Johnson", "Brown", "Ross", "Davis", "Miller", "Wilson", "Moore", "Taylor", "Anderson", "Thomas", "Jackson", "White", "Harris", "Martin"]

def generate_employee_csv(filename):
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["EmployeeID", "Name", "Department", "Salary", "Email"])
        for i in range(1, 101):
            fname = random.choice(first_names)
            lname = random.choice(last_names)
            name = f"{fname} {lname}"
            dept = random.choice(departments)
            salary = random.randint(50000, 150000)
            email = f"{fname.lower()}.{lname.lower()}{i}@example.com"
            writer.writerow([i, name, dept, salary, email])

generate_employee_csv("employees_100.csv")
print("Successfully generated employees_100.csv with 100 records!")
