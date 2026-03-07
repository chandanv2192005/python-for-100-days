# File handling example: Reading from a file
# The 'r' mode opens a file for reading. It is the default mode.

def main():
    try:
        with open("example_write.txt", "r") as file:
            content = file.read()
            print("Content of the file:")
            print(content)
    except FileNotFoundError:
        print("The file does not exist. Run the write example first.")

if __name__ == "__main__":
    main()
# End of read script
