import json

with open("sample2.json", 'r') as f:
    data = json.load(f)

data["people"][2]["name"] = "Raj"


with open("sample2.json", 'w') as f:
    json.dump(data, f, indent=4)


print(data)
