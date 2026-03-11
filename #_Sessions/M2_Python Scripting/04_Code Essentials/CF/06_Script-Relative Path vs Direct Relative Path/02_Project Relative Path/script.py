import json


file_path = "sample.json"

with open(file_path, 'r') as file:
    data = json.load(file)

print(data)
