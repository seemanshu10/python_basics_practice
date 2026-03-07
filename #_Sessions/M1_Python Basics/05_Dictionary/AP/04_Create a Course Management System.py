"""
Task Objective:
• Create a nested dictionary named course_data to manage university course enrollments.
• Store structured details like instructor, credits, and enrolled_students.
• Modify the student list and course details.
• Add a new course with complete data.
• Access data from a course that may not exist using the get() method.

📝 Instructions:
• Define a dictionary named course_data with at least two courses: CS101 and MATH123.
  - Each should store:
    • instructor (string)
    • credits (int)
    • enrolled_students (list of strings)
• Add a new student to the enrolled_students list for CS101.
• Update the number of credits for MATH123.
• Add a new course PHY202 with full details.
• Print the entire updated dictionary.
• Use the get() method to check if a course BIO150 exists and return "Course not available" if not.

💡 Sample Output:

Updated CS101: ['Alice', 'Bob', 'Charlie']  
Updated MATH123 credits: 4  
Added course PHY202: {'instructor': 'Dr. Lee', 'credits': 3, 'enrolled_students': ['Sam', 'Nina']}

Full Course Data:  
{'CS101': {'instructor': 'Dr. Smith', 'credits': 3, 'enrolled_students': ['Alice', 'Bob', 'Charlie']},  
 'MATH123': {'instructor': 'Dr. Brown', 'credits': 4, 'enrolled_students': ['Tom']},  
 'PHY202': {'instructor': 'Dr. Lee', 'credits': 3, 'enrolled_students': ['Sam', 'Nina']}}

BIO150: Course not available
"""

course_data = {
    'CS101': {'instructer': 'Macky', 'Credits': 4, 'enrolled_students': ["Alice", "Bob"]},
    'MATH123': {'instructer': 'David', 'Credits': 5, 'enrolled_students': ["Ricky","Manav","Macky"]},
}

print(course_data)
# Add a new student to the enrolled_students list for CS101.
course_data["CS101"]["enrolled_students"].append("Charlie")
Course_Values = course_data["CS101"]["enrolled_students"]
print("Updated CS101:",Course_Values)
# Updated CS101: ['Alice', 'Bob', 'Charlie']

cred_math=course_data["MATH123"]["Credits"] = "6"
print("Updated MATH123 credits is: ",cred_math )
# Updated MATH123 credits is:  6

new_course = {
    'PHY202': {'instructer': 'Dr. Lee', 'Credits': 3, 'enrolled_students':  ['Sam', 'Nina']}
}

course_data.update(new_course)
print("Added Course ",new_course)

print("\n Full Course data :\n", course_data)
# Full Course data :
# {'CS101': {'instructer': 'Macky', 'Credits': 4, 'enrolled_students': ['Alice', 'Bob', 'Charlie']}, 'MATH123': {'instructer': 'David', 'Credits': '6', 'enrolled_students': ['Ricky', 'Manav', 'Macky']}, 'PHY202': {'instructer': 'Dr. Lee', 'Credits': 3, 'enrolled_students': ['Sam', 'Nina']}}

course_BIO150 = course_data.get("BIO150","Course not available")
print("BIO150: ",course_BIO150)
# BIO150:  Course not available
