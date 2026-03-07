import json

with open("only_dict.json", "r") as file:
    data = json.load(file)

print(data["name"])
print(data["age"])
print(data["city"])