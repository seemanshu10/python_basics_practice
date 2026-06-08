import os

DEFAULT_DATA_FILE = "shots.json"
file_json_shot = os.environ.get("SHOT_DATA_FILE", DEFAULT_DATA_FILE)
print(file_json_shot)

