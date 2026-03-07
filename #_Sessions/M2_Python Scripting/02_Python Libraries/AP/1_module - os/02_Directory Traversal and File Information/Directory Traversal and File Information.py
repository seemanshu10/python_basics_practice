# Directory Traversal and File Information

import os 

print("===== DIRECTORY TRAVERSAL REPORT =====\n")

root_folder = r"#_Sessions\M2_Python Scripting\02_Python Libraries\AP\1_module - os\02_Directory Traversal and File Information\traversal_test" # root folder path 

for root, dirs, files in os.walk(root_folder):
    
    level = root.replace(root_folder, "").count(os.sep) # calculates how deep we travel in folder structure 
    indent = "    " * level
    
    print(f"{indent}-> {os.path.basename(root)}")
    
    sub_indent = "    " * (level + 1)
    
    for file in files:
        file_path = os.path.join(root, file)
        
        size = os.path.getsize(file_path)
        
        readable = os.access(file_path, os.R_OK)
        writable = os.access(file_path, os.W_OK)
        executable = os.access(file_path, os.X_OK)
        
        print(f"{sub_indent} -->{file}")
        print(f"{sub_indent}   Size: {size} bytes")
        print(f"{sub_indent}   Readable: {readable}")
        print(f"{sub_indent}   Writable: {writable}")
        print(f"{sub_indent}   Executable: {executable}")
        print()