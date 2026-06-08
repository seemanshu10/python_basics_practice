import sys 

from .commands import shot_created, show_help, preview_shots

def run_main():
    
    args = sys.argv

    if len(args) < 2 or args[1] == "help":
        show_help()
        return
    
    command = args[1]

    if command == "add-shot":
        if len(args) < 3:
            print("Error: Shot name required")
            return

        shotname_arg = args[2].upper()
        shot_created(shotname_arg)

    elif command == "list-shots":
        preview_shots()

    else:
        print("Error: Unknown command")
        show_help()
