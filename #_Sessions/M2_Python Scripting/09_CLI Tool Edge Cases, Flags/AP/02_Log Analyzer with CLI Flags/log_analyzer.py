import sys
import os

VALID_FLAGS = {
    "--info": "INFO",
    "--warning": "WARNING",
    "--error": "ERROR",
    "--critical": "CRITICAL"
}


OPTIONAL_FLAGS = {"--reverse", "--verbose"}

if "--help" in sys.argv:
    print("""
Usage : python log_analyzer.py <directory_path> [error] 
Options:
    --info      Show only INFO messages.
    --warning   Show only WARNING messages.
    --error     show only ERROR messages.
    --critical  show only CRITICAL messages.
    --reverse   reverse the order of the displayed logs.
    --verbose   show debug info like which file is being opened and what filter is used.
    --help      Show this help messages and exit.

Description: 
    Filter log entries by severity level (`INFO`, `WARNING`, `ERROR`, `CRITICAL`) using flags.
    If **no filter flags** are provided, all log messages should be displayed.
    If an **invalid flag** is passed or if the **file doesn't exist**, display an error message.

Example:
    python log_analyzer.py --help
    python log_analyzer.py ./logs.txt --warning
                       
""")
    sys.exit(0)

args = sys.argv[1:]

# Check if at least file path is provided
if not args:
    print("Log file path not given. ")
    print("Usage: python log_analyzer.py <logfile> [--info|--warning|--error|--critical] [--reverse] [--verbose]")
    sys.exit(1)

logFile_path = args[0]
flags = args[1:]

selected_flags = []
reverse_toggle = False
verbose_toggle = False

for flag in flags:
    if flag in VALID_FLAGS:
        selected_flags.append(VALID_FLAGS[flag])
    elif flag in OPTIONAL_FLAGS:
        if flag == "--reverse":
            reverse_toggle = True
        elif flag == "--verbose":
            verbose_toggle = True
    else:
        print(f"Error: Unknown flag '{flag}'. Use '--help' for instructions.")
        sys.exit(1)

# print(selected_flags, verbose_toggle, reverse_toggle)

# Check file existence
if not os.path.isfile(logFile_path):
    print(f"Error: File '{logFile_path}' not found.")
    sys.exit(1)

# reading the content of file 
with open(logFile_path, "r") as log_file:
    content_log = log_file.readlines()

# variable to store the filtred lines 
filtered_logs_storage = [] 

if selected_flags:
    for line in content_log:      # Go through each line
        clean_line = line.strip()
        # print(clean_line)
        for flags_select in selected_flags:  # Check each selected level
            if flags_select in line:    # if selected flag is in line 
                filtered_logs_storage.append(clean_line)
                break
else:
    # if no filtrer selected add every line at once 
    for line in content_log:
        filtered_logs_storage.append(line.strip())

# Reverse the lines if requested
if reverse_toggle:
    filtered_logs_storage.reverse()

# Print the filtered lines
for line in filtered_logs_storage:
    print(line)