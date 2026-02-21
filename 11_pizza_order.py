print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L: ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N: ").upper()
extra_cheese = input("Do you want extra cheese? Y or N: ").upper()

bill = 0

# 1. Base price based on size
if size == "S":
    bill += 15
elif size == "M":
    bill += 20
elif size == "L":
    bill += 25
else:
    print("Invalid size. Defaulting to Small.")
    bill += 15

# 2. Add pepperoni price
if add_pepperoni == "Y":
    if size == "S":
        bill += 2
    else:
        bill += 3

# 3. Add extra cheese price
if extra_cheese == "Y":
    bill += 1

print(f"Your final bill is: ${bill}.")

