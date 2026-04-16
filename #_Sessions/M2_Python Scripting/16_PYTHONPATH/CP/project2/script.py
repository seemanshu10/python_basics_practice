import os

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "data")

if os.path.exists(file_path):
    files = os.listdir(file_path)
    print("Files in the 'data' directory:")
    for file in files:
        print(file)

else:
    print("File does not exists.")
"""
Files in the 'data' directory:
file1.txt
file2.txt
file3.txt
"""