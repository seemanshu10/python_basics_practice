person = {"name": "Alice", "age": 25, "city": "London"}

# -------------- Without Default Value ------------
country = person.get("country")

print(country)  # Output: None


# ------------- With Default Value -------------
country = person.get("country", "Not Specified")

print(country)  # Output: Not Specified