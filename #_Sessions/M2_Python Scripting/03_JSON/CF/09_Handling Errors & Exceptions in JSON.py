import json

# invalid_json_string = '{"name": "Alice", "age": 30}'


# --------- Handling Invalid JSON Strings
# try:
#     data = json.loads(invalid_json_string)
#     print(data)
# except json.JSONDecodeError as e:
#     print(f"JSON decode error: {e}")


# # ----------- Handling Missing Files
try:
    with open('hello.json', 'r') as file:
        data = json.load(file)
except FileNotFoundError as e:
    print(f"File not found: {e}")