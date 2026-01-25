"""
Nested Dictinaries  : Dictinaries inside dictionary
"""

# Creating A Simple Nested Dict. 

student = {
    "name":"John",
    "details":{
        "age":12,
        "grade":"A"
    }
}
print(student)

# {'name': 'John', 'details': {'age': 12, 'grade': 'A'}}

# Modifying nested Value 

student = {
    "name":"John",
    "details":{
        "age":12,
        "grade":"A"
    }
}

student["details"]["grade"] = "B+"
print(student)

# {'name': 'John', 'details': {'age': 12, 'grade': 'B+'}}

# Accessing nested Value in a classroom Dictionary

classRoom = {
    "class_name":"Physics",
    "students":{
        "student1":{"name":"Alice","age":20},
        "student2":{"name":"Bob","age":12},
        "student3":{"name":"David","age":21}
    }
}

student_name = classRoom["students"]["student3"]["name"]
print (student_name) # David

# Adding A New Key Value pair to a nested dictionary 

employee = {
    "name":"Emma",
    "position":"Manager",
    "projects":{
        "Current":["Project A","Project B"],
        "Completed":["Project X"]
    }
}

employee["projects"]["Current"].append("Project C")

print(employee)

# Output : {'name': 'Emma', 'position': 'Manager', 'projects': {'Current': ['Project A', 'Project B', 'Project C'], 'Completed': ['Project X']}}

# creating Nested Dictionary for a classroom 
# Modyfying A nested Vlaue in nested dictinary 
classRoom = {
    "class_name":"Physics",
    "students":{
        "student1":{"name":"Alice","age":20},
        "student2":{"name":"Bob","age":12},
        "student3":{"name":"David","age":21}
    }
}
print (classRoom)
# Output : {'class_name': 'Physics', 'students': {'student1': {'name': 'Alice', 'age': 20}, 'student2': {'name': 'Bob', 'age': 12}, 'student3': {'name': 'David', 'age': 21}}}
classRoom["students"]["student1"]["Age"] = 22
print(classRoom)

# Output : {'class_name': 'Physics', 'students': {'student1': {'name': 'Alice', 'age': 20, 'Age': 22}, 'student2': {'name': 'Bob', 'age': 12}, 'student3': {'name': 'David', 'age': 21}}}
