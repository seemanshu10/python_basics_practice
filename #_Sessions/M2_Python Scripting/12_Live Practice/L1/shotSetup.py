"""
Shot Cretaor 

New Shot Given , too crates 
plate 
comp 
cache 
render 
scripts 


Folder Streucture 
D:\Projects\Seq01\SH020\ 
    plate\ 
    comp\ 
    cache\ 
    render\ 
    scripts\ 


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
if len(sys.argv) < 3:
    print("Invalid Input! Command Must contain python shotsetup.py <shot_name> <root_path> ")
    sys.exit(1)

args = sys.argv[1:]

shot_name = args[0]
seq_directory_path = args[1]

list_of_folder = ["plate", "comp", "cache", "render", "scripts"]

# check if shot number is a directory in path D:\Projects\Seq01 
if not os.path.isdir(seq_directory_path):
    
    os.makedirs(seq_directory_path, exist_ok= True)
    print("New Sequence Created at:", seq_directory_path)

list_of_shots = os.listdir(seq_directory_path)

if shot_name not in list_of_shots:
    shot_folder_path = os.path.join(seq_directory_path, shot_name)
    # print(shot_folder_path)
    for folder in list_of_folder:
        subfolders_path = os.path.join(shot_folder_path, folder)
        # print(folder_path)
        
        os.makedirs(subfolders_path, exist_ok= True)
        print(f"Subfolders Created at {subfolders_path}")

else:
    print("Given Shot already Created!")
