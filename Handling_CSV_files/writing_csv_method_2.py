import csv

# Data as a list of dictionaries
employees_to_add = [
    {"emp_id": "E009", "name": "Ian Wright", "department": "Finance", "salary": 72000, "experience": 3, "rating": 4.1},
    {"emp_id": "E010", "name": "Jane Adams", "department": "IT", "salary": 88000, "experience": 6, "rating": 4.6},
]

# Writing dictionaries to a CSV
with open("new_employees.csv", "w", newline="") as file:
    # Defining the header columns
    fieldnames = ["emp_id", "name", "department", "salary", "experience", "rating"]
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    # Write the header first
    writer.writeheader()
    
    # Write the rows dict by dict
    writer.writerows(employees_to_add)

print("Status: Successfully created new_employees.csv using DictWriter.")
