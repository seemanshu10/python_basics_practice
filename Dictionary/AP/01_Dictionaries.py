"""
program that demonstrates the use of dictionaries. Dictionaries are a fundamental data structure in Python used to store key-value pairs.
"""
# creting the person dictionary 
person = {
    "name":"John",
    "Age":30,
    "City" :"London",
    "Country": "United Kingdom"
}
# printing 
print(person)
# {'name': 'John', 'Age': 30, 'City': 'London', 'Country': 'United Kingdom'}

# updting Pin and printing 
person.update({"Pin":20004})
print(person)
# Output : {'name': 'John', 'Age': 30, 'City': 'London', 'Country': 'United Kingdom', 'Pin': 20004}

# dictionary viwable items 
dic_items = person.items()
print(dic_items)
# Output : dict_items([('name', 'John'), ('Age', 30), ('City', 'London'), ('Country', 'United Kingdom'), ('Pin', 20004)])


person["City"]="Edinburgh"
dic_items = person.items()
print(dic_items)

# Output : dict_items([('name', 'John'), ('Age', 30), ('City', 'Edinburgh'), ('Country', 'United Kingdom'), ('Pin', 20004)])


city_value= person.get("City")
print(city_value) # Output : Edinburgh