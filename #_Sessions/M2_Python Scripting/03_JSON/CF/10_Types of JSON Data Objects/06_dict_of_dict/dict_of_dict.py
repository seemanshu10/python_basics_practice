import json

with open("dict_of_dict.json", "r") as file:
    data = json.load(file)


for person_id, person_details in data.items():
    print(f"{person_id}: Name - {person_details['name']}, Age - {person_details['age']}")