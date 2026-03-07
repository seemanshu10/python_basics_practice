# Basic Syntax
# file_object = open("filename", "mode")


# Using "r" Mode (Read Mode)
# file = open("example.txt", "r")

# content = file.read()
# print(content)
# file.close()


# # Using "a" Mode (Append Mode)
# file = open("example.txt", "a")

# file.write("This line will be appended.\n")
# file.close()

# # Using "w" Mode (Write Mode)
file = open("example.txt", "w")

file.write("Hello")
file.close()


