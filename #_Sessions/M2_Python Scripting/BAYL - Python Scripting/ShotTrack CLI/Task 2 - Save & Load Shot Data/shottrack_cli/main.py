import os,sys
import json

FILE_NAME = "shots.json"
shot_file_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), FILE_NAME)

def show_help():
    print("""
Usage: python main.py [add-shot | list-shots | help] <shot-number>

Options:
  add-shot          Adding Shot Default value = "Not Started".
  list-shots        list all the shots that are created.
  help              Show this help message and exit.

Description:
  simple command-line tool in Python to manage VFX shots.

Examples:
  python main.py add-shot SH010
  python main.py add-shot SH020
  python main.py list-shots
  python main.py help
""")

def load_json_shot_data():
    """Load shots data. Create file if it doesn't exist."""

    if not os.path.exists(shot_file_path):
        with open(shot_file_path, "w") as f:
            json.dump([], f)
        return 

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

def shot_created(shotname_arg):

    shots = load_json_shot_data()

    # prevent duplicates
    
    for shot in shots:
        if shot["shot_code"] == shotname_arg:
            print(f"Shot {shotname_arg} already exists.")
            sys.exit()

    new_shot = {
        "shot_code": shotname_arg,
        "status": "not_started"
    }

    shots.append(new_shot) 
    save_json_shot_data(shots)

    print(f"Shot {shotname_arg} added successfully.")


def preview_shots():

    shots = load_json_shot_data()

    if not shots:
        print("No shots found.")
        return

    for i, shot in enumerate(shots, start=1):
        print(f"{i}. {shot['shot_code']} - {shot['status']}")

def main():
    args = sys.argv

    if len(args) < 2 or args[1] == "help":
        show_help()
        return

    command = args[1]

    if command == "add-shot":
        if len(args) < 3:
            print("Error: Shot name required")
            return

        shotname_arg = args[2]
        shot_created(shotname_arg)

    elif command == "list-shots":
        preview_shots()

    else:
        print("Error: Unknown command")
        show_help()

if __name__ == "__main__":
    main()