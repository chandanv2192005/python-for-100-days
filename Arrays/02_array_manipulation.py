import array

# Create an array
my_array = array.array('i', [1, 2, 3])

# Append an element
my_array.append(4)
print(f"After appending 4: {my_array}")

# Insert at an index
my_array.insert(1, 100)
print(f"After inserting 100 at index 1: {my_array}")

# Remove an element
my_array.remove(2)
print(f"After removing 2: {my_array}")

# Pop the last element
popped_element = my_array.pop()
print(f"Popped element: {popped_element}, Array now: {my_array}")
