from .storage import load_json_shot_data, save_json_shot_data
from .validators import is_valid_shot_code, is_valid_status, is_valid_shot_status_filter

from .exporter import export_report

def show_help():
    print("""
Usage: python main.py [add-shot | list-shots | help] <shot-number>

Options:
  add-shot              Adding Shot Default value = "Not Started".
  list-shots            List all the shots that are created.
  help                  Show this help message and exit.
  set-status            Set the status of the shots 
  add-notes             Adding notes on shot
  add-task              Adding tasks on particular shot 
  done-task             Task Status updated to done
  delete-task           Deleted compoleted task 
  view-notes            View Notes added to the shot 
  list-shots --pending  List shots with pending status    
  list-shots --done     List shots with done status
  list-shots --review   List shots with review status       

Description:
  simple command-line tool in Python to manage VFX shots.

Examples:
  python main.py help
  python main.py add-shot SH010
  python main.py list-shots
  python main.py set-status SH010 review
  python main.py add-note SH010 "Need better edge cleanup"
  python main.py set-status SH100 approved
  python main.py view-notes SH010
  python main.py add-task SH010 "Roto cleanup"
  python main.py done-task SH010 1
  python main.py delete-task SH010 2      
  python main.py list-shots --pending
  python main.py list-shots --review
  python main.py list-shots --done
  python main.py list-shots --status review
""")

def shot_created(shotname_arg):

    if not is_valid_shot_code(shotname_arg):
        print(f"Invalid shot code format. Use format like SH001.")
        return
    
    json_shot_data = load_json_shot_data()

    # prevent duplicates
    for shot in json_shot_data:
        if shot["shot_code"] == shotname_arg:
            print(f"Shot {shotname_arg} already exists.")
            return

    new_shot_data = {
        "shot_code": shotname_arg,
        "status": "not_started",
        "notes": [],
        "tasks": []
    }

    json_shot_data.append(new_shot_data) 
    save_json_shot_data(json_shot_data)

    print(f"Shot {shotname_arg} added successfully.")

def preview_shots(filter_status = None):
    
    shots = load_json_shot_data()

    if not shots:
        print("No shots found.")
        return
    
    for i, shot in enumerate(shots, start=1):
        status = shot['status']

        if filter_status is None:
            match = True

        elif filter_status == "done":
            match = (status == "approved")

        elif filter_status == "pending":
            match = status in ["hold", "not_started", "in_progress"]

        elif filter_status == "review":
            match = (status == "review")

        if match:
            print(f"{i}. {shot['shot_code']} - {shot['status']}")

def set_shot_status(shotname_arg, new_status):

    if not is_valid_shot_code(shotname_arg):
        print(f"Invalid shot code format. Use format like SH001.")
        return
    
    if not is_valid_status(new_status):
        print("Error Status is invalid. ")
        return
    
    shots = load_json_shot_data()
  
    for shot in shots:
        
        if shot["shot_code"] == shotname_arg:
            shot["status"] = new_status
            print(f"Status for {shotname_arg} updated to {new_status}. ")
            break
        
    save_json_shot_data(shots)
    return shots
        
def add_notes(shotname_arg, new_note):
    if not is_valid_shot_code(shotname_arg):
        print(f"Invalid shot code format. Use format like SH001.")
        return
    
    shots = load_json_shot_data()

    for shot in shots:
        
        if shot["shot_code"] == shotname_arg:

            # if notes is emopty 
            if not shot["notes"]:
                shot["notes"] = [new_note]

            # if notes is a string (single note)

            elif isinstance(shot["notes"], str):
                shot["notes"] = [shot["notes"], new_note] 

            # If notes is already a list
            elif isinstance(shot["notes"], list):
                shot["notes"].append(new_note)

            print(f"Note added to {shotname_arg}")
            break
    
    save_json_shot_data(shots)
    
def view_notes_data(shotname_arg):
    if not is_valid_shot_code(shotname_arg):
        print(f"Invalid shot code format. Use format like SH001.")
        return
    
    shots = load_json_shot_data()

    for shot in shots:

        if shot["shot_code"] == shotname_arg:
            notes = shot.get("notes", [])

            print(f"\nPrinting Notes for {shotname_arg}: ")

            if not notes:
                print(" No notes available.")
                return
            
            # if single string note 

            if isinstance(notes, str):
                print(f" 1. {notes}")
                return
            
            # if list of notes 
            for i, note in enumerate(notes, start=1):
                print(f" {i}. {note}")
            return

    print(f"Shot {shotname_arg} not found. ") 
        
def add_new_task(shotname_arg, task_note, status_task = "Not started"
                 ):
    
    if not is_valid_shot_code(shotname_arg):
        print(f"Invalid shot code format. Use format like SH001.")
        return

    shots = load_json_shot_data()
    
    # prevent duplicates
    for shot in shots:
        if shot["shot_code"] == shotname_arg:

            next_id = 1

            if len(shot["tasks"]) > 0:
                biggest_id = 0

                for task in shot["tasks"]:
                    if task["id"] > biggest_id:
                        biggest_id = task["id"]

                next_id = biggest_id + 1

            new_task = {
                "id": next_id,
                "title": task_note,
                "status": status_task
            }

            shot["tasks"].append(new_task)

            save_json_shot_data(shots)

            print(f"Task added to {shotname_arg}: {new_task}")
            return

    # If no matching shot found
    print(f"Shot {shotname_arg} not found.")

def done_task_updated(shotname_arg, task_code):
    if not is_valid_shot_code(shotname_arg):
        print(f"Invalid shot code format. Use format like SH001.")
        return
    
    if not task_code.isdigit():
        print("Invalid Task_id can only be a whole number. ")
        return 
    
    old_task_code = task_code
    task_code = int(task_code) - 1
    
    shots = load_json_shot_data()
  
    for shot in shots:
        
        if shot["shot_code"] == shotname_arg:
            shot["tasks"][task_code]["status"] = "done"
            print(f"Task {old_task_code} in {shotname_arg} marked as done. ")
            break
    save_json_shot_data(shots)
    return shots

def delete_task_from_shot(shotname_arg, task_code):

    if not is_valid_shot_code(shotname_arg):
        print(f"Invalid shot code format. Use format like SH001.")
        return
    
    if not task_code.isdigit():
        print("Invalid Task_id can only be a whole number. ")
        return 
    
    shots = load_json_shot_data()

    old_task_code = task_code
    task_code = int(task_code) - 1
    for shot in shots:
        
        if shot["shot_code"] == shotname_arg:
            try:
                del shot["tasks"][task_code]

                print(f"Task {old_task_code} deleted from {shotname_arg}.")
                break
            except IndexError:
                print("Shot Task code doesn't exist.")

    save_json_shot_data(shots)
    return shots

def export_report_shots():
    export_report()