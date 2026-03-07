# Adding Key-Value Pairs

person = {"name": "Alice", "age": 25}
person["city"] = "London"


# Updating Values
person = {"name": "Alice", "age": 25, "city": "London"}
person["age"] = 26


# Updating Key-Value Pairs - update()
person = {"name": "Alice", "age": 25}
person.update({"age": 26, "city": "London"})


# ------------------- Removing Key-Value Pairs --------------
# using -- del Keyword
person = {"name": "Alice", "age": 25, "city": "London"}
del person["city"]

# using -- pop()
person = {"name": "Alice", "age": 25, "city": "London"}
age = person.pop("age")

print(age)
print(person)