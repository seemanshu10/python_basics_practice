import os

from .constants import DEFAULT_DATA_FILE

def get_shot_data_file_path():
    """
    Return the path to json shot file. 
    Use rnvironment variable if set, otherwise default.
    """
    
    file_json_shot = os.getenv("SHOT_DATA_FILE",DEFAULT_DATA_FILE)

    shot_json_file_path = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), file_json_shot)
    # Ensure directory exists (if folder is included)
    directory = os.path.dirname(shot_json_file_path)

    if directory and not os.path.exists(directory):
        os.makedirs(directory)

    # print(shot_json_file_path)
    return shot_json_file_path

if __name__ == "__main__":

    get_shot_data_file_path()