import sys
import os

if len(sys.argv) < 2:
    print("Error: You must provide a file path.")
    sys.exit(1)  # Exit with error code

file_path = sys.argv[1]

if not os.path.isfile(file_path):
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)  # Exit with error code/

print(f"✅ File '{file_path}' found. Continuing...")