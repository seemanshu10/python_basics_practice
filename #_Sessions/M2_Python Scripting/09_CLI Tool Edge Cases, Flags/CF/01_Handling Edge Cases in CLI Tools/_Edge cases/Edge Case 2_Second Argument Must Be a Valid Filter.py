import sys

try:
    first_arg = sys.argv[1]
    with open(first_arg, 'r') as f:
        data = f.readlines()
except FileNotFoundError:
    print("ERROR: A valid file path is expected as the first argument.")
    sys.exit(1)  


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
