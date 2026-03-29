# File handling example: Reading file line by line
# This is memory efficient and suitable for large files.

def main():
    try:
        with open("example_write.txt", "r") as file:
            print("Reading line by line:") 
            for line_number, line in enumerate(file, 1): 
                print(f"Line {line_number}: {line.strip()}")  
    except FileNotFoundError:
        print("The file does not exist. Run the write example first.")

if __name__ == "__main__":
    main()
# End of read lines script
