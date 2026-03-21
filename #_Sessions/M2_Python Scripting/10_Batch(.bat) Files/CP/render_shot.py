import sys
if len(sys.argv) == 3:
    shot = sys.argv[1]
    task = sys.argv[2]
    if task == "render":
        print(f"Rendering Shot: {shot}")
    elif task == "preview":
        print(f"Generating preview for shot: {shot}")
    else:
        print(f"Unknown task: {task}. Use 'render' or 'preview'.")

else:
    print("Usage: render_shot.py <shot> <task>")
    