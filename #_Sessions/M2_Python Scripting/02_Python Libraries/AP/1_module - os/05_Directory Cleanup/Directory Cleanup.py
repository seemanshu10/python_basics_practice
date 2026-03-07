# Directory Cleanup
import os

filePathRoot = r"#_Sessions\M2_Python Scripting\02_Python Libraries\AP\1_module - os\05_Directory Cleanup\cleanup_test"

# Add some sample files 
sample_files = ["file1.txt", "file2.log", "file3.jpg", "file4.log", "file5.txt"]
for filename in sample_files:
    file_path = os.path.join(filePathRoot, filename)
    with open(file_path, "w") as f:
        f.write(f"Sample content for {filename}")

        
listOf_files = os.listdir(filePathRoot)
# List all files in the directory 
print("All files before deletion:")
# print(files)
for file in listOf_files:
    print(file)

# Delete only .log files and track deleted ones
deleted_logs = []
for filename in listOf_files:
    if filename.endswith(".log"):
        os.remove(os.path.join(filePathRoot, filename))
        deleted_logs.append(filename)

print("\nDeleted .log files:")
# print(deleted_logs)
for file in deleted_logs:
    print(file)

#  Listing remaining files 
remaining_files = os.listdir(filePathRoot)
print("\nFiles remaining after deletion:")
for file in remaining_files:
    print(file)