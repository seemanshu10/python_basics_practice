import sys

first_arg = sys.argv[1]

with open(first_arg, 'r') as f:
    data = f.readlines()
    
second_arg = sys.argv[2]

if second_arg == "INFO":
    for each_line in data:
        if "INFO" in each_line.strip():
            print(each_line.strip())
            
# if second_arg == "CRITICAL":
#     for each_line in data:
#         if "CRITICAL" in each_line.strip():
#             print(each_line.strip())