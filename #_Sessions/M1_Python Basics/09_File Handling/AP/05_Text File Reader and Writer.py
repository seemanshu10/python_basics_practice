"""
# Description of the Task
This task involves creating a Python script that can read from and write to text files. 

# Instructions
Create a Python script named file_operations.py.
The script should:
Read the contents of a file named input.txt.
Write the contents of input.txt to a new file named output.txt but with all text converted to uppercase.
Handle cases where input.txt does not exist by printing an appropriate error message.
Print a confirmation message once the contents are successfully written to output.txt.

# Learning Objective
Understand how to open and close files in Python.
Learn to read from and write to text files.
Practice error handling using try-except blocks.
Manipulate string data read from files.
"""

# Read from input.txt
input_file = open(r"#_Sessions\M1_Python Basics\09_File Handling\AP\input.txt", "r")
content = input_file.read()
input_file.close()

# Convert text to uppercase
uppercase_content = content.upper()

# Write to output.txt
output_file = open(r"#_Sessions\M1_Python Basics\09_File Handling\AP\upperCase.txt", "w")
output_file.write(uppercase_content)
output_file.close()

print("Contents successfully written to output.txt")