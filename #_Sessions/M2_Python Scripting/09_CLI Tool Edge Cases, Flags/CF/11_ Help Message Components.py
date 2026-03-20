import sys

help_msg = """

Usage: 
  script.py [OPTIONS] <file_path> <filter_keyword>

Options:
  --help        Show this help message and exit
  --verbose     Enable detailed output
  --filter=TYPE Specify a filter type (e.g., INFO, ERROR)

Arguments:
  <file_path>      The path to the input file
  <filter_keyword> Keyword to filter (e.g., INFO, ERROR)

Examples:
  script.py logs.txt INFO
  script.py --verbose logs.txt ERROR
  script.py --help
"""

if "--help" in sys.argv:
    print(help_msg)
    sys.exit(0)

print("Program running...")
