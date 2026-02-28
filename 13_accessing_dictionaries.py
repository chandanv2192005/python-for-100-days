# Accessing Values
person = {"name": "John", "age": 25, "city": "New York"}

print(f"Name: {person['name']}") # John

# Using .get() method
print(f"Email: {person.get('email')}") # None (no crash!)
print(f"Email (with default): {person.get('email', 'N/A')}") # N/A (default value)
