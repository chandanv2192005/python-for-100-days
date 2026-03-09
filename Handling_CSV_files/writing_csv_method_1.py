import csv

# Data to be written (list of lists)
data = [
    ["Product ID", "Name", "Category", "Price"],
    [101, "Wireless Mouse", "Electronics", 25.99],
    [102, "Mechanical Keyboard", "Electronics", 89.50],
    [103, "Ergonomic Chair", "Furniture", 199.99],
    [104, "Standing Desk", "Furniture", 299.00]
]

# Writing to a new CSV file
with open("products.csv", "w", newline="") as file:
    writer = csv.writer(file)
    # Write multiple rows at once
    writer.writerows(data)

print("Status: Successfully written data to products.csv")

# Quick check to read it back
with open("products.csv", "r") as file:
    print("Contents of products.csv:")
    print(file.read())
