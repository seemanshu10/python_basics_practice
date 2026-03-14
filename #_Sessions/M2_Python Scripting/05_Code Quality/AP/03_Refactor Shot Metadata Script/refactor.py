# Refactor Render Data Script
import os
import json

SHOT_DATA_PATH = os.path.dirname(os.path.abspath(__file__))

def calculate_frame_count_data(frame_start_data, frame_end_data):

   """
   Calculate the total frame count from fram_start and frame_end 

   Args:
      frame_start_data : frame start end (int)
      frame_end_data : frame end data (int)

   Returns:
      frame_count_data : int
    
   """
   frame_count_data = frame_end_data - frame_start_data + 1       # formula to calculate the total frames 
   return frame_count_data

def process_directory(shots_folder):

   shot_folder_Path = os.path.join(SHOT_DATA_PATH, shots_folder)
   shot_file_name = os.listdir(shot_folder_Path)
  
   # loop through all the files and read data and update 
   for shot_file in shot_file_name:
      if shot_file.endswith(".json"):
         
         shot_file_path = os.path.join(shot_folder_Path, shot_file)
         
         try:
            with open(shot_file_path, "r") as read_shot_file:
               shot_data = json.load(read_shot_file)

         except FileNotFoundError:
            print(f"Error :'{shot_file_path} doesn't exist'")

         except json.JSONDecodeError as e:
            print(f"Json decode error: {e} ")

         frame_start_data = shot_data["frame_start"]
         frame_end_data = shot_data["frame_end"]
         
         frame_count_data = calculate_frame_count_data(frame_start_data , frame_end_data )
      
         shot_data["frame_count"] = frame_count_data

         with open(shot_file_path, "w") as write_shot_file:
            shot_data = json.dump(shot_data , write_shot_file , indent=4)
                  
         print(f"Processed {shot_file} | Frame Count: {frame_count_data}")

if __name__ == "__main__":
   process_directory("shots")