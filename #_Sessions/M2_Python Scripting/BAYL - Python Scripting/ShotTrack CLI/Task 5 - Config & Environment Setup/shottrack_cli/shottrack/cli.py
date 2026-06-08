import sys 

from .commands import (show_help, shot_created, preview_shots,
                       set_shot_status, add_notes, view_notes_data, add_new_task, done_task_updated, delete_task_from_shot)

from .validators import is_valid_shot_status_filter

def run_main():
    
    args = sys.argv

    if len(args) < 2 or args[1] == "help":
        show_help()
        return

    command = args[1]

    if command == "add-shot":
        if len(args) < 3:
            print("Error: Please provide a shot code.")
            return
        
        shotname_arg = args[2].upper()
        shot_created(shotname_arg)
        
    elif command == "set-status":
        if len(args) < 4:
            print("Error: Shot and status needs to be defined. ")
            return
        
        shotname_arg = args[2].upper()
        shot_status = args[3]
        set_shot_status(shotname_arg, shot_status)

    elif command == "add-note":
        if len(args) < 4:
            print("Error: Shot and notes needs to be defined.")
            return
        
        shotname_arg = args[2].upper()
        shot_note = args[3]
        add_notes(shotname_arg, shot_note)

    elif command == "view-notes":
        if len(args) < 3:
            print("Error: Shot needs to be defined.")

        shotname_arg = args[2]
        view_notes_data(shotname_arg)

    elif command == "add-task":
        if len(args) < 4:
            print("Error: Shot and task needs to be defined.")
            return
        
        shotname_arg = args[2].upper()
        task_note = args[3]
        
        add_new_task(shotname_arg, task_note)

    elif command == "done-task":
        if len(args) < 3:
            print("Error: Shot and task_code needs to be defined.")
            return
        
        shotname_arg = args[2].upper()
        task_code = args[3]
       
        done_task_updated(shotname_arg, task_code)

    elif command == "delete-task":
        if len(args) < 3:
            print("Error: Shot and task_code needs to be defined.")
            return
        
        shotname_arg = args[2].upper()
        task_code = args[3]
       
        delete_task_from_shot(shotname_arg, task_code)

    elif command == "list-shots":
        if len(args) < 2:
            print("Error: Shot and filter status needs to be defined.")
            return
        
        try:
            status_flags = args[2]
        except: 
            status_flags = None

        if not is_valid_shot_status_filter(status_flags):
            return

        if "--pending" in args:
            preview_shots("pending")

        elif "--done" in args:
            preview_shots("done")

        elif "--review" in args:
            preview_shots("review")

        else: 
            # No flag → show all
            preview_shots()

    else:
        print(f"Invalid Command: {command}")
        show_help()
