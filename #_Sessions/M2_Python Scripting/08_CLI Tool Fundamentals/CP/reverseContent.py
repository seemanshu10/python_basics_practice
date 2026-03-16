import sys 

if len(sys.argv) < 2:
    print("Usage: python reverseContent.py is not found. ")

else:
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                print(line.strip()[::-1])
    except FileNotFoundError:
        print(f"Error: File '{file_path}' no found!.")