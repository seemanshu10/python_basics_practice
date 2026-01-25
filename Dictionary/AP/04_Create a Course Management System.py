"""
 Create a nested dictionary named course_data to manage university course enrollments.
• Store structured details like instructor, credits, and enrolled_students.
• Modify the student list and course details.
• Add a new course with complete data.
• Access data from a course that may not exist using the get() method.
"""

course_data = {
    'CS101': {'instructer': 'Macky', 'Credits': 4, 'enrolled_students': ["Alice", "Bob"]},
    'MATH123': {'instructer': 'David', 'Credits': 5, 'enrolled_students': ["Ricky","Manav","Macky"]},
}

print(course_data)
# Add a new student to the enrolled_students list for CS101.
course_data["CS101"]["enrolled_students"].append("Charlie")
Course_Values =course_data["CS101"]["enrolled_students"]
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

print("\n Full Course data :\n",course_data)
# Full Course data :
# {'CS101': {'instructer': 'Macky', 'Credits': 4, 'enrolled_students': ['Alice', 'Bob', 'Charlie']}, 'MATH123': {'instructer': 'David', 'Credits': '6', 'enrolled_students': ['Ricky', 'Manav', 'Macky']}, 'PHY202': {'instructer': 'Dr. Lee', 'Credits': 3, 'enrolled_students': ['Sam', 'Nina']}}

course_BIO150 = course_data.get("BIO150","Course not available")
print("BIO150: ",course_BIO150)
# BIO150:  Course not available

