# default_path = "/project/assets"

def list_files(path):
    return [f"{path}/file.txt", f"{path}/file2.txt"]

def create_file(path, name):
    return f"Created file at {path}{name}"