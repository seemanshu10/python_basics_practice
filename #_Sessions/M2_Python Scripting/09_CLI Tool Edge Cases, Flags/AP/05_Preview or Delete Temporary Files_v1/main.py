import os
import sys

def show_help():
    print("""
Usage: python main.py <directory_path> [--delete | --preview] [--ext EXTENSION]

Options:
  --delete       Delete all matching files in the specified directory.
  --preview      List all matching files without deleting them.
  --ext          Specify file extension to target (default: .tmp)
  --help         Show this help message and exit.

Description:
  This script scans a directory recursively and either previews or deletes
  files with a specified extension.

Examples:
  python .\main.py .\temp_project\ --preview
  python .\main.py .\temp_project\ --delete
  python .\main.py .\temp_project\ --preview --ext .tmp
  python .\main.py .\temp_project\ --preview --ext .log
""")

def validate_directory(path):
    if not os.path.isdir(path):
        print("Error: Directory not found.")
        sys.exit(1)

def find_files(directory, extension):
    matches = []
    for root, dirs, files in os.walk(directory):
        # print(f"Root {root}")
        # print(type(root))
        # print(f"dirs {dirs}")
        # print(type(dirs))
        # print(f"files {files}" )
        # print(type(files))
        for file in files:
            if file.endswith(extension):
                full_path = os.path.join(root, file)
                # print(full_path)
                matches.append(full_path)
    
    return matches

def preview_files(files, base_dir):
    if not files:
        print("No matching files found.")
        return

    print("Temporary files found:")
    for file in files:
        rel_path = os.path.relpath(file, base_dir)
        # folder = os.path.dirname(rel_path)
        print(f"{rel_path} ")

    print(f"\nTotal found: {len(files)}")
    

def delete_files(files):
    if not files:
        print("No matching files to delete.")
        return

    deleted_count = 0

    for file in files:
        try:
            os.remove(file)
            deleted_count += 1
        except Exception as e:
            print(f"Failed to delete {file}: {e}")

    print(f"Found: {len(files)}, Deleted: {deleted_count}")


def main():
    args = sys.argv

    if "--help" in args or len(args) < 3:
        show_help()

    directory = args[1]

    # Default extension
    extension = ".tmp"

    # Custom extension support
    if "--ext" in args:
        try:
            ext_index = args.index("--ext") + 1
            extension = args[ext_index]
            if not extension.startswith("."):
                extension = "." + extension
        except IndexError:
            print("Error: Please provide an extension after --ext")
            return

    validate_directory(directory)

    files = find_files(directory, extension)

    if "--preview" in args:
        preview_files(files, directory)
    elif "--delete" in args:
        delete_files(files)
    

if __name__ == "__main__":
    main()