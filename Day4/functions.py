 # Day 4: Functions in Python

def greet(name):
    """Function to greet a person by name."""
    return f"Hello, {name}!"  

# Example usage 
print(greet("Alice"))

# Function with default arguments 
def power(base, exponent=2):
    """Function to calculate the power of a number."""
    return base ** exponent

# Example usage
print(power(3))  # Default exponent
print(power(3, 3))  # Custom exponent

# Function with variable arguments
def add_numbers(*args):
    """Function to add an arbitrary number of numbers."""
    return sum(args)

# Example usage
print(add_numbers(1, 2, 3, 4))
