# Refactor Render Data Script
import os
import json

JOBS_DATA_PATH = os.path.dirname(os.path.abspath(__file__))

def calculate_frame_count(frame_end, frame_start):
    """
    Calculate the total number of frames for a render job.

    Args:
        frame_start (int): Starting frame of the shot.
        frame_end (int): Ending frame of the shot.

    Returns:
        int: Total frame count including both start and end frames.
    """
    return frame_end - frame_start + 1

def calculate_total_render_time(frame_count, render_time_per_frame):
    """
    Calculate total render time for a render job.

    Args:
        frame_count (int): Total number of frames in the job.
        render_time_per_frame (float): Time required to render a single frame.

    Returns:
        float: Total render time for the job.
    """
    return frame_count * render_time_per_frame


def process_render_farm_data(jobs_folder):
    job_folder_Path = os.path.join(JOBS_DATA_PATH, jobs_folder)
    job_file_name = os.listdir(job_folder_Path)

    total_render_time_jobs = 0

    for job_file in job_file_name:
        if job_file.endswith(".json"):
            job_file_path = os.path.join(job_folder_Path, job_file)

        try:
            with open(job_file_path, "r") as job_shot_file:
                job_data = json.load(job_shot_file)
                
        except FileNotFoundError:
            print(f"Error :'{job_file_path} doesn't exist'")

        except json.JSONDecodeError as e:
            print(f"Json decode error: {e} ")

        frame_start_data = job_data["frame_start"]
        frame_end_data = job_data["frame_end"]
        render_time_per_data = job_data["render_time_per_frame"]

        # calulating frame_count on each shot 
        frame_count = calculate_frame_count(frame_end_data, frame_start_data)
        # calculating total render time 
        total_render_time = calculate_total_render_time(frame_count, render_time_per_data)

        job_data["frame_count"] = frame_count
        job_data["total_render_time"] = total_render_time

        try:
            with open(job_file_path, "w") as job_shot_file:
                job_data = json.dump(job_data , job_shot_file , indent=4)

        except FileNotFoundError:
            print(f"Error :'{job_file_path} doesn't exist'")

        except json.JSONDecodeError as e:
            print(f"Json decode error: {e} ")
        
        print(f"Processed {job_file} | Frames: {frame_count} | Total Render Time: {total_render_time}")

        
        total_render_time_jobs += total_render_time
    print("Total Render Time Across All Jobs: ", total_render_time_jobs)

if __name__ == "__main__":
   process_render_farm_data("jobs")