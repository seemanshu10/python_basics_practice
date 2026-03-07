'''

### 🎯 AP. Student Grades Management


#### Task Objective

In this task, you will:

* Read structured student grade data from a file.
* Organize and store data using Python dictionaries and lists.
* Calculate the average grade for each student using basic loops.
* Write the processed results to a new file.

This task helps build foundational skills in file I/O and basic data processing using core Python structures.


#### Instructions

1. **Create the Input File**
   Create a file named `students.txt` with the following structure:

   ```+
   student_id,student_name,grade1,grade2,grade3
   1,John Doe,85,78,92
   2,Jane Smith,90,88,79
   3,Sam Brown,70,85,82
   ```

2. **Read Student Data**
   Write a function `read_student_data(file_path)` that reads the data from the file and stores each student in a dictionary with:

   * `student_id`
   * `student_name`
   * `grades` (a list of three integers)

3. **Calculate Averages**
   Write a function `calculate_averages(students)` that loops through the list of grades manually (do not use `sum()`) and adds a new key `average_grade` to each student dictionary.

4. **Write the Output File**
   Write a function `write_averages_to_file(students, output_file_path)` that creates a new file named `averages.txt` with this format:

   ```
   student_name,average_grade
   John Doe,85.0
   Jane Smith,85.67
   Sam Brown,79.0
   ```

5. **Create the Main Function**
   Write a `main()` function to call all the above in order and run the script.


#### Sample Output

**Input (`students.txt`):**

```
student_id,student_name,grade1,grade2,grade3
1,John Doe,85,78,92
2,Jane Smith,90,88,79
3,Sam Brown,70,85,82
```

**Output (`averages.txt`):**

```
student_name,average_grade
John Doe,85.0
Jane Smith,85.67
Sam Brown,79.0
```

'''


def read_student_data(file_path):

    students = []
    # reading  file  and printing 
    with open (file_path,"r") as file:
        lines = file.readlines()
        print(lines)

    # skip header line as that is not needed 
    
    for line in lines[1:]:
        # splittimg by comma 
        each_student_data = line.strip().split(",")

        student = {
            "student_id": int(each_student_data[0]),
            "student_name": each_student_data[1],
            "grades": [
                int(each_student_data[2]),
                int(each_student_data[3]),
                int(each_student_data[4])
            ]
        }

        students.append(student)

    return students

# Camlulating Average of students score 
def calculate_averages(students):
    for student in students:
        total = 0
        count = 0

        for grade in student["grades"]:
            total = total + grade
            count = count + 1

        student["average_grade"] = round(total / count, 2) 


def write_averages_to_file(students, output_file_path):
    file = open(output_file_path, "w")
    file.write("student_name,average_grade\n")

    for student in students:
        file.write(student["student_name"] + "," + str(student ["average_grade"]) + "\n")

    file.close()


def main():
    students = read_student_data(r"#_Sessions\M1_Python Basics\09_File Handling\AP\students.txt")
    calculate_averages(students)
    write_averages_to_file(students, r"#_Sessions\M1_Python Basics\09_File Handling\AP\averages.txt")

main()
