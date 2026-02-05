"""
Build a Python script that reads from two separate text files one using a relative path and one using an absolute path.
Implement basic file error handling to gracefully report missing or inaccessible files.

"""

# Creating a function which handles all the open operatins on files 
def read_assetInfo_file(file_path,label):
    try:
        print(f"\nReading {label}:")
        #  open file 
        with open(file_path, "r") as info:
            asset_content = info.read()   # reading All content of file 
        print(asset_content)
    
    # file not found error handling 
    except FileNotFoundError:
        print("File not found. Please Check path : ", path_assetInfo)

# relative path call 
path_assetInfo = r"Absolute&RelativePath\AP\01_Reading Vfx Config Files\projects\assets\asset_info.txt"
read_assetInfo_file(path_assetInfo,"asset_info.txt using relative path")

# absolute path call 
path_systemConfig = r"D:\PipelineTD\python_basics_practice\system_config.txt"
read_assetInfo_file(path_systemConfig, "system_config.txt using absolute path")


"""
Reading asset_info.txt using relative path:
Asset: Dragon_Rig
Version: 1.2

Reading system_config.txt using absolute path:
RenderEngine=Arnold
FrameRange=1001-1100
Resolution=1920x1080

"""