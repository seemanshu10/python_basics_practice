# keyError
my_dict = {"name": "Alice", "age": 25}
print(my_dict["city"])

# -- prevention -> use get()
print(my_dict.get("city"))
print(my_dict.get("city", "Not Found"))

# -------------- Need to discuss ------------------------

# TypeError
my_dict = {[1, 2]: "value"}


# ValueError
my_dict = {"name": "Alice", "age": 25}
my_dict.update(["incorrect_format"])
