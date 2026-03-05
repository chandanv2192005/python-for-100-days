import json

user_data = {
    "name": "Chandan",
    "course": "Python for 100 Days",
    "lessons_completed": 12,
    "is_active": True
}

# Writing Python dictionary to a JSON file
with open("user.json", "w") as file:
    json.dump(user_data, file, indent=4) 
print("JSON file created!")

# Reading from a JSON file back into a Python dictionary
with open("user.json", "r") as file:
    loaded_data = json.load(file)
    
print(f"Welcome back, {loaded_data['name']}!")
