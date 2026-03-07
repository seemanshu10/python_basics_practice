import json

with open("list_of_list.json", "r") as file:
    data = json.load(file)

# Iterate through outer and inner lists
for sublist in data:
    for item in sublist:
        print(item)