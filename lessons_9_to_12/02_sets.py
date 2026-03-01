# Lesson 9: Sets

fruits  = {"apple", "banana", "mango"}
empty_set = set()    # use set(), NOT {} (that creates a dict!)

# Duplicates removed automatically!
nums = {1, 2, 2, 3, 3, 3, 4}
print(nums)    # {1, 2, 3, 4}

# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(a | b)   # {1,2,3,4,5,6}  Union
print(a & b)   # {3, 4}          Intersection
print(a - b)   # {1, 2}          Difference
print(a ^ b)   # {1,2,5,6}       Symmetric difference
