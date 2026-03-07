try:
    with open("new_file.bin", "xb") as file:
        file.write(b"This is a new binary file!")
        
    print("File created successfully.")
    
except FileExistsError:
    print("File already exists. Cannot create.")

# Output: File created successfully.