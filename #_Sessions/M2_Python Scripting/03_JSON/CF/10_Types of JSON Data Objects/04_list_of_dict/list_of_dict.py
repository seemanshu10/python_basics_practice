import json

with open("list_of_dict.json", "r") as file:
    data = json.load(file)

for item in data:
    print(f"ID: {item['id']}, Name: {item['name']}")