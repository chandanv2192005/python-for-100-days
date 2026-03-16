import array

# Create an array of integers (type code 'i')
int_array = array.array('i', [10, 20, 30, 40, 50])

print("Array elements:")
for el in int_array:
    print(el)

print(f"First element: {int_array[0]}")
print(f"Last element: {int_array[-1]}")
 
