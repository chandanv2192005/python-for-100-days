# File handling using 'with' block
# This is the recommended way to handle files as it automatically closes the file

def main():
    try:
        with open("example_with.txt", "w") as file:
            file.write("This file is managed by a 'with' block.\n")
            file.write("It will be closed automatically when the block is exited.\n")
        print("Successfully wrote to example_with.txt using 'with' block.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
