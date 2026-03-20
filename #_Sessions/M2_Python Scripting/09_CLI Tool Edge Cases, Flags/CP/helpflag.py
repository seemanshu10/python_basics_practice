# simple script for herlp flag 

import sys

if "--help" in sys.argv:
    print("""
Usage : python helpfalg.py [--help]

Options:
    --help      Show this help messages and exit.

Description: 
    This script demonstrates how to use thje --help glag in a python script. 

Example:
    python helpflag.py --help
                       
""")
    sys.exit(0)

print("Run this script with '--help' to see usage instructions. ")

"""
python helpflag.py --help

Usage : python helpfalg.py [--help]

Options:
    --help      Show this help messages and exit.

Description: 
    This script demonstrates how to use thje --help glag in a python script. 

Example:
    python helpflag.py --help
    
"""