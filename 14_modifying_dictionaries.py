# Adding, Updating & Removing
person = {"name": "John", "age": 25}

person["email"] = "john@email.com" # add new key
person["age"] = 26 # update existing key
print(f"After adding and updating: {person}")

del person["email"] # remove key
print(f"After deleting email: {person}")

age = person.pop("age") # remove and return value
print(f"Popped Age: {age}")
print(f"Final Person Dictionary: {person}")

student = {"name": "chandan", "age": 20}
print(student)

student["email"] = "chandanv2192005@gmail.com"
student["city"] = "bangalore"
print(student)
