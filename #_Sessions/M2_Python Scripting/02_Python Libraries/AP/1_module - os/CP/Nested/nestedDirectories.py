import os 

# create a nested dixtionary structure 
nested_path = r"02_Python Libraries\CP\Nested\projects\python\scripts"

os.makedirs(nested_path,exist_ok=True)
print(f"Nested Directories created : {nested_path}")

files = os.listdir(".")

print("Files and directories in the current folder:")
for file in files:
    print(file)