import os 

def list_files(directory_path):
    
    folder_type = {}

    for root, dirs, files in os.walk(directory_path):
        folder_name = os.path.basename(root) if root != directory_path else "."

        # Store files per folder
        folder_type[folder_name] = files

    # Print in required format
    for folder, files in folder_type.items():
        print(f"Files in '{folder}': {files}")

