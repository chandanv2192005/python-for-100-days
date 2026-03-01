# Sets — Unique Values Only
fruits = {"apple", "banana", "mango"}
print(f"Fruits set: {fruits}")

# Creating an empty set
# use set(), NOT {} (that creates a dict!)
empty_set = set()
print(f"Empty set: {empty_set}")
print(f"Type of empty_set: {type(empty_set)}")

# Duplicates removed automatically!
nums = {1, 2, 2, 3, 3, 3, 4, 5, 6, 7, 5, 6}
print(f"Initial list with duplicates: {{1, 2, 2, 3, 3, 3, 4}}")
print(f"Set from list (duplicates removed): {nums}") # {1, 2, 3, 4}
