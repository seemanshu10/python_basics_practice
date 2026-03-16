import sys 

if len(sys.argv) < 2:
    print("Usage: python averageMarks.py is not found. ")

else:
    file_path = sys.argv[1]
    try:
        with open(file_path, 'r') as file:
            marks = [float(line.strip()) for line in file if line.strip()]
            if marks:
                average = sum(marks) / len(marks)
                print(f"Average Marks: {average:.2f}")
            else:
                print("No mrks found in the file.")
            
    except FileNotFoundError:
        print(f"Error: File '{file_path}' no found!.")
    except ValueError:
        print(f"Error: File contains invalid marks.")