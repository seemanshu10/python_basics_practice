import sys

if "--help" in sys.argv:
    print("""
Usage : python palindromeChecker.py <word> [--ignore-case] 
Options:
    --ignore-case   ignore case when checking for palindrome.
    --help          Show this help messages and exit.

Description: 
    This script checks number is palindrome.

Example:
    python palindromeChecker.py racecar
    python palindromeChecker.py Racecar --ignore-case
                       
""")
    sys.exit(0)

if len(sys.argv) < 2 or len(sys.argv) >3:
    print("Error: Missing Arguments. Use '--help' to see usage instructions. ")
    sys.exit(1)

word = sys.argv[1]

if "--ignore-case" in sys.argv:
    word = word.lower()

if word == word[::-1]:
    print(f"'{sys.argv[1]}' is a palindrome. ")
else:
    print(f"'{sys.argv[1]}' is not a palindrome. ")

"""
 python .\palindromeChecker.py racecar                   
'racecar' is a palindrome. 

python .\palindromeChecker.py Racecar --ignore-case
'Racecar' is a palindrome. 
"""