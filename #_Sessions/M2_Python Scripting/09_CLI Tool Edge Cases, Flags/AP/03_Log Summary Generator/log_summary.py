import sys
import os

VALID_FLAGS = {
    "--info": "INFO",
    "--warning": "WARNING",
    "--error": "ERROR",
    "--critical": "CRITICAL"
}

if "--help" in sys.argv:
    print("""
Usage : python log_summary.py <directory_path> [error] 
Options:
    --info      Show only INFO messages.
    --warning   Show only WARNING messages.
    --error     show only ERROR messages.
    --critical  show only CRITICAL messages.
    --help      Show this help messages and exit.

Description: 
    Filter log entries by severity level (`INFO`, `WARNING`, `ERROR`, `CRITICAL`) using flags.
    If **no filter flags** are provided, all log messages should be displayed.
    If an **invalid flag** is passed or if the **file doesn't exist**, display an error message.

Example:
    python log_summary.py --help
    python log_summary.py ./logs.txt --warning                 
""")
    sys.exit(0)

args = sys.argv[1:]

# Check if at least file path is provided
if not args:
    print("Log file path not given. ")
    print("Usage: python log_summary.py <logfile> [--info|--warning|--error|--critical]")
    sys.exit(1)

logFile_path = args[0]
flags = args[1:]

selected_flags = []

for flag in flags:
    if flag in VALID_FLAGS:
        selected_flags.append(VALID_FLAGS[flag])
    
    else:
        print(f"Error: Unknown flag '{flag}'. Use '--help' for instructions.")
        sys.exit(1)


# Check file existence
if not os.path.isfile(logFile_path):
    print(f"Error: File '{logFile_path}' not found.")
    sys.exit(1)

# reading the content of file 
with open(logFile_path, "r") as log_file:
    content_log = log_file.readlines()

# Create dictionaries to store counts and last entries
counts = {"INFO": 0, "WARNING": 0, "ERROR": 0, "CRITICAL": 0}
last_entries = {"INFO": "", "WARNING": "", "ERROR": "", "CRITICAL": ""}

for line in content_log:      # Go through each line
    clean_line = line.strip()
    for flags_select in selected_flags:  # Check each selected level
        if flags_select in line:    # if selected flag is in line 
            counts[flags_select] += 1
            last_entries[flags_select] = line
            break

print("Summary Report! ")
print("-"*20)
for flags_select in selected_flags:
    count = counts[flags_select]
    occ_str = "occurrence"
    print(f"{flags_select:<9} {count} {occ_str:<11} | Last Entry: {last_entries[flags_select]}")

"""
python log_summary.py logs.txt --error --info --warning
Summary Report!
--------------------
ERROR     2 occurrence  | Last Entry: [2024-02-01 10:10:05] ERROR: File missing in directory assets/

INFO      2 occurrence  | Last Entry: [2024-02-01 10:08:45] INFO: Render completed for shot_001

WARNING   2 occurrence  | Last Entry: [2024-02-01 10:11:20] WARNING: Disk space running low


"""

