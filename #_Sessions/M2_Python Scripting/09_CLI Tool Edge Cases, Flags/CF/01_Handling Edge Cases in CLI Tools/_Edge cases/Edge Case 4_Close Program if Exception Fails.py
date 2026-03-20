import sys
import os

try:
    if len(sys.argv) < 3:
        raise ValueError("ERROR: At least two arguments are required: a file path and a filter (INFO/ERROR).")
    if len(sys.argv) > 3:
        raise ValueError("ERROR: Too many arguments. Only two arguments are allowed.")

    first_arg = sys.argv[1]
    if not os.path.isfile(first_arg):
        raise FileNotFoundError(f"ERROR: The file '{first_arg}' does not exist. Please provide a valid file path.")

    with open(first_arg, 'r') as f:
        data = f.readlines()

    second_arg = sys.argv[2]
    accepted_args = ["INFO", "ERROR"]

    if second_arg not in accepted_args:
        raise ValueError(f"Invalid argument: {second_arg}. Accepted values are 'INFO' or 'ERROR'.")

    if second_arg == "INFO":
        for each_line in data:
            if "INFO" in each_line.strip():
                print(each_line.strip())
    elif second_arg == "ERROR":
        for each_line in data:
            if "ERROR" in each_line.strip():
                print(each_line.strip())

except ValueError as ve:
    print(ve)
    sys.exit(1)

except FileNotFoundError as fnfe:
    print(fnfe)
    sys.exit(1)

except Exception as e:
    print(f"An unexpected error occurred: {e}")
    sys.exit(1)