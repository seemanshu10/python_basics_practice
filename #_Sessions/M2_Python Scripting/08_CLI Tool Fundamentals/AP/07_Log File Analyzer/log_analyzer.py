import sys
from colorama import Fore, Style, init

# reset to default after every print 
init(autoreset=True)

VALID_STATUSES = {"ERROR", "INFO", "WARNING", "--ERROR"}

def main():
    if len(sys.argv) != 3:
        print("Usage: python organize_directory.py <log_file> <STATUS>")
        print("Example: python organize_directory.py logs.txt ERROR")
        sys.exit(1)

    log_file = sys.argv[1]
    status_log = sys.argv[2].upper()
    
    # Validate status input
    if status_log not in VALID_STATUSES:
        print(f"Invalid status '{status_log}'.")
        print(f"Allowed values: {', '.join(VALID_STATUSES)}")
        sys.exit(1)

    try:
        with open(log_file, 'r') as log_file:
            log_data = log_file.readlines()

    except FileNotFoundError:
        print(f"Unexpected error while reading file: {e}")
        sys.exit(1)

    # print(log_data)
    for log in log_data:
        # print(log)
        line = log.strip()

        # Split into two parts from : on first instance 
        line_split = line.split(": ", 1)[0]
        # print(line_split)
        # check what error occurs 
        if status_log == line_split:
            # print(log, end = " ")
            if status_log == "ERROR":
                print(Fore.RED + Style.BRIGHT + line )
                
            elif status_log == "INFO":
                print(Fore.GREEN + Style.BRIGHT + line )

            elif status_log == "WARNING":
                print(Fore.YELLOW + Style.BRIGHT + line )
           
if __name__ == "__main__":
    main()

"""
python log_analyzer.py system.log errOr                    
ERROR: Failed to connect to the database.
ERROR: User authentication failed.
ERROR: Timeout while waiting for server response.

INFO: System started successfully.
INFO: User logged in.
INFO: Connection timeout after 30 seconds.
INFO: Scheduled job completed.
"""