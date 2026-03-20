import os
import sys

first_arg = sys.argv[1]

# Check if the file exists
if not os.path.isfile(first_arg):
    print(f"ERROR: The file '{first_arg}' does not exist. Please provide a valid file path.")
    sys.exit(1)


with open(first_arg, 'r') as f:
    data = f.readlines()

second_arg = sys.argv[2]

if second_arg == "INFO":
    for each_line in data:
        if "INFO" in each_line.strip():
            print(each_line.strip())

if second_arg == "ERROR":
    for each_line in data:
        if "ERROR" in each_line.strip():
            print(each_line.strip())
