import csv

# Data for a Tab-Separated Values (TSV) file
books = [
    ["Title", "Author", "Year"],
    ["The Great Gatsby", "F. Scott Fitzgerald", 1925],
    ["1984", "George Orwell", 1949],
    ["To Kill a Mockingbird", "Harper Lee", 1960]
]

# Writing with a custom delimiter (tab)
file_name = "books.tsv"
with open(file_name, "w", newline="") as file:
    # Set the delimiter to '\t' instead of ','
    writer = csv.writer(file, delimiter='\t')
    writer.writerows(books)

print(f"Status: Custom delimiter file {file_name} created.")

# Reading back the TSV file using the custom delimiter
print("\nReading back data:")
with open(file_name, "r") as file:
    # Must specify the same delimiter to read correctly
    reader = csv.reader(file, delimiter='\t')
    for row in reader:
        print(row)
