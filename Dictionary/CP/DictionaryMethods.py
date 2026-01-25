"""
Method for dictionary 
"""

# Acessing nested Dictinary Values 

student = {
    "Name":"Seemanshu",
    "Grades":{
        "Math":91,
        "Science":89
    }
}

math_grade = student.get("Grades").get("Math")
print(math_grade)
# Output : 90

scince_grade= student.get("Grades").get("Science")
print(scince_grade)
# output : 89

# Accessing a non exitant Value 
# if provide a error or not found message it will print the message instead of goving keyError 

car = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2021
}
color = car.get("Color","Not Found ")
print(color) # Not Found

# using keys with empty dictionary 

empty_dict = {}

empt_keys = empty_dict.keys()
print(empt_keys)
# Output : dict_keys([])

# accessing keys in a nested dictionary 

student = {
    "Name":"Seemanshu",
    "Grades":{
        "Math":91,
        "Science":89
    }
}

grade_keys=student["Grades"].keys()
print(grade_keys)
# dict_keys(['Math', 'Science'])

stu_keys = student.keys()
print(stu_keys)
# dict_keys(['Name', 'Grades'])

# values : gives out values in dict 

empty_dict = {}

empt_Values = empty_dict.values()
print(empt_Values)
# outpt : dict_values([])

# Viewin items in nested dictionary 
student = {
    "Name":"Seemanshu",
    "Grades":{
        "Math":91,
        "Science":89
    }
}
grade_Items = student["Grades"].items()
print(grade_Items)
# dict_items([('Math', 91), ('Science', 89)])

# updating Existing Key Values 
car = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2021
}
car.update({"year":2025})
print(car)

# Output : {'brand': 'Toyota', 'model': 'Camry', 'year': 2025}

# pop : Removes Key from dict and returns its value . 

student = {
    "Name":"Seemanshu",
    "Grades":{
        "Math":91,
        "Science":89
    }
}

removed_Value= student["Grades"].pop("Science")
print (student)
# Output : {'Name': 'Seemanshu', 'Grades': {'Math': 91}}   

print("Removed Values:",removed_Value)
# removed Value : 89

# clear - clear the dictionary 

student = {
    "Name":"Seemanshu",
    "Grades":{
        "Math":91,
        "Science":89
    }
}
print("Before Clear(): ",student)
# Before Clear():  {'Name': 'Seemanshu', 'Grades': {'Math': 91, 'Science': 89}}
student.clear()
print("After Clear(): ",student)
# After Clear():  {}


