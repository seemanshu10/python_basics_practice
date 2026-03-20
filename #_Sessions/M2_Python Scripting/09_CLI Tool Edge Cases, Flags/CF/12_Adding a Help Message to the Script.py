import sys

# Define the help message
help_text = """
Usage: script.py [OPTIONS] <file_path> <filter_keyword>

Options:
  --help        Show this help message and exit

Arguments:
  <file_path>      The path to the input file
  <filter_keyword> Keyword to filter (e.g., INFO, ERROR)

Examples:
  script.py logs.txt INFO
  script.py --help
"""

# Check if '--help' is present in the arguments
if "--help" in sys.argv:
    print(help_text)
    sys.exit(0)

# Extract and process required arguments
first_arg = sys.argv[1]
with open(first_arg, 'r') as f:
    data = f.readlines()

second_arg = sys.argv[2]
accepted_args = ["INFO", "ERROR"]

if second_arg in accepted_args:
    if second_arg == "INFO":
        for each_line in data:
            if "INFO" in each_line.strip():
                print(each_line.strip())
    elif second_arg == "ERROR":
        for each_line in data:
            if "ERROR" in each_line.strip():
                print(each_line.strip())
else:
    raise ValueError(f"Invalid argument: {second_arg}. Accepted values are 'INFO' or 'ERROR'.")

