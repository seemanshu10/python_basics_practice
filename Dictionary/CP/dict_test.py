person = {"name" : "Alice","age":25}

#person[0] = "JAck"
#print (person)

person.update({"age":34})
print (person)
person.update({"city":"London"})
print(person)
print(type(person))

n = person.items()
person["age"] = 78

print (n)
# dict_items([('name', 'Alice'), ('age', 78), ('city', 'London')])
n = person.items()
person["age"] = 120

print (n)
# dict_items([('name', 'Alice'), ('age', 120), ('city', 'London')])

#  

person = {"name" : "Alice","age":25,"name":"Value"}
print(person)

tupleTest= {
    "name" : "sadsad",
    ("a","b") : 45              
}

print(tupleTest["a","b"]) 
