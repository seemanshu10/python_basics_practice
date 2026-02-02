"""
students will analyze a log file containing error messages. 
The program will read the log file, extract the error messages, 
count the occurrences of each error type, and write a summary report to an output file.
"""
# reading  file  and printing 
error_counts ={}
with open ("FileHandling/AP/log.txt","r") as file:
    names = file.readlines()
    print(names)

# we can use with like this so that we open the file and then close the file and can do further operations on it .
for line in names:
    line = line.strip()
    if "ERROR:" in line:
        error_message = line.split("ERROR:")[1].strip()
        error_counts[error_message] = error_counts.get(error_message, 0) + 1

    
# Write  summary report to the output file
with open ("FileHandling/AP/error_summary.txt", "w") as file1:
    for error,count in error_counts.items():
        file1.write(f"{error} : {count}\n")

print(f"Error summary have been written  to '{file1.name}'")