# Variable Scope — Local vs Global
name = "John" # global variable — accessible everywhere

def greet():
    x = 10 # local variable — only inside this function
    print(name) # can access global variable: prints John
    print(x) # can access local variable: prints 10

greet()
# print(x) # ERROR! x does not exist outside the function
