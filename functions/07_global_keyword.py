# The 'global' Keyword
# Used to modify a global variable from inside a function

count = 0 # Global variable

def increment():
    global count # Declare that we want to use the global 'count'
    count += 1
    print(f"Inside function: count is {count}")

print(f"Before: {count}")
increment()
increment()
print(f"After: {count}")

# Without the 'global' keyword, Python would create a NEW local variable 
# instead of modifying the global one if you tried to assign to it.
