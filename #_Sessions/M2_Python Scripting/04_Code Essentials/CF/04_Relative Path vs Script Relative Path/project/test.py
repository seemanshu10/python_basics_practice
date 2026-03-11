import json


# Using Relative Path
with open("./data/weather.json", 'r') as file:
    data = json.load(file)

print(data)




'''
    - Q.1 What If We Move test.py inside Script Folder ?
    - Q.2 What If weather.json Moves to data/?
'''