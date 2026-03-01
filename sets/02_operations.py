# Set operations
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}

print(f"Set a: {a}")
print(f"Set b: {b}")

# Union (|)
# Combines elements from both sets
print(f"Union (a | b): {a | b}") # {1, 2, 3, 4, 5, 6}

# Intersection (&)
# Only elements present in both sets
print(f"Intersection (a & b): {a & b}") # {3, 4}

# Difference (-)
# Elements in 'a' but not in 'b'
print(f"Difference (a - b): {a - b}") # {1, 2}

# Symmetric difference (^)
# Elements in either 'a' or 'b', but not both
print(f"Symmetric difference (a ^ b): {a ^ b}") # {1, 2, 5, 6}
