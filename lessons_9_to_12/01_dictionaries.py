# Lesson 9: Dictionaries

person = {"name": "John", "age": 25, "city": "New York"}
empty  = {}
mixed  = {"id": 1, "score": 9.5, "active": True}

print(person["name"])              # John
print(person.get("email"))         # None  (no crash!)
print(person.get("email", "N/A"))  # N/A   (default value)

person["email"] = "john@email.com"  # add new key
person["age"]   = 26                # update existing key

del person["email"]                 # remove key
age = person.pop("age")             # remove and return value
print(age)    # 25

person = {"name": "John", "age": 25, "city": "New York"}
print(person.keys())     # dict_keys(['name', 'age', 'city'])
print(person.values())   # dict_values(['John', 25, 'New York'])
print(person.items())    # dict_items([('name','John'), ...])
print(len(person))       # 3
print("name" in person)  # True

for key, value in person.items():
    print(f"{key}: {value}")

students = {
    "Alice": {"age": 20, "grade": "A"},
    "Bob":   {"age": 22, "grade": "B"},
}

print(students["Alice"]["grade"])   # A

for name, info in students.items():
    print(f"{name} -> Age: {info['age']}, Grade: {info['grade']}")
