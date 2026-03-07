"""
# Description of the Task
In this task, students will practice file operations in Python by writing a program that reads from an input text file, processes the data, and writes the processed data to an output text file. The program will read a list of names from the input file, sort the names alphabetically, and then write the sorted names to the output file.

# Instructions
Create a text file named input.txt and populate it with a list of names, one name per line.
Write a Python program that:
Opens and reads the input.txt file.
Sorts the names alphabetically.
Writes the sorted names to a new file called output.txt.
Ensure that the program handles exceptions, such as the input file not existing.

# Learning Objective
By completing this task, students will:
Gain experience with file reading and writing in Python.
Learn how to handle file-related exceptions.
Practice basic data processing and sorting in Python.

# Sample UsageExample usage:
Create input.txt with the following content:
John
Alice
Bob
Charlie
Run the Python program.

The program creates output.txt with the following content:
Alice
Bob
Charlie
John
"""

# reading  file  and printing 
with open (r"#_Sessions\M1_Python Basics\09_File Handling\AP\input.txt","r") as file:
    names = file.readlines()
    print(names)

# Remove any extra whitespace or newline characters
names = [name.strip() for name in names]


# Sort names alphabetically
names.sort()

# Write sorted names to the output file
with open(r"#_Sessions\M1_Python Basics\09_File Handling\AP\output.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print(f"Sorted names have been written to '{file.name}'")