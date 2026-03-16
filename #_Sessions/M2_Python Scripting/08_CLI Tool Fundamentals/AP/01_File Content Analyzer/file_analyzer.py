import sys
import os

if len(sys.argv) < 2:
    print("Please provide a file name.")
    sys.exit(1)

file_path = sys.argv[1]

# Check if file exists
if not os.path.isfile(file_path):
    print("Error: File does not exist")
    sys.exit(1)

word_count = 0
char_count = 0
line_count = 0

try:
    with open(file_path, "r", encoding="utf-8") as file:
        for line in file:
            line_count += 1
            char_count += len(line)

            # Remove punctuation 
            clean_line = ""
            for ch in line:
                if ch.isalnum():
                    clean_line += ch

            clean_line = clean_line.lower()
            words = clean_line.split()
            word_count += len(words)

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

print("File Analysis Results")
print("---------------------")
print(f"Lines: {line_count}")
print(f"Words: {word_count}")
print(f"Characters (including spaces): {char_count}")

"""
python file_analyzer.py sample.txt              
File Analysis Results
---------------------
Lines: 7
Words: 37
Characters (including spaces): 236
"""