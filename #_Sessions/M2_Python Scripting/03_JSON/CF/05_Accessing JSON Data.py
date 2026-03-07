import json



# Load the JSON file
with open("sample2.json", 'r') as f:
    data = json.load(f)

# Access the first person’s data
# print(data["people"])


# Get the last_name of Every Person
for each in data["people"]:
    # print(each)
    print(each["last_name"])