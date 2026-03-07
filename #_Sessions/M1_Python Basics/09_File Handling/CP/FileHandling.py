"""
Docstring for FileHandling.py.CP.FileHandling
"""
# Reading Entire File 
with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\Output.txt","r") as file:
    content = file.read()
    print(content)

"""
Hello , This is an example file . 
It Contains multiple lines of text.
"""

# Reading An empty File 

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\empty.txt","w") as file:
    pass # crerate an empty file 

with open (r"#_Sessions\M1_Python Basics\09_File Handling\CP\empty.txt","r") as file:
    content = file.read()
    print("Content of Empty File . ",content)
    # Content of Empty File .

# reading Oneline ata a time . 
with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\Output.txt","r") as file:
    line1 = file.readline()
    print("First Line : ",line1) # always gives a space after each line as the control goes to next line 
    line2 = file.readline()
    print("secondLine Line : ",line2)

# Reading All lines using loop 

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\Output.txt","r") as file:
    while True:
        line = file.readline()
        if not line:
            break
        print("Read Line: ",line.strip())
# Read Line:  Hello , This is an example file .
# Read Line:  It Contains multiple lines of text.

# Reading Lines with a Specified Number of Lines

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\Output.txt", "r") as file:
    for line in range(2):
        line = file.readline()
        print("Reading Line: ", line.strip())
        #print (type(line))

"""
Reading Line:  Hello , This is an example file .
None         ?
Reading Line:  It Contains multiple lines of text.
None           ?
"""

# Reading All Lines at Once

# with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\Output.txt","r") as file:
#     lines = file.readlines()
#     print(lines)

# ['  Hello , This is an example file .    \n', '                It Contains multiple lines of text.      \n', 'It is a big file.']

# Looping Over the List of Lines

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\Output.txt","r") as file:
    lines = file.readlines()
    for line in lines:
        # print (type (line))
        print(line.strip())

# Writing a Single Line to a File

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\single_line.txt","w") as file:
    file.write("This a New single line ")
    

# Writing Multiple Lines Manually
with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\single_line.txt","w") as file:
    file.write("This a New single line \n")
    file.write("This a New second line \n")
    file.write("This a New third line \n")
    
# Appending to an Existing File
with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\single_line.txt","a") as file:
    file.write("What a line! \n")

# Writing User Input to a File

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\single_line.txt","a") as file:
    user_input = input("Enter a line to write on file: ")
    file.write(user_input + "\n")

# Enter a line to write on file: line added 

# Writing a list of strings 
lines = [
    "first line. \n",
    "second line. \n",
    "third line. \n"
]

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\single_line.txt","w") as file:
    for line in lines:
        file.write(line)

"""
first line. 
second line. 
third line. 

"""

# writing lines using loop 

lines = []

for i in range(5):
    lines.append(f"This is line {i+1}. \n")

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\multi_line.txt","w") as file:
    file.writelines(lines) 

"""
This is line 1. 
This is line 2. 
This is line 3. 
This is line 4. 
This is line 5. 

"""
# Appending Multiple Lines to an Existing File

new_lines = [
    "This is an additinal line one \n"
    "This is an additinal line two \n"
    "This is an additinal line three \n"
]

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\multi_line.txt","a") as file:
    file.writelines(new_lines) 

"""
This is line 1. 
This is line 2. 
This is line 3. 
This is line 4. 
This is line 5. 
This is an additinal line one 
This is an additinal line two 
This is an additinal line three 
"""

# Writing Lines Using a Loop

lines = []

for i in range(5):
    lines.append(f"This is line {i+1}.\n")

with open(r"#_Sessions\M1_Python Basics\09_File Handling\CP\multi_line.txt","a") as file:
    file.writelines(lines) 

"""

This is line 1. 
This is line 2. 
This is line 3. 
This is line 4. 
This is line 5. 
This is an additinal line one 
This is an additinal line two 
This is an additinal line three 
This is line 1.
This is line 2.
This is line 3.
This is line 4.
This is line 5.

"""

