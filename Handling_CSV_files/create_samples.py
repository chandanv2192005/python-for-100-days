# create_samples.py — run this FIRST!
# students.csv
with open("students.csv", "w") as f:
    f.write("name,age,grade,subject,city\n")
    f.write("Alice,20,92,Math,Mumbai\n")
    f.write("Bob,22,45,Science,Delhi\n")
    f.write("Carol,21,85,Math,Bangalore\n")
    f.write("David,23,78,Science,Mumbai\n")
    f.write("Emma,20,95,Math,Delhi\n")
    f.write("Frank,22,38,Science,Bangalore\n")
    f.write("Grace,21,88,Math,Mumbai\n")
    f.write("Henry,23,55,Science,Delhi\n")
# sales.csv
with open("sales.csv", "w") as f:
    f.write("date,product,category,quantity,price,city\n")
    f.write("2024-01-15,Laptop,Electronics,2,55000,Mumbai\n")
    f.write("2024-01-16,Phone,Electronics,5,20000,Delhi\n")
    f.write("2024-01-17,Desk,Furniture,1,12000,Bangalore\n")
    f.write("2024-01-18,Laptop,Electronics,3,55000,Mumbai\n")
    f.write("2024-01-19,Chair,Furniture,4,5000,Delhi\n")
    f.write("2024-01-20,Phone,Electronics,2,20000,Bangalore\n")
    f.write("2024-01-21,Tablet,Electronics,6,15000,Mumbai\n")
    f.write("2024-01-22,Desk,Furniture,2,12000,Delhi\n")
# employees.csv
with open("employees.csv", "w") as f:
    f.write("emp_id,name,department,salary,experience,rating\n")
    f.write("E001,Alice Johnson,Engineering,85000,5,4.5\n")
    f.write("E002,Bob Smith,Marketing,60000,3,3.8\n")
    f.write("E003,Carol White,Engineering,92000,7,4.9\n")
    f.write("E004,David Brown,HR,55000,2,3.5\n")
    f.write("E005,Emma Davis,Engineering,78000,4,4.2\n")
    f.write("E006,Frank Miller,Marketing,65000,5,4.0\n")
    f.write("E007,Grace Wilson,HR,52000,1,3.2\n")
    f.write("E008,Henry Moore,Engineering,95000,8,4.8\n")

print("All sample CSV files created!")