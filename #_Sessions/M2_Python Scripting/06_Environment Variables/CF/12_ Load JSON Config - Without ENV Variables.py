import json
import os

def load_config(config_filename):
    """
    Load a specific JSON configuration file from a hardcoded folder path.
    """
    config_folder = "C:/Users/pralhad/Desktop/New folder/configs"
    config_path = os.path.join(config_folder, config_filename)

    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
            print(f"\nLoaded configuration from: {config_path}")
            print(json.dumps(config, indent=2))
    except FileNotFoundError:
        print(f"Error: Config file '{config_filename}' not found in {config_folder}")
    except json.JSONDecodeError:
        print(f"Error: Failed to parse JSON in {config_filename}")


if __name__ == "__main__":
    load_config('database.json')
    load_config('logging.json')
    load_config('app.json')