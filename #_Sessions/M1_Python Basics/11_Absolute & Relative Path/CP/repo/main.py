# same folder Structure 

# with open(r"#_Sessions\M1_Python Basics\11_Absolute & Relative Path\CP\repo\data\sample.txt", "r") as file:
#     content = file.read()
# print(content)

# file in subfolder 

# with open(r"#_Sessions\M1_Python Basics\11_Absolute & Relative Path\CP\repo\data\sample.txt", "r") as file:
#     content = file.read()
# print(content)

with open(r"#_Sessions\M1_Python Basics\11_Absolute & Relative Path\CP\repo\data\sample.txt", "r") as file:
    content = file.read()
print(content)

with open(r"#_Sessions\M1_Python Basics\11_Absolute & Relative Path\CP\repo\logs\my_app.log", "w") as log_file:
    log_file.write("Application started successfully.\n")
print("Log Written Successfully.")