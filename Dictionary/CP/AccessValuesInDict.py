"""
Docstring for Dictionary.AccessValuesInDict
"""
# using Variables as keys to access values 
employee = {
    "name":"Sarah",
    "position":"Manager",
    "salary":70000
    }

key = "salary"
print(employee[key])
# Output : 70000

# Accessing Values in a dictionary with non String Keys

num_dict = {1:"One",2:"Two",3:"Three"}

print(num_dict[1]) # output : One
print(num_dict[2]) # output : Two
print(num_dict[3]) # output : Three

# Access Values in a dict with mixed data types 

person = {
    "name":"John",
    "Age":30,
    "is_employed" :True
}

print(person["Age"]) # 30
print(person["name"]) # John
print(person["is_employed"]) # True

# Items method to display dictionaru as a dinctionary viewable item 

empty_dict ={}
empty_items = empty_dict.items()
print(empty_items)

# Output : dict_items([])

# Basic Disctionary 

car = {
    "brand":"Toyota",
    "model":"Camry",
    "year":2021
}

car_items=car.items()
print(car_items)

# Output : dict_items([('brand', 'Toyota'),('model', 'Camry'), ('year', 2021)])

