import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data", "sample.txt")

if os.path.exists(file_path):
    with open(file_path, 'r') as file:
        content = file.read()


    print("File Content: ")
    print(content)

else:
    print("File does not exists.")

"""
File Content: 
This file is located in a subdirectory. 
"""