"""
# Description of the Task:
Write a Python program that reads from a file and writes to a file. The program should:
Read a list of names from a file.
Sort the names alphabetically.
Write the sorted names to a new file.

# Instructions:
Create a text file named "names.txt" and add some names, each on a separate line.
Write a Python program to read the names from "names.txt", sort them alphabetically, and write the sorted names to a new file named "sorted_names.txt".

"""

"""

Python program that reads from a file and writes to a file. The program should:
Read a list of names from a file.
Sort the names alphabetically.
Write the sorted names to a new file.
"""

# reading  file  and printing 
with open (r"#_Sessions\M1_Python Basics\09_File Handling\AP\names.txt","r") as file:
    names = file.readlines()
    print(names)

# Remove any extra whitespace or newline characters
names = [name.strip() for name in names]

# Sort names alphabetically
names.sort()

# Write sorted names to the output file
with open(r"#_Sessions\M1_Python Basics\09_File Handling\AP\sorted_names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print(f"Sorted names have been written to '{file.name}'")

