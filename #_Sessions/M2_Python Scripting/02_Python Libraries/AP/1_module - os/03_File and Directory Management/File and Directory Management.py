# File and Directory Management

import os
import shutil

root_path = r"#_Sessions\M2_Python Scripting\02_Python Libraries\AP\1_module - os\03_File and Directory Management"

# Full path for practice_os
practice_os_path = os.path.join(root_path, "practice_os")
# print(practice_os_path)
# Create main directory
if not practice_os_path:
    os.makedirs(practice_os_path, exist_ok=True)

# Subdirectories
dirs = ["dir1", "dir2", "dir3"]
for d in dirs:
    os.makedirs(os.path.join(practice_os_path, d), exist_ok=True)

# create file content on three directories 
files_content = {
    "dir1/file1.txt": "Hello from dir1",
    "dir2/file2.txt": "Hello from dir2",
    "dir3/file3.txt": "Hello from dir3"
}

for relative_path, content in files_content.items():    # trraversing through files content  
    file_path = os.path.join(practice_os_path, relative_path)
    with open(file_path, "w") as f:
        f.write(content)

# Rename file1.txt to renamed_file1.txt
os.rename(
    os.path.join(practice_os_path, "dir1/file1.txt"),
    os.path.join(practice_os_path, "dir1/renamed_file1.txt")
)

# Delete file2.txt
file2_path = os.path.join(practice_os_path, "dir2/file2.txt")
if os.path.exists(file2_path):
    os.remove(file2_path)

# Delete entire dir3 directory
dir3_path = os.path.join(practice_os_path, "dir3")
if os.path.exists(dir3_path):
    shutil.rmtree(dir3_path)

print("All operations completed successfully.")