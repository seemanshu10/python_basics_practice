import os
import json

script_dir = os.path.dirname(os.path.abspath(__file__))
print(script_dir)

file_path = os.path.join(script_dir, "..", "data", "sample.json")
print(file_path)

file_path = os.path.abspath(file_path)
print(file_path)

with open(file_path, "r") as file:
    data = json.load(file)

print(data)
