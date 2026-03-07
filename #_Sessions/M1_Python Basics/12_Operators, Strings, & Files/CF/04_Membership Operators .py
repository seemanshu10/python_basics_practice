#---------------- Using 'in' with a list ----------------
cities = ["Paris", "London", "Tokyo"]

print("Tokyo" in cities)     # True
print("Berlin" in cities)    # False



#---------------- Using 'not in' with a list -------------
ids = [101, 102, 103]

print(104 not in ids)   # True
print(102 not in ids)   # False



#---------------- Membership with strings ----------------
message = "Python programming is fun"

print("Python" in message)      # True
print("Java" not in message)    # True



#---------------- Membership with sets -------------------
skills = {"HTML", "CSS", "JavaScript"}

print("CSS" in skills)          # True
print("Python" not in skills)   # True



#---------------- Membership with dictionary keys --------
car = {"brand": "Tesla", "year": 2023}

print("brand" in car)        # True
print("model" not in car)    # True