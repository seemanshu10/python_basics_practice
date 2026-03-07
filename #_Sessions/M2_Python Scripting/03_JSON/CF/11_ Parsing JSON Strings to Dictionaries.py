import json

# JSON string (dictionary format)
json_string = '{"name": "Bob", "age": 25, "city": "Builderland"}'

# Convert to Python dictionary
python_dict = json.loads(json_string)

print(python_dict)