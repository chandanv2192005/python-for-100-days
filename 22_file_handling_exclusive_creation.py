# File handling: Exclusive creation mode
# The 'x' mode opens a file for exclusive creation, failing if the file already exists.

def main():
    filename = "example_exclusive.txt"
    try:
        with open(filename, "x") as file:
            file.write("This file was created exclusively.\n")
        print(f"Successfully created and wrote to {filename}")
    except FileExistsError:
        print(f"Failed: The file {filename} already exists!")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
