import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample.txt")

with open(file_path, 'r') as file:
    content = file.read()

print("File Content: ")
print(content)

"""
File Content: 
Hello, This is a smaple file for practicising realtive paths.
"""