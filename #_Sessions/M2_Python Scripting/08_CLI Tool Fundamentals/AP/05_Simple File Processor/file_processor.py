import sys
import os

if len(sys.argv) < 3:
    print("Please provide a file name.")
    sys.exit(1)

file_path = sys.argv[1].lower()

# Check if file exists
if not os.path.isfile(file_path):
    print("Error: File does not exist")
    sys.exit(1)

else:
    try:
        operation = sys.argv[2].lower()
        if operation == 'char':
            count_char = 0
            with open(file_path, "r", encoding="utf-8") as file:
                char_data = file.read()
            # print(content_data)
            for line in char_data:
                count_char += 1

            print(f"Number of char: {count_char}")

        elif operation == 'words':
            count_words = 0
            with open(file_path, "r", encoding="utf-8") as file:
                words_data = file.readlines()
            for words in words_data:
                words = words.split()
                count_words += len(words)

            print(f"Number of words: {count_words}")

        elif operation == 'lines':
            
            with open(file_path, "r", encoding="utf-8") as lines_file:
                lines_data = lines_file.readlines()
            line_count = len(lines_data)
            print(f"Number of lines: {line_count}")

        else:
            print(f"Error: Unknown operation '{operation}'. Use char | words | lines")
            sys.exit(1)

    except FileNotFoundError:
        print(f"Error: File '{file_path}' not found.")
        sys.exit(1)

"""
python file_processor.py sample.txt char 
Number of char: 236


 python file_processor.py sample.txt words
Number of words: 38

python file_processor.py sample.txt lines
Number of lines: 7
"""