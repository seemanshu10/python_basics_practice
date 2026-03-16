import sys 

if len(sys.argv) < 2:
    print("Usage: python wordCount.py is not found. ")

else:
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            lines = file.read()
            words = lines.split()
            print(f"THe file contains {len(words)} words.")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' no found!.")