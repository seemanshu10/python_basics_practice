import sys

if "--help" in sys.argv:
    print("""
Usage : python toggleDebug.py [--debug ]
          
Options:
    --debug     Enable Debug mode        
    --help      Show this help messages and exit.

Description: 
    This script toggle a debug mode based ion the presence of --debug flag.

Example:
    python toggleDebug.py --debug
    python toggleDebug.py
                       
""")
    sys.exit(0)


if "--debug" in sys.argv:
    print(f"Debug mode is ON.")
else:
    print(f"Debug mode is OFF.")
