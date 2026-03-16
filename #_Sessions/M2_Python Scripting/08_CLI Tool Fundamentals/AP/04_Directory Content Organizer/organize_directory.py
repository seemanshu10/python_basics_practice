import sys
import os
import shutil

def organize_directory(directory_path):
    # Check if directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' does not exist.")
        return
    
    files = os.listdir(directory_path)

    # Filter only files (ignore directories)
    filtered_files = []

    for f in files:
        full_path = os.path.join(directory_path, f)

        if os.path.isfile(full_path):
            filtered_files.append(f)

    files = filtered_files

    if not files:
        print("The directory contains no files to organize.")
        return
    # print(files)

    for file in files:
        file_path = os.path.join(directory_path, file)

        # Get file extension
        _, extension = os.path.splitext(file)

        if not extension:
            print(f"Skipped (no extension): {file}")
            continue
        
        # print(extension) # .csv
        extension = extension[1:]  # remove "."
        
        target_folder = os.path.join(directory_path, extension)
    
        # Create extension folder if it doesn't exist
        if not os.path.exists(target_folder):
            os.makedirs(target_folder)

        target_path = os.path.join(target_folder, file)
        # print(target_path)
        # Skip if file already in correct place
        if os.path.exists(target_path):
            print(f"Skipped (already organized): {file}")
            continue

        shutil.move(file_path, target_path)
        print(f"Moved: {file} → {extension}/")

def main():
    if len(sys.argv) != 2:
        print("Usage: python organize_directory.py <directory_path>")
        sys.exit(1)

    directory_path = sys.argv[1]
    organize_directory(directory_path)

if __name__ == "__main__":
    main()

