import json

with open("only_list.json", "r") as file:
    data = json.load(file)

# Access each element
for item in data:
    print(item)