import csv

# Append a single row to an existing file
new_sales_record = ["2024-01-23", "Monitor", "Electronics", "3", "30000", "Chennai"]

# Notice the 'a' mode for appending instead of 'w' for writing
with open("sales.csv", "a", newline="") as file:
    writer = csv.writer(file)
    # Append the new row at the end of the file
    writer.writerow(new_sales_record)

print("Status: Appended new sales record to sales.csv.")

# Verify by printing the last 3 lines
with open("sales.csv", "r") as file:
    lines = file.readlines()
    print("Last 3 records in sales.csv:")
    for line in lines[-3:]:
        print(line.strip())
