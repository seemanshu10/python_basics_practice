import json

# Python dictionary
data = {
    "name": "Alice",
    "age": 28,
    "is_student": False,
    "courses": ["Art", "Design"]
}

#  Another Dictionary Example
# data = {'name': 'aman', 'last_name': 'verma', 'location': ['mumbai', 'banglore']}

# with open('output.json', 'w') as file:
#     json.dump(data, file)  


with open('output.json', 'w') as file:
    json.dump(data, file, indent=4)  