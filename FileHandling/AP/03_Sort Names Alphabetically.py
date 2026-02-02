"""
Create a text file named input.txt and populate it with a list of names, one name per line.
Write a Python program that:
Opens and reads the input.txt file.
Sorts the names alphabetically.
Writes the sorted names to a new file called output.txt.
Ensure that the program handles exceptions, such as the input file not existing.
"""
# reading  file  and printing 
with open ("FileHandling/AP/input.txt","r") as file:
    names = file.readlines()
    print(names)

# Remove any extra whitespace or newline characters
names = [name.strip() for name in names]


# Sort names alphabetically
names.sort()

# Write sorted names to the output file
with open("FileHandling/AP/output.txt", "w") as file:
    for name in names:
        file.write(name + "\n")

print(f"Sorted names have been written to '{file.name}'")