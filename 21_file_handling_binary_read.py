# File handling: Reading binary data
# The 'rb' mode opens a file for reading in binary format.

def main():
    try:
        with open("example_binary.bin", "rb") as file:
            content = file.read()
            print("Content of the binary file:", list(content))
    except FileNotFoundError:
        print("The binary file does not exist. Run the binary write example first.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
