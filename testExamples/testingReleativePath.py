import os 

# print(os.path)

# print(__file__)
# print(os.path.abspath(__file__))
# print(os.path.relpath(__file__))
# print(os.path.dirname(os.path.abspath(__file__)))

directory_path = os.path.dirname(os.path.abspath(__file__))

for root, dirs, files in os.walk(directory_path):
    # print(f"Root {root}")
    # print(f"dirs {dirs}")
    # print(f"files {files}")
    # print(type(files))
    for file in files:
        full_path = os.path.join(root, file)
        print(full_path)
        print(os.path.split(full_path))
        print(os.path.splitext(full_path))
        print(os.path.getsize(full_path))
    