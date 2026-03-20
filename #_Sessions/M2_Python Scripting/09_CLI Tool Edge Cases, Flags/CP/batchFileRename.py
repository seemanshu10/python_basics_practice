import sys
import os

if "--help" in sys.argv:
    print("""
Usage : python batchFileRename.py <directory_path> <prefix> [--preview | --rename]
Options:
    --preview   Preview the new file names without renaming.
    --rename    Rename the files with the given prefix.
    --help      Show this help messages and exit.

Description: 
    This script renames all files in a directory by adding a prefix . 

Example:
    python batchFileRename.py --help
    python batchFileRename.py ./test_folder new_ --preview
    python batchFileRename.py ./test_folder new_ --rename
                       
""")
    sys.exit(0)

if len(sys.argv) != 4 or sys.argv[3] not in ["--preview", "--rename"]:
    print("Error: Invalid Arguments. Use '--help' to see usage instructions. ")
    sys.exit(1)

directory = sys.argv[1]
prefix = sys.argv[2]
flag = sys.argv[3]

if not os.path.isdir(directory):
    print("Erorr: Directory not found. ")

files = os.listdir(directory)

for file in files:

    new_name = prefix + file

    if flag == "--preview":
        print(f"Preview {file} -> {new_name}")
    elif flag == "--rename":
        os.rename(os.path.join(directory, file), os.path.join(directory, new_name))
        print(f"Renamed: {file} -> {new_name}")
    