#If you have a Python object, you can convert it into a JSON string by using the json.dumps() method.
import json

# a Python object (dict):
x = {
  "name": "chandan",
  "age": 20,
  "city": "Bangalore"
}

# convert into JSON:
y = json.dumps(x)

# the result is a JSON string:
print(y)

#output
#{"name": "chandan", "age": 20, "city": "Bangalore"}
