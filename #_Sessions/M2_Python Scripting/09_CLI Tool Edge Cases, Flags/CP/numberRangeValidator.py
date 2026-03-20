import sys

if "--help" in sys.argv:
    print("""
Usage : python numberRangeValidator.py <number> --min <min_Value> --max <max_value> 
Options:
    --min   Specify the minimum valid value 
    --max   Specify the maximum valid value 
    --help  Show this help messages and exit.

Description: 
    This script validates if a given number is within specified range 

Example:
    python numberRangeValidator.py 5 --min 1 --max 10
    python numberRangeValidator.py 15 --min 1 --max 10
                       
""")
    sys.exit(0)

if len(sys.argv) != 6 or "--min" not in sys.argv or "--max" not in sys.argv:
    print("Error: Missing Arguments. Use '--help' to see usage instructions. ")
    sys.exit(1)

try:
    number = int(sys.argv[1])
    min_value = int(sys.argv[sys.argv.index("--min") + 1])
    max_value = int(sys.argv[sys.argv.index("--max") + 1])
except ValueError:
    print("Error: Provise a valid number. ")
    sys.exit(1)

if min_value <= number <= max_value:
    print(f"{number} is within the range [{min_value}, {max_value}].")
else:
    print(f"{number} is outside the range [{min_value}, {max_value}].")


"""
python numberRangeValidator.py 5 --min 1 --max 10
5 is within the range [1, 10]

python numberRangeValidator.py 15 --min 1 --max 10
15 is outside the range [1, 10].

"""