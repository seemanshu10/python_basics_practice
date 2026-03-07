import json

# Data to be written
data = {
    'name': 'aman',
    'last_name': 'verma',
    'location': ['mumbai', 'banglore']
}


with open("sample_output.json", 'w') as f:
    json.dump(data, f, indent=4)