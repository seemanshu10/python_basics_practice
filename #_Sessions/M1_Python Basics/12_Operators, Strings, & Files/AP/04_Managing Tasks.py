"""
🎯 AP. Managing Tasks

Task Objective
--------------
In this task, you will:
• Work with text files using Python's file handling modes
• Read and display content from a file
• Overwrite existing file content with new data
• Append new data to an existing file without removing current content
• Use output printing to verify file content after each operation


Instructions
------------
• Create a text file named `tasks.txt`
• Open the file in read mode (`r`)
  - Read and print its current content
• Open the file in write mode (`w`)
  - Overwrite the content with at least two new tasks
• Open the file in append mode (`a`)
  - Add at least one additional task to the file
• After each operation (read, write, append):
  - Re-open the file in read mode
  - Print its content to verify the updates


Sample Output
-------------
Current Tasks:
- Buy groceries
- Call Mom

After Writing:
- Finish homework
- Clean room

After Appending:
- Finish homework
- Clean room
- Read a book
"""

file_path = r"#_Sessions\M1_Python Basics\12_Operators, Strings, & Files\AP\tasks.txt"
# reading the file contents 
with open (file_path,"r") as file:
    content = file.read()
    print("Current Tasks: \n",content)

# creating the file 

with open (file_path,"w") as file:
    file.write("- Finish homework\n")
    file.write("- Clean room\n")

# reading the file contents 
with open (file_path,"r") as file:
    content = file.read()
    print("After Writing: \n",content)

# appnding the files 

with open (file_path,"a") as file:
    file.write("- Finish homework\n")
    file.write("- Clean room\n")
    file.write("- Read a book\n")


# reading the file contents 
with open (file_path,"r") as file:
    content = file.read()
    print("After Appending: \n",content)
