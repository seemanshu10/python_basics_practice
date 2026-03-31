"""
Shot Folder Auto-Creator - Level 2 
Objective: Upgrade your Level-1 CLI tool so that the folder structure is NO LONGER hard-
coded inside the script, but is loaded from an external JSON config file. 
In real VFX pipelines, folder structures are not fixed inside code. 
Studios store folder rules in config files, so they can change structures without modifying Python 
scripts. 
You will now convert your Level-1 tool into a config-driven tool that reads a 
shot_structure.json file and creates folders accordingly.



Run command 
python shotsetup.py <shot_name> <root_path>

Example 
python shotsetup.py SH020 D:\Projects\Seq01 
"""

# check in the directory if shot name exist 
# if exist then fine 
# if doesn't exist then create the folder structure in the shot folder 
import os
import sys
import json

if len(sys.argv) < 3:
    print("Invalid Input! Command Must contain python shotsetup.py <shot_name> <root_path> ")
    sys.exit(1)

args = sys.argv[1:]

shot_name = args[0]
seq_directory_path = args[1]

# list of folders will be from shot_structure.json
# list_of_folder = ["plate", "comp", "cache", "render", "scripts"]


try:
    with open(r"C:\Users\ANT-pc\Desktop\Cohort-EC1\#_Sessions\M2_Python Scripting\12_Live Practice\L2\shot_structure.json", "r") as shot_config_file:
        content_shot_cofig = json.load(shot_config_file)
        print("Reading folder structire from shot_structure.json")

except FileNotFoundError:
    print("Error: shot_structure.json not found.")

except json.JSONDecodeError:
    print("Error: Cannot Read config File")


# # check if shot number is a directory in path D:\Projects\Seq01 
if not os.path.isdir(seq_directory_path):
    os.makedirs(seq_directory_path, exist_ok= True)
    print("Creating sequence directory:", seq_directory_path)


# # list_of_shots = os.listdir(seq_directory_path)

# adding Shot name is seq directory Path 
shot_directory_path = os.path.join(seq_directory_path,shot_name)
# print(shot_directory_path)

# dictionary view from json file 
folder = content_shot_cofig.items()

# if shot_name 
for rootFolder , subfolder in folder:
    # print(rootFolder)
    # print(os.path.join(shot_directory_path, rootFolder))
    if os.path.exists(shot_directory_path):
        print("Shot Exists! , skip ")
    else:
        os.makedirs(os.path.join(shot_directory_path, rootFolder))
    for folder in subfolder:
        # print(f"---{folder}")
        shot_folder_path = os.path.join(shot_directory_path, rootFolder, folder)
        # print(shot_folder_path)
        if os.path.exists(shot_folder_path):
            print("Folder Exists ! skipping")
        else:
            os.makedirs(os.path.join(shot_folder_path))
            print(f"Created folder : {shot_folder_path}")
        
print(f"Shot {shot_name} created successfully!")