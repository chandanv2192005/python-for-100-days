import csv

updated_rows = []

# Reading the original CSV file
with open("products_02.csv", "r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(f"Old Price for {row['ProductName']}: {row['Price']}")
        # Increase price by 10%
        new_price = float(row["Price"]) * 1.10
        row["Price"] = round(new_price, 2)
        updated_rows.append(row)

# Writing the updated data to a new CSV file
with open("updated_products_02.csv", "w") as file:
    writer = csv.DictWriter(file, fieldnames=["ProductID", "ProductName", "Price"])
    writer.writeheader()
    for row in updated_rows:
        writer.writerow(row)
