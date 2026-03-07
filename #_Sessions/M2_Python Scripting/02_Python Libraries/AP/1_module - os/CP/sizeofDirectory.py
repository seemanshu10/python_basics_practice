import os 

def get_directory_size(directory):
    total_size = 0

    for dirpath , dirnames , filenames in os.walk(directory):
        for file in filenames:
            file_path = os.path.join(dirpath,file)
            total_size += os.path.getsize(file_path)

    return total_size

# get the size of current directory 
directory_size = get_directory_size(".")
print(f"Total size of the current directory: {directory_size / 1024:.2f} KB")

# Total size of the current directory: 444.63 KB