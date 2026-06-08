import sys

def shot_created(shotname_arg):
    print(f"Shot Created {shotname_arg}")

def run_main():
    
    args = sys.argv

    if len(args) < 2 or args[1] == "help":
        print("Help call! ")
        return

    command = args[1]

    if command == "add-shot":
        if len(args) < 3:
            print("Error: Shot name required")
            return
        
        shotname_arg = args[2]
        # print(shotname_arg)
        shot_length = len(shotname_arg[2:])
        
        if shot_length <=3:
            shot_created(shotname_arg)
        else:
            print("Error: Invalid shot number length given. Give number like 001.")
            return
        
run_main()