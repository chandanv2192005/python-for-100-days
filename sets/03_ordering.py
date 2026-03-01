# Comparison of Ordering in Python Data Structures

# 1. Lists - ORDERED
# Lists maintain the exact order in which elements are added.
my_list = ["apple", "banana", "cherry"]
print("--- Lists (Ordered) ---")
print(f"Original: {my_list}")
my_list.append("date")
print(f"After append: {my_list} (Order is preserved)")

# 2. Dictionaries - ORDERED (Python 3.7+)
# Since Python 3.7, dictionaries maintain insertion order.
my_dict = {"a": 1, "b": 2, "c": 3}
print("\n--- Dictionaries (Ordered since 3.7+) ---")
print(f"Original: {my_dict}")
my_dict["d"] = 4
print(f"After adding 'd': {my_dict} (Order is preserved)")

# 3. Sets - UNORDERED
# Sets do NOT maintain any specific order. Elements are stored based on a hash.
# Every time you print a set or iterate over it, the order could technically be different.
my_set = {"apple", "banana", "cherry"}
print("\n--- Sets (Unordered) ---")
print(f"Initial set: {my_set}")
my_set.add("date")
print(f"After adding 'date': {my_set} (Order is not guaranteed)")

# Summary:
# - Lists & Tuples: Ordered (Access by index)
# - Dictionaries: Ordered by insertion (Access by key)
# - Sets: Unordered (Unique values only, no indexing)
