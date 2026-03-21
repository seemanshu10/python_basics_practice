import os
import sys
import json
from colorama import init , Fore , Style

# Initialize colorama
init(autoreset=True)

# Get the folder of the current script
dirname = os.path.dirname(__file__)
filename_render = os.path.join(dirname, 'render_status.json')

# Load JSON safely
try:
    with open(filename_render, "r") as f:
        render_data = json.load(f)
except FileNotFoundError:
    print(f"Error: 'render_status.json' not found.")
    sys.exit(1)

# print(render_data)

# Get shot IDs from CLI
shot_ids = sys.argv[1:]

if not shot_ids:
    print("Usage: python check_render.py <shot_id1> <shot_id2> ...")
    sys.exit(0)

# process shots 
for shot_id in shot_ids:
    shot_info = render_data.get(shot_id) 
    # print(shot_info)

    if shot_info:
        status = shot_info.get("status").lower()
        artist = shot_info.get("artist")
        frame_range = shot_info.get("frame_range")
        last_update = shot_info.get("last_update")
        notes = shot_info.get("notes")

        # Color logic
        if status == "rendered":
            color = Fore.GREEN + Style.BRIGHT
        elif status == "rendering":
            color = Fore.YELLOW + Style.BRIGHT
        elif status == "failed":
            color = Fore.RED + Style.BRIGHT
        else:
            color = Fore.WHITE + Style.BRIGHT


        print(f"{color} Shot ID: {shot_id}")
        print(f"{color} Status: {status}")
        print(f"{color} Artist: {artist}")
        print(f"{color} Frame Range: {frame_range}")
        print(f"{color} Last Update: {last_update}")
        print(f"{color} Notes: {notes}\n")
    else:
        print(f"Shot {shot_id} not found !")