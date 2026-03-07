# Using the with statement 
# with open("example.txt", "r") as file:
#     content = file.read()
#     print(content)


# # Reading r Mode
# # read entire file
# with open("example.txt", "r") as file:
    # content = file.read()  
#     print(content) 


# # read file line by line
# with open("example.txt", "r") as file:
#     for line in file:
#         print(line.strip())


# # Writing w Mode
# # # single line
with open("example.txt", "w") as file:
    file.write("Hello, World!")  



# # multiple line
with open("output.txt", "w") as file:
    file.write("First Line\n")
    file.write("Second Line\n")
    file.write("Third Line\n")


# # Appending a Mode
# # single line
with open("output.txt", "a") as file:
    file.write("This line will be appended")


# # multiple lines
with open("output.txt", "a") as file:
    file.write("Appended Line 1\n")
    file.write("Appended Line 2\n")