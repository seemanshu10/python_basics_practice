import os, json
from shottrack.config import get_shot_data_file_path

def load_json_shot_data():
    """Load shots data. Create file if it doesn't exist."""

    shot_file_json_path = get_shot_data_file_path()

    if not os.path.exists(shot_file_json_path):
        with open(shot_file_json_path, "w") as f:
            json.dump([], f)

    try:
        with open(shot_file_json_path, "r") as f:   
            data = json.load(f)

            if isinstance(data, list):
                return data
            else:
                return 

    except json.JSONDecodeError:
        print("Invalid JSON format. Resetting file.")
        save_json_shot_data([])
        return 

def save_json_shot_data(shots):
    """Save shots to JSON file."""

    shot_file_json_path = get_shot_data_file_path()

    with open(shot_file_json_path, "w") as f: 
        json.dump(shots, f, indent=4)