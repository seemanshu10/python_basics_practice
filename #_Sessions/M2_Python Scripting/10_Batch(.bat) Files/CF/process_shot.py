import sys

if len(sys.argv) != 3:
    print("Usage: process_shot.py <shot_name> <task>")
    print("Example tasks: render, color_grading, preview")
    sys.exit(1)


shot_name = sys.argv[1]
task = sys.argv[2]


if task == "render":
    print(f"Rendering Shot: {shot_name}")

elif task == "color_grading":
    print(f"Applying color grading to Shot: {shot_name}")

elif task == "preview":
    print(f"Generating preview for Shot: {shot_name}")

else:
    print(f"Unknown task '{task}'. Supported tasks: render, color_grading, preview")
    sys.exit(1)

    
print("Task completed successfully!")