"""
Objective: Extend your Level-2 tool by adding a manual logging system that records every 
action into a tool_log.txt file with timestamps. 
In real VFX pipelines, every tool must log what it does — not just print to screen — so that 
production, leads, or TDs can verify actions later. 
You have not learned the logging module yet, so this task will teach you how to build a manual 
log writer using basic file operations. 
This means: 
     Every important event = one printed message AND one logged line 
     Log file must be persistent and keep old history (append mode



Run command 
python shotsetup.py <shot_name> <root_path>

Example 
python shotsetupL3.py SH020 D:\Projects\Seq01 
"""

# check in the directory if shot name exist 
# if exist then fine 
# if doesn't exist then create the folder structure in the shot folder 
import os
import sys
import json

from datetime import datetime

if len(sys.argv) < 3:
    print("Invalid Input! Command Must contain python shotsetup.py <shot_name> <root_path> ")
    sys.exit(1)

args = sys.argv[1:]

shot_name = args[0]
seq_directory_path = args[1]


# Path Setup 
folder_path = os.path.dirname(os.path.abspath(__file__))                        # current working directory 
log_file_path = os.path.join(seq_directory_path, shot_name, "tool_log.txt")     # log file path 
shot_directory_path = os.path.join(seq_directory_path, shot_name)                # adding Shot name is seq directory Path 

# now gives current datetime 
def logdatetime_format(log_message):

    """
    logDateTime _format which takes message and add in the log text file  
    """
    log_time = datetime.now().strftime("[%Y-%m-%d %H:%M:%S]")
    # print(log_time, log_message)
    final_log_message = f"{log_time} {log_message}"

    with open(log_file_path, "a") as log_file:
        log_file.write(final_log_message + "\n")

try:
    shot_structure_file_path = os.path.join(folder_path, "shot_structure.json")
    with open(shot_structure_file_path, "r") as shot_config_file:
        content_shot_cofig = json.load(shot_config_file)
        print("Reading folder structire from shot_structure.json")

except FileNotFoundError:
    print("Error: shot_structure.json not found.")
    sys.exit(1)

except json.JSONDecodeError:
    print("Error: Cannot Read config File")
    sys.exit(1)


# check if shot number is a directory in path D:\Projects\Seq01 
if not os.path.isdir(seq_directory_path):
    os.makedirs(seq_directory_path, exist_ok= True)
    print(f"Creating sequence directory: {seq_directory_path}")
else:
    print(f"Sequence directory exists: ", {seq_directory_path})
    logdatetime_format(f"Sequence directory exists: {seq_directory_path}")

# dictionary view from json file 
folder_config_data = content_shot_cofig.items()

# if shot_name 
for rootFolder, subfolder in folder_config_data:
    # print(rootFolder)
    # print(os.path.join(shot_directory_path, rootFolder))
    if os.path.exists(shot_directory_path):
        shot_exist_statement = "Shot Exists! , skip Shot Creation. "
        print(shot_exist_statement)
        logdatetime_format(shot_exist_statement)
    else:
        os.makedirs(os.path.join(shot_directory_path, rootFolder))
        shot_creation_statement = f"Shot Creation Successfull: {rootFolder}"
        print(shot_creation_statement)
        logdatetime_format(shot_creation_statement)

    for folder in subfolder:
        # print(f"---{folder}")
        shot_folder_path = os.path.join(shot_directory_path, rootFolder, folder)
        # print(shot_folder_path)
        if os.path.exists(shot_folder_path):
            folder_exist_statement = f"Folder Exists ! skipping {shot_folder_path}"
            print(folder_exist_statement)
            logdatetime_format(folder_exist_statement)
        else:
            os.makedirs(os.path.join(shot_folder_path))
            shot_folder_statement = f"Created folder : {shot_folder_path}"
            print(shot_folder_statement)
            logdatetime_format(shot_folder_statement)

final_log_statement = f"Shot {shot_name} created successfully!"
print(final_log_statement)
logdatetime_format(final_log_statement)