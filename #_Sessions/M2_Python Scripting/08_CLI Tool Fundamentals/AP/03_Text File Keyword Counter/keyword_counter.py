import sys 

if len(sys.argv) < 3:
    print("Usage: python keyword_Counter.py is not found. ")

else:
    file_path = sys.argv[1]
    keyword_to_search = sys.argv[2]
    word_count = 0

    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            for line in lines:
                if keyword_to_search in line:
                    word_count +=1
        print(f"Number of Words ,{keyword_to_search} : {word_count}")
    except FileNotFoundError:
        print(f"Error: File '{file_path}' no found!.")
