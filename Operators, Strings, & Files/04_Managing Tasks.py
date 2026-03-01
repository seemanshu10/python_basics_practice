"""
 Managing Tasks

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

"""
# reading the file contents 
with open (r"Operators, Strings, & Files\tasks.txt","r") as file:
    content = file.read()
    print("Currect Tasks: \n",content)

# creating the file 

with open (r"Operators, Strings, & Files\tasks.txt","w") as file:
    file.write("- Finish homework\n")
    file.write("- Clean room\n")

# reading the file contents 
with open (r"Operators, Strings, & Files\tasks.txt","r") as file:
    content = file.read()
    print("After Writing: \n",content)

# appnding the files 

with open (r"Operators, Strings, & Files\tasks.txt","a") as file:
    file.write("- Finish homework\n")
    file.write("- Clean room\n")
    file.write("- Read a book\n")


# reading the file contents 
with open (r"Operators, Strings, & Files\tasks.txt","r") as file:
    content = file.read()
    print("After Appending: \n",content)

