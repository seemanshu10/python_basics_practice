person = {"name": "Alice", "age": 25, "city": "London"}


# ------------ Access value using get()
name = person.get("name")

print(name)  # Output: Alice


# ---------- Accessing a Missing (Non-Existent) Key

# Try to get a key that doesn't exist
country = person.get("country")

print(country)  # Output: None