import os, json

FILE_NAME = "shots.json"
shot_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), FILE_NAME)

def load_json_shot_data():
    """Load shots data. Create file if it doesn't exist."""

    if not os.path.exists(shot_file_path):
        with open(shot_file_path, "w") as f:
            json.dump([], f)
        return []

    try:
        with open(shot_file_path, "r") as f:   
            data = json.load(f)

            if isinstance(data, list):
                return data
            else:
                return 

    except json.JSONDecodeError:
        print("Invalid JSON format. Resetting file.")
        return 

def save_json_shot_data(shots):
    """Save shots to JSON file."""
    with open(shot_file_path, "w") as f: 
        json.dump(shots, f, indent=4)