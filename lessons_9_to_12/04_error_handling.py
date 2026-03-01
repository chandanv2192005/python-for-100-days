# Lesson 11: Error Handling

# Catching basic errors
try:
    num = int(input("Enter a number: "))
    print(f"You entered: {num}")
except ValueError:
    print("That is not a valid number!")

# Catching Specific Errors
try:
    num1 = int(input("First number: "))
    num2 = int(input("Second number: "))
    result = num1 / num2
    print(f"Result: {result}")
except ValueError:
    print("Please enter valid numbers!")
except ZeroDivisionError:
    print("Cannot divide by zero!")
except Exception as e:
    print(f"Unexpected error: {e}")

# try / except / else / finally
try:
    file = open("data.txt", "r")
    content = file.read()
except FileNotFoundError:
    print("File not found!")
else:
    print("File read successfully!")
    print(content)
finally:
    print("Program finished.")    # ALWAYS runs!

# Raising Your Own Errors
def set_age(age):
    if age < 0:
        raise ValueError("Age cannot be negative!")
    if age > 150:
        raise ValueError("Age seems unrealistic!")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid input: {e}")

# Input Validation with Loops
while True:
    try:
        user_input = input("Enter your age (or 'q' to quit): ")
        if user_input.lower() == 'q':
            break
        age = int(user_input)
        if age < 0 or age > 120:
            raise ValueError("Age must be 0-120!")
        print(f"Your age: {age}")
        break    # exit loop on valid input
    except ValueError as e:
        print(f"Invalid: {e}. Try again!")
