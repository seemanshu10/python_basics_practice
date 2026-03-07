import json

# Load JSON data from file
with open("sample.json", 'r') as f:
    data = json.load(f)

# Print the data
print(data)