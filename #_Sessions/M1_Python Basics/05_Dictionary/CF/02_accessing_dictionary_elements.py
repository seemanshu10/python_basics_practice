person = {"name": "Alice", "age": 25, "city": "London"}

# --------------- Accessing Values ---------------

# Using Keys
print(person["name"])


# ------------------ Get All Keys -  keys() ------------------

person = {"name": "Alice", "age": 25, "city": "London"}
keys = person.keys()


# --------------- Get all Values -- Values() ------------------
person = {"name": "Alice", "age": 25, "city": "London"}
values = person.values()
print(values)


# -------------- Get All Key-Value Pairs -- items() -------------
book = {"title": "1984", "author": "George Orwell", "year": 1949}
book_items = book.items()
print(book_items)

