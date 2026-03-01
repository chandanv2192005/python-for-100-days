# Lesson 10: File Handling
import os

# "w" mode — creates or OVERWRITES
file = open("notes.txt", "w")
file.write("Hello, World!\n")
file.write("Python is awesome!\n")
file.close()    # ALWAYS close the file!

# Method 1 — read() — entire file as one string
file = open("notes.txt", "r")
content = file.read()
print(content)
file.close()

# Method 2 — readline() — one line at a time
file = open("notes.txt", "r")
line1 = file.readline()
line2 = file.readline()
file.close()

# Method 3 — readlines() — all lines as a list
file = open("notes.txt", "r")
lines = file.readlines()    # ['Hello, World!\n', ...]
file.close()

# Using `with` statement
# Writing
with open("notes.txt", "w") as file:
    file.write("Hello, World!\n")
    file.write("Python is great!\n")
# file is automatically closed here!

# Reading
with open("notes.txt", "r") as file:
    content = file.read()
    print(content)

# Appending
with open("diary.txt", "w") as file:
    file.write("Day 1: Started Python!\n")

with open("diary.txt", "a") as file:    # append mode
    file.write("Day 2: Learned files!\n")

with open("diary.txt", "r") as file:
    print(file.read())

# Checking if a File Exists
if os.path.exists("notes.txt"):
    print("File exists!")
else:
    print("File not found!")

print(os.path.getsize("notes.txt"))  # size in bytes
os.remove("notes.txt")               # delete a file

# Looping Through Lines
with open("diary.txt", "r") as file:
    for line in file:
        print(line.strip())    # strip() removes trailing \n

# Clean up remaining file
if os.path.exists("diary.txt"):
    os.remove("diary.txt")
