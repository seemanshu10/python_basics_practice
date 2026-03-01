"""
Binary File Handling Workflow

Task Objective
--------------
In this task, you will:
• Create and write to a binary file using a bytes object
• Read and display binary data from the file
• Append additional binary content to the file
• Modify existing binary data using read/write access
• Use seek() to position the file cursor correctly before writing

Instructions
------------
• Create a new binary file using write binary mode (wb)
  - Write a bytes object (e.g., b"Hello Binary World!")
• Read the entire file using read binary mode (rb)
  - Print the binary output
• Append a new bytes object to the file using append binary mode (ab)
• Use read/write binary mode (rb+) to:
  - Read and print the original content
  - Use seek() to move the cursor to the beginning
  - Overwrite the first few bytes with new binary data
    (e.g., replace "He" with "Hi")
  - Print the modified content to verify the changes

"""
fileBinaryName = r"Operators, Strings, & Files\bytes.txt"

# creating a new binary file for data 
with open(fileBinaryName, "wb") as binary_file:
    binary_file.write(b"Hello Binary World!")

# reading entire file and prnt binary output 
with open(fileBinaryName, "rb") as binary_file:
    content = binary_file.read()
    print("Before Content:", content)

# append the file 
with open(fileBinaryName, "ab") as binary_file:
    binary_file.write(b"Appended Data")
    
with open(fileBinaryName, "rb") as binary_file:
    contentAppend = binary_file.read()
    print("After Append:", contentAppend)

# Use read/write binary mode (rb+)
with open(fileBinaryName, "rb+") as file:
    
    # Read and print original content
    original_content = file.read()
    print("Original in rb+:", original_content)

    # Move cursor to beginning
    file.seek(0)

    # Overwrite first few bytes ("He" -> "Hi")
    file.write(b"Hi")

    # Move back to beginning to read modified content
    file.seek(0)
    modified_content = file.read()
    print("Modified Content:", modified_content)
