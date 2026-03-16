import sys 

if len(sys.argv) < 3:
    print("Usage: python search_in_File is not found. ")

else:
    file_path = sys.argv[1]
    keyword = sys.argv[2]

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if keyword in line:
                    print(line.strip())

    except FileNotFoundError:
        print(f"Error: File '{file_path}' no found!.")
