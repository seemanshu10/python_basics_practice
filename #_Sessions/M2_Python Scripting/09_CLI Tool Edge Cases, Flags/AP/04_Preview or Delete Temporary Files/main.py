import sys
import os

def print_help():
    help_test = ("""
    Usage : python main.py <directory_path> <prefix> [--preview | --delete]
    Options:
        --preview   Preview the new file names without renaming.
        --delete    to remove all .tmp files from the directory.
        --help      Show this help messages and exit.

    Description: 
        This script renames all files in a directory by adding a prefix . 

    Example:
        python main.py --help
        python main.py ./temp_project --preview
        python main.py ./temp_project --delete
                        
    """)
    print(help_test)
    sys.exit(0)

def find_temperory_files(directory_path):
    temp_files = []
    for root, dirs, files in os.walk(directory_path):
        for file in files:
            if file.endswith(".tmp"):
                # Save relative path to directory
                rel_path = os.path.relpath(os.path.join(root, file), directory_path)
                temp_files.append(rel_path)
    return temp_files

def preview_tmp_files(directory_path):
    tmp_files = find_temperory_files(directory_path)
    if tmp_files:
        print("Temporary files:")
        for file in tmp_files:
            print(file.split("\\")[1])
    else:
        print("No temporary files found.")

def delete_tmp_files(directory_path):
    tmp_files = find_temperory_files(directory_path)

    if tmp_files:
        for file in tmp_files:
            # delete 
            os.remove(os.path.join(directory_path,file))
    else:
        print("No temporary files found to be deleted.")
    

def main():

    if len(sys.argv) < 2 or "--help" in sys.argv:
        print_help()
        return
    
    args = sys.argv[1:] 
    directory_path = args[0]

    # Check if directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' does not exist.")
        
    if "--preview" in sys.argv:
        preview_tmp_files(directory_path)
    elif "--delete" in sys.argv:
        delete_tmp_files(directory_path)
    

if __name__ == "__main__":
    main()