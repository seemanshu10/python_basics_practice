from .storage import load_json_shot_data, save_json_shot_data
from .validators import is_valid_code

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


def shot_created(shotname_arg):
    # is_shot_name_valid
    if not is_valid_code(shotname_arg):
        print(f"Invalid shot code format. Use format like SH001.")
        return
    
    shots = load_json_shot_data()

    # prevent duplicates
    for shot in shots:
        if shot["shot_code"] == shotname_arg:
            print(f"Shot {shotname_arg} already exists.")
            return []

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