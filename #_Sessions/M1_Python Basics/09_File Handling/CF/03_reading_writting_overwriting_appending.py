# ------------- Various Reading Methods -----------------------

# Using - read() Method
# file = open("example.txt", "r")
# content = file.read()

# print(content)
# file.close()

# Using - readline() Method
# file = open("example.txt", "r")

# line1 = file.readline()
# print("First line:", line1)

# # line2 = file.readline()
# # print("Second line:", line2)

# file.close()

# # Using - readlines() Method
# file = open("quotes.txt", "r")
# lines = file.readlines()
# for line in lines:
#     print("Line:", line.strip())


# c = "\nHello\tNew"
# # print(c)
# print(c.strip())

# file.close()


# # ---------------- Various Writing Methods --------------------------

# # Using - write() Method
# with open("example.txt", "w") as file:
#     file.write("This is the first line.\n")
#     file.write("This is the second line.\n") 
#     file.write("This is the second line.\n") 
#     file.write("This is the second line.\n") 



# Using - writelines() Method
lines = [
    "First line.\n",
    "Second line.\n",
    "Third line.\n"
]

# with open("example.txt", "w") as file:
#     file.writelines(lines) 



# # ----------------- Overwriting Vs Appending ------------------------------

# # Overwriting Files -- open in write mode
with open("over.txt", "w") as file:
    file.write("This is the first line.\n") 

with open("over.txt", "w") as file:
    file.write("This is the second line.\n")


# # -----------------------------------------------------

# # Appending to Files -- open append mode
with open("example.txt", "a") as file:
    file.write("This is an additional line.\n")

with open("example.txt", "a") as file:
    file.write("This is another line.\n")



