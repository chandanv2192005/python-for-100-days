# Variable Scope — Local vs Global
name = "John" # global variable — accessible everywhere

def greet():
    x = 10 # local variable — only inside this function
    print(name) # can access global variable: prints John
    print(x) # can access local variable: prints 10

greet()

try:
    print(x) # This will cause a NameError
except NameError as e:
    print(f"Caught expected error: {e}")
    print("Explanation: 'x' is a local variable inside greet() and cannot be accessed outside.")
