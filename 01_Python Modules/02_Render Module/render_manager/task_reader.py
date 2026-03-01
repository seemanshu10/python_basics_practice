"""
write a function to read all tasks from a given file and return them as a list of strings.
"""

def read_tasks(file_path):
    # Create an empty list to store tasks
    tasks = []
    # Open the file in read mode
    file = open(file_path, 'r')

    # Read each line one by one
    for line in file:
        # Remove extra spaces and newline characters
        clean_line = line.strip()

        # Only add the line if it is not empty
        if clean_line != "":
            tasks.append(clean_line)

    # Close the file after reading
    file.close()

    # Return the list of tasks
    return tasks