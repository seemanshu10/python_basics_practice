import sys

if "--help" in sys.argv:
    print("""
Usage : python squareCube.py [--square | --cube] <number>
Options:
    --cube      Calculate cube   
    --help      Show this help messages and exit.

Description: 
    This script demonstrates how to use thje --help glag in a python script. 

Example:
    python helpflag.py --help
                       
""")
    sys.exit(0)

if len(sys.argv) != 3:
    print("Error: Missing Arguments. Use '--help' to see usage instructions. ")
    sys.exit(1)

flag = sys.argv[1]

try:
    number = float(sys.argv[2])
except ValueError:
    print("Error: Provise a valid number. ")
    sys.exit(1)

if flag == "--square":
    print(f"The Square of {number} is {number ** 2}")
elif flag == "--cube":
    print(f"The Cube of {number} is {number ** 3}")
else:
    print("Error: Unknown flag. Use '--help' for instructions")
"""
python squareCube.py --square 3
The Square of 3.0 is 9.0

 python squareCube.py --cube 3  
The Cube of 3.0 is 27.0
"""