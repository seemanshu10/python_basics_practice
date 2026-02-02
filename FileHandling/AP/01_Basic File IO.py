"""

Python program that reads from a file and writes to a file. The program should:
Read a list of names from a file.
Sort the names alphabetically.
Write the sorted names to a new file.
"""

# reading  file  and printing 
with open ("FileHandling/AP/names.txt","r") as file:
    names = file.readlines()
    print(names)

# Remove any extra whitespace or newline characters
names = [name.strip() for name in names]

# Sort names alphabetically
names.sort()

# Write sorted names to the output file
with open("FileHandling/AP/sorted_names.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print(f"Sorted names have been written to '{file}'")

# FileNotFound : 2
# OutOfMemory : 1
# NullReference : 1