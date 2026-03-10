# The standard array module doesn't have a built-in sort method.
# Since Python lists are often used as arrays, here is how you sort array-like lists.

my_list_array = [45, 12, 89, 33, 7]
print(f"Original array: {my_list_array}")

# Sort in ascending order
my_list_array.sort()
print(f"Sorted array (ascending): {my_list_array}")

# Sort in descending order
my_list_array.sort(reverse=True)
print(f"Sorted array (descending): {my_list_array}")

# We can also use sorted() which returns a new sorted list
original_array = [10, 2, 8, 4]
new_sorted_array = sorted(original_array)
print(f"Original unchanged: {original_array}, New sorted: {new_sorted_array}")
