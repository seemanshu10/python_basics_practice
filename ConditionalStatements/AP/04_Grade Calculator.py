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