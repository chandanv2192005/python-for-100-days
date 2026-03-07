# File handling: Writing binary data
# The 'wb' mode opens a file for writing in binary format.

def main():
    try:
        # Some sample bytes
        data = bytes([120, 3, 255, 0, 100])
        with open("example_binary.bin", "wb") as file:
            file.write(data)
        print("Successfully wrote binary data to example_binary.bin")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()
