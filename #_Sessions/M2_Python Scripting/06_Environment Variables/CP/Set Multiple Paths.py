import os 

# Set environments variables for asset paths
os.environ['MODEL_PATH'] = r'D:\PipelineTD\python_basics_practice\#_Sessions\M2_Python Scripting\06_Environment Variables\CP\StudioTools\Assets\Models'

os.environ['TEXTURE_PATH'] = r'D:\PipelineTD\python_basics_practice\#_Sessions\M2_Python Scripting\06_Environment Variables\CP\StudioTools\Assets\Textures'

os.environ['RIG_PATH'] = r'D:\PipelineTD\python_basics_practice\#_Sessions\M2_Python Scripting\06_Environment Variables\CP\StudioTools\Assets\Rigs'

# print all paths

for asset_type in ['MODEL_PATH', 'TEXTURE_PATH', 'RIG_PATH']:
    path = os.getenv(asset_type)
    print(f"{asset_type}: {path if path else 'Not Set'}")

