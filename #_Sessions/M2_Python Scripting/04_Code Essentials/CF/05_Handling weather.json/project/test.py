import os

# Calculating the Path to weather.json
cur_file = os.path.dirname(os.path.abspath(__file__)) 
print(cur_file)
# weather_json_file_path = cur_file + "weather.json" 

# print(weather_json_file_path)  



# # Using os.path.join() to Correct the Path
weather_json_file_path = os.path.join(cur_file,"data", "weather.json") 

print(weather_json_file_path)
# print(os.path.exists(weather_json_file_path))




# # ---------- Reading weather.json Dynamically ------------------
# # weather_json_file_path = os.path.join(cur_file, "data", "weather.json")

with open(weather_json_file_path, 'r') as file:
    data = file.read()
    print(data)