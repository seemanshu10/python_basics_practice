## 🎯 AP. Student Record System

### Task Objective

* Create a class to represent student records.
* Include properties to store student details.
* Add functionality to display a student’s summary.
* Add functionality to update a student’s marks.
* Test the system with multiple student entries.

### Instructions

* Create a class called `Student` that takes three values during object creation: `name`, `grade_level`, and `marks` (as a list of integers).
* Inside the class, create a method that prints the student's name, grade, and their average mark.
* Add another method that takes a new mark as input and adds it to the existing list of marks.
* Create at least two different student objects and test both methods to confirm they work as expected.

### Sample Output

**Usage**

```python
# Create student objects
student1 = Student("Aria", 10, [80, 90])
student2 = Student("Leo", 12, [75, 82])

# Display summaries
student1.display_summary()
student2.display_summary()

# Add new marks and display summaries again
print("Adding new mark to Aria...")
student1.add_mark(95)
student1.display_summary()

print("Adding new mark to Leo...")
student2.add_mark(83)
student2.display_summary()
```

**Output**

```
Student: Aria | Grade: 10 | Average Mark: 85.0
Student: Leo | Grade: 12 | Average Mark: 78.5
Adding new mark to Aria...
Student: Aria | Grade: 10 | Average Mark: 88.3
Adding new mark to Leo...
Student: Leo | Grade: 12 | Average Mark: 80.0
```
