import os

def delete_file(filename):
    try:
        if os.path.exists(filename):
            os.remove(filename)
            print(f"File '{filename}' deleted successfully.")
        else:
            print(f"File '{filename}' does not exist.")
    except Exception as e:
        print(f"Error deleting file: {e}")