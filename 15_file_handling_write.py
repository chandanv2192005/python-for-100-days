# File handling example: Writing to a file
# The 'w' mode opens a file for writing. It creates the file if it does not exist,
# and overwrites the contents if it does.

def main():
    with open("example_write.txt", "w") as file:
        file.write("Hello, this is a test string!\n")
        file.write("Writing multiple lines is easy.\n")
    print("Successfully wrote to example_write.txt")

if __name__ == "__main__":
    main()
# End of write script
