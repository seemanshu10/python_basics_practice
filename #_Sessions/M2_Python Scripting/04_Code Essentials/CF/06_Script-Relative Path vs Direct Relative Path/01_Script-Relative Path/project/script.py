import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "sample.json")


with open(file_path, 'r') as file:
    data = json.load(file)

print(data)
