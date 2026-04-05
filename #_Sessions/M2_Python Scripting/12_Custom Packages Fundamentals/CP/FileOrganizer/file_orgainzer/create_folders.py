import os

def create_folder(directory, folder_name):
    os.makedirs(os.path.join(directory, folder_name), exist_ok=True)
    return 