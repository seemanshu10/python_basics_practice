# same folder Structure 

# with open(r"Absolute&RelativePath\CP\repo\sample.txt", "r") as file:
#     content = file.read()
# print(content)

# file in subfolder 

# with open(r"D:\PipelineTD\python_basics_practice\Absolute&RelativePath\CP\repo\data\sample.txt", "r") as file:
#     content = file.read()
# print(content)

with open(r"D:\PipelineTD\python_basics_practice\Absolute&RelativePath\CP\repo\data\sample.txt", "r") as file:
    content = file.read()
print(content)

with open(r"D:\PipelineTD\python_basics_practice\Absolute&RelativePath\CP\repo\logs\my_app.log", "w") as log_file:
    log_file.write("Application started successfully.\n")
print("Log Written Successfully.")