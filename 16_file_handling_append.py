# File handling example: Appending to a file
# The 'a' mode opens a file for appending. It retains the old content
# and adds new content at the end of the file.

def main():
    with open("example_write.txt", "a") as file:
        file.write("Appending this new line at the end.\n")
    print("Successfully appended to example_write.txt")

if __name__ == "__main__":
    main()
# End of append script 
