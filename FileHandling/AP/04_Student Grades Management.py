"""
Student Grades Management


#### Task Objective

In this task, you will:

* Read structured student grade data from a file.
* Organize and store data using Python dictionaries and lists.
* Calculate the average grade for each student using basic loops.
* Write the processed results to a new file.
"""

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
    students = read_student_data("FileHandling/AP/students.txt")
    calculate_averages(students)
    write_averages_to_file(students, "FileHandling/AP/averages.txt")


main()
