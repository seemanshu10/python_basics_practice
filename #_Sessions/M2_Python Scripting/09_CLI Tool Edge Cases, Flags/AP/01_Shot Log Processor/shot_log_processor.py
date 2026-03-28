import sys
import os


def main():

    if "--help" in sys.argv:
        print("""
        Usage : python shot_log_processor.py <log_path> <prefix> [--preview | --rename]
        Options:
            --preview   Preview the new file names without renaming.
            --rename    Rename the files with the given prefix.
            --help      Show this help messages and exit.

        Description: 
            This script renames all files in a directory by adding a prefix . 

        Example:
            python  .\shot_log_processor.py --help
            python  .\shot_log_processor.py .\shot_log_processor.py --preview
            python  .\shot_log_processor.py .\shot_log_processor.py --rename
                            
        """)
        sys.exit(0)

    try:
        args = sys.argv[1:] 

        if len(args) < 2:
            print("ERROR: At least two arguments are required: a file path and a filter keyword.")
            return
        elif len(args) > 2:
            print("ERROR: Too many arguments. Only two arguments are allowed.")
            return

        file_path, keyword = args

        # Validate keyword
        valid_keywords = ["RENDERED", "FAILED"]
        if keyword not in valid_keywords:
            print(f"ERROR: Invalid filter: {keyword}. Accepted values are 'RENDERED' or 'FAILED'.")
            return

        # Check if file exists
        if not os.path.isfile(file_path):
            print(f"ERROR: The file '{file_path}' does not exist. Please provide a valid file path.")
            return

        # Read and filter file
        with open(file_path, "r") as file_log:
            for line in file_log:
                if keyword in line:
                    print(line.strip())

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()

"""
python .\shot_log_processor.py .\shots.log RENDERED
SHOT_001 RENDERED
SHOT_003 RENDERED
SHOT_005 RENDERED

python .\shot_log_processor.py .\shots.log FAILED  
SHOT_002 FAILED
SHOT_004 FAILED

python .\shot_log_processor.py .\shots.log       
ERROR: At least two arguments are required: a file path and a filter keyword.

python .\shot_log_processor.py .\shots.log failed
ERROR: Invalid filter: failed. Accepted values are 'RENDERED' or 'FAILED'.
"""