# Nested Scopes and the 'nonlocal' Keyword

def outer_function():
    message = "Hello from Outer" # Local to outer_function
    
    def inner_function():
        nonlocal message # Refers to the variable in the nearest enclosing scope
        message = "Hello from Inner"
        print(f"Inner: {message}")
        
    print(f"Outer before: {message}")
    inner_function()
    print(f"Outer after: {message}")

outer_function()

# Summary of Scopes (LEGB rule):
# L: Local - Inside the current function
# E: Enclosing - Inside any enclosing functions
# G: Global - At the top level of the module
# B: Built-in - Keywords and built-in functions (like print, len)
