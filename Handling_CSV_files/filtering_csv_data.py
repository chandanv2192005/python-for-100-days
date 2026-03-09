import csv

# Goal: Read employees.csv, filter out only "Engineering" department workers, 
# and save them into a new file called 'engineers.csv'

engineers = []

# Step 1: Read the CSV and filter
with open("employees.csv", "r") as read_file:
    reader = csv.DictReader(read_file)
    for row in reader:
        if row["department"] == "Engineering":
            engineers.append(row)

# Step 2: Write the filtered data to a new CSV
with open("engineers.csv", "w", newline="") as write_file:
    if engineers:
        fieldnames = engineers[0].keys()
        writer = csv.DictWriter(write_file, fieldnames=fieldnames)
        
        writer.writeheader()
        writer.writerows(engineers)
        print(f"Status: Successfully saved {len(engineers)} engineers to engineers.csv")
    else:
        print("No engineers found.")
