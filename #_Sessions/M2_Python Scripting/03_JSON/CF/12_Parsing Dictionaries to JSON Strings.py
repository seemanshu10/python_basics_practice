import json

# Python dictionary
python_dict = {
    "name": "Bob",
    "age": 25,
    "city": "Builderland"
}

#  Convert Dictionary to JSON String
json_string = json.dumps(python_dict)


# Python list
python_list = ["apple", "banana", "cherry"]

# Convert to JSON string
json_string_list = json.dumps(python_list)


print(json_string)

print(json_string_list)