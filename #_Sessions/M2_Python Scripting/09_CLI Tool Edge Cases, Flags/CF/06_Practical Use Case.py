import sys
import os

if len(sys.argv) < 2:
    print("Error: Missing argument 'file_path'.")
    print("Usage: python script.py <file_path>")
    sys.exit(1)  # Exit with error if no file is provided

file_path = sys.argv[1]

if not os.path.exists(file_path) or not os.path.isfile(file_path):
    print(f"Error: File '{file_path}' does not exist or is not a valid file.")
    sys.exit(1)  # Exit with error if file doesn't exist

try:
    with open(file_path, "r", encoding="utf-8") as file:
        content = file.read()
        print(f"📄 Content of {file_path}:\n")
        print(content)
except Exception as e:
    print(f"❌ Error while reading the file: {e}")
    sys.exit(1)  # Exit with error if reading fails


sys.exit(0)