import sys
import os

if len(sys.argv) < 3:
    print("Usage: python script.py <file_path> <operation1> [operation2] ...")
    print("Operations: char | words | lines | longest")
    sys.exit(1)

file_path = sys.argv[1]
operations = sys.argv[2:]

# Check if file exists
if not os.path.isfile(file_path):
    print("Error: File does not exist")
    sys.exit(1)

try:
    with open(file_path, "r", encoding="utf-8") as text_file:
        content_data = text_file.read()

    # pre_calculate everything once 
    char_count = len(content_data)
    words_list = content_data.split()
    word_count = len(words_list)
    line_count = len(content_data.splitlines())
    longest_word = max(words_list, key=len) 

    for operation in operations:
        operation_lower = operation.lower()
        if operation_lower in ["--characters", "-c"]:
            print(f"Number of characters: {char_count}")

        elif operation_lower in ["--words", "-w"]:
            print(f"Number of words: {word_count}")

        elif operation_lower in ["--lines", "-l"]:
            print(f"Number of lines: {line_count}")

        elif operation_lower in ["--longest-word", "-lw"]:
            print(f"Longest word: {longest_word} ({len(longest_word)} characters)")

        else:
            print(f"Error: Unknown operation '{operation}'. Use --char | --words | --lines | --longest")

except FileNotFoundError:
    print(f"Error: File '{file_path}' not found.")
    sys.exit(1)

"""
python text_analyzer.py sample.txt char words
Number of characters: 247
Number of words: 41 

Number of characters: 247
Number of words: 41
Longest word: development, (12 characters)

python text_analyzer.py sample.txt lines words longest
Number of lines: 4
Number of words: 41
Longest word: development, (12 characters)
"""