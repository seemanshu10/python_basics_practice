# Create a Student Record System
class Student:

    def __init__(self, student_name, student_grade_level, student_marks):

        self.student_name = student_name
        self.student_grade_level = student_grade_level
        self.student_marks = student_marks

    def display_summary(self):

        average_marks = sum(self.student_marks) / len(self.student_marks)
        print(f"Student: {self.student_name} | Grade: {self.student_grade_level} | Average Mark: {average_marks:.2f}")

    def add_mark(self, marks_to_add):
        self.student_marks.append(marks_to_add)

# obeject instantiate 
# creating student objects 
student1 = Student("Aria", 10, [80, 90])
student2 = Student("Leo", 12, [75, 82])

# Display summaries
student1.display_summary()
student2.display_summary()

# Add New marks and display summaries again
print("Adding new mark to Aria...")
student1.add_mark(95)
student1.display_summary()

print("Adding new mark to Leo...")
student2.add_mark(83)
student2.display_summary()
        
"""
Student: Aria | Grade: 10 | Average Mark: 85.00
Student: Leo | Grade: 12 | Average Mark: 78.50
Adding new mark to Aria...
Student: Aria | Grade: 10 | Average Mark: 88.33
Adding new mark to Leo...
Student: Leo | Grade: 12 | Average Mark: 80.00
"""
        