import sys

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

list_shots = []

def shot_created(shotname_arg):
    
    shots = [
        {"shot_code" : shotname_arg, "status": "not_started"}
    ] 

    list_shots.append(shots)
    print(f"Shot {shotname_arg} added successfully.")
    # print(list_shots)
    
def preview_shots():
    if not list_shots:
        print("No shots found.")
        return
    
    for i, shot in enumerate(list_shots, start = 1):
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

"""
```python main.py add-shot SH010``` 
Shot SH010 added successfully.
```python main.py add-shot SH020```
Shot SH020 added successfully.
```python main.py list-shots```
Shot SH030 added successfully.

```python main.py list-shots```
No shots found.
"""