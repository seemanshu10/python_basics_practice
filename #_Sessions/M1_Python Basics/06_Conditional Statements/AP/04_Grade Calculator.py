"""
# Description of the Task
Create a Python program that takes a student's marks as input and prints the corresponding grade based on predefined criteria.

# Instructions
Prompt the user to enter the student's marks (a number between 0 and 100).
Use if-else statements to determine the grade based on the following criteria:
A: 90-100
B: 80-89
C: 70-79
D: 60-69
F: below 60
Print the corresponding grade.

# Learning Objective
To practice using if-else statements.
To understand how to implement conditional logic in a Python program.
To gain experience with basic input and output operations in Python.

# Sample Usage
Enter the student's marks: 85
Grade: B
Enter the student's marks: 72
Grade: C
Enter the student's marks: 59
Grade: F
"""

"""
 program that takes a student's marks as input and prints the corresponding grade based on predefined criteria.
"""
# Enter the user input 
marks = int(input("Enter the student's marks: "))

# Checking The Grades 
if 90<=marks>=100 :
    print("Grade: A")
elif 80<=marks>=89 :
    print("Grade: B")
elif 70<=marks>=79 :
    print("Grade: C")
elif 60<=marks>=69 :
    print("Grade: D")
else:
    print("Grade: E ")

"""
Output:
Enter the student's marks: 89
Grade: B
Enter the student's marks: 72
Grade: D
Enter the student's marks: 59
Grade: E
"""