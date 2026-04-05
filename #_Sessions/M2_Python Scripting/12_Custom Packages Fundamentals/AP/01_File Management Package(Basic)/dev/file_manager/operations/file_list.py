import os 

def list_files(directory_path):
    
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            rel_path = os.path.relpath(os.path.join(root, file), directory_path)
            print(rel_path)


def list_files_dir(directory):
    try:
        files = os.listdir(directory)
        print(f"Files in dev: {files}")
    except Exception as e:
        print(f"Error listing files: {e}")