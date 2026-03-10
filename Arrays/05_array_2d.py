# Multi-dimensional arrays are typically implemented as lists of lists in Python.
# They are often used to represent matrices.

matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("2D Array (Matrix):")
for row in matrix:
    print(row)

# Accessing an element (e.g., row index 1, column index 2)
print(f"Element at row 1, col 2 is: {matrix[1][2]}")

# Iterating through all elements in the 2D array
print("Iterating through all elements:")
for row in matrix:
    for item in row:
        print(item, end=" ")
    print()
