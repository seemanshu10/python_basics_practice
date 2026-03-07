import json

with open("dict_of_list.json", "r") as file:
    data = json.load(file)


print("Fruits:", data["fruits"])
print("Vegetables:", data["vegetables"])


for fruit in data["fruits"]:
    print("Fruit:", fruit)

for vegetable in data["vegetables"]:
    print("Vegetable:", vegetable)