"""
Docstring for Loops.CP.DictinaryFor
"""

# iterating dictionary 

student_grades = {
    'Alice':85,
    'Bob':90
}

for grade in student_grades.values():
    print(grade)

# output 
#85
#90

# iterating over key value pairs 
student_grades = {
    'Alice':85,
    'Bob':90
}

for stu,grade in student_grades.items():
    print(f"{stu}:{grade}")
"""
Alice:85
Bob:90
"""

