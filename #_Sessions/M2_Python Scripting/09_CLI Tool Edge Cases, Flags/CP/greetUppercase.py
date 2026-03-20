import sys

if "--help" in sys.argv:
    print("""
Usage : python greetupperCase.py [--uppercase] <name>
Options:
    --uppercase display name in uppercase
    --help      Show this help messages and exit.

Description: 
    This script greet the user in uppercase name 

Example:
    python greetUppercase.py --help
    python greetUppercase.py --uppercase Alice
                       
""")
    sys.exit(0)

if len(sys.argv) < 2 or len(sys.argv) >3:
    print("Error: Missing Arguments. Use '--help' to see usage instructions. ")
    sys.exit(1)

if "--uppercase" in sys.argv:
    name = sys.argv[2].upper()

else:
    name = sys.argv[1]
print(f"Hello, {name}!")