"""
Update & Append Notes

Task Description
----------------
In this task, you will:
• Use combined file modes (r+, w+, a+) to manage a text file
• Read and update existing content using r+
• Write and read notes using w+
• Append and read all content using a+
• Practice moving the file cursor with seek() to read from the correct position


Instructions
------------
• Create a file named `notes.txt` and write some initial notes into it
• Open the file using `r+` mode:
  - Read and display the original notes
  - Move the cursor to the start using `seek()`
  - Overwrite the first note
  - Read and print the updated content
• Open the file using `w+` mode:
  - Write two new notes
  - Move the cursor to the start
  - Read and display the file content
• Open the file using `a+` mode:
  - Append a new note to the file
  - Move the cursor to the beginning
  - Read and display all notes
• Print the content after each stage to confirm file behavior

"""

# reading the file contents in r+ 
with open (r"Operators, Strings, & Files\notes.txt","r+") as file:
    content = file.read()
    print("Currect notes: \n",content)
    file.seek(0)
    file.write("- Updated Note 1\n")

    file.seek(0)
    content = file.read()
    print("After Appending:\n", content)

"""
Open the file using `w+` mode:
  - Write two new notes
  - Move the cursor to the start
  - Read and display the file content
"""

with open (r"Operators, Strings, & Files\notes.txt","w+") as file:
    file.write("- New Note A\n")
    file.write("- New Note B\n")

    file.seek(0)  # Move cursor to beginning
    content = file.read()
    print("After w+: \n", content)


# appnding the files a+

with open (r"Operators, Strings, & Files\notes.txt","a+") as file:
    file.write("- Finish homework\n")
    file.write("- Clean room\n")
    file.write("- Read a book\n")

    file.seek(0)
    content = file.read()
    print("After Appending: \n",content)



