# Python If-Else Statements Examples

# 1. Simple if-else
age = 18
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# 2. If-elif-else chain
score = 85
if score >= 90:
    grade = 'A'
elif score >= 80:
    grade = 'B'
elif score >= 70:
    grade = 'C'
else:
    grade = 'F'
print(f"Your grade is: {grade}")

# 3. Nested if statements
is_logged_in = True
has_permission = False

if is_logged_in:
    if has_permission:
        print("Access granted.")
    else:
        print("Access denied: Missing permissions.")
else:
    print("Please log in first.")

# 4. Short-hand if (Ternary operator)
status = "Allow" if age >= 18 else "Deny"
print(f"Entry status: {status}")

# 5. Using multiple conditions (and, or)
temperature = 25
is_raining = False

if temperature > 20 and not is_raining:
    print("Perfect weather for a walk!")
elif temperature < 10 or is_raining:
    print("Stay indoors.")
else:
    print("Normal weather.")
