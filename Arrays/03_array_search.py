import array

my_array = array.array('i', [10, 20, 30, 40, 50, 20])

search_value = 20

# Find the index of the first occurrence of search_value
try:
    index = my_array.index(search_value)
    print(f"Value {search_value} found at index: {index}")
except ValueError:
    print(f"Value {search_value} not found in the array.")

# Count occurrences of a value
count = my_array.count(search_value)
print(f"Value {search_value} occurs {count} time(s) in the array.")
