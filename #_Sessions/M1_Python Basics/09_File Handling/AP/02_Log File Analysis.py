"""
# Description of the Task
In this task, students will analyze a log file containing error messages. 
The program will read the log file, extract the error messages, 
count the occurrences of each error type, and write a summary report to an output file.

# Instructions
Create a text file named log.txt and populate it with log entries. 
Each entry should have a timestamp followed by an error message. 

Example format:
2024-06-01 12:00:00 ERROR: FileNotFound
2024-06-01 12:05:00 ERROR: OutOfMemory
2024-06-01 12:10:00 ERROR: FileNotFound

Write a Python program that:
Opens and reads the log.txt file.
Extracts and counts the occurrences of each error message.
Writes a summary report to a new file called error_summary.txt.
Ensure that the program handles exceptions, such as the input file not existing.

# Example usage:
Create log.txt with the following content:

2024-06-01 12:00:00 ERROR: FileNotFound
2024-06-01 12:05:00 ERROR: OutOfMemory
2024-06-01 12:10:00 ERROR: FileNotFound
2024-06-01 12:15:00 ERROR: NullReference

Run the Python program.
The program creates error_summary.txt with the following content:

FileNotFound: 2
OutOfMemory: 1
NullReference: 1

"""

"""
students will analyze a log file containing error messages. 
The program will read the log file, extract the error messages, 
count the occurrences of each error type, and write a summary report to an output file.
"""
# reading  file  and printing 
error_counts ={}
with open (r"#_Sessions\M1_Python Basics\09_File Handling\AP\log.txt" , "r") as file:
    names = file.readlines()
    print(names)

# we can use with like this so that we open the file and then close the file and can do further operations on it .
for line in names:
    line = line.strip()
    if "ERROR:" in line:
        error_message = line.split("ERROR:")[1].strip()
        error_counts[error_message] = error_counts.get(error_message, 0) + 1

    
# Write  summary report to the output file
with open (r"#_Sessions\M1_Python Basics\09_File Handling\AP\error_summary.txt", "w") as file1:
    for error,count in error_counts.items():
        file1.write(f"{error} : {count}\n")

print(f"Error summary have been written  to '{file1.name}'")