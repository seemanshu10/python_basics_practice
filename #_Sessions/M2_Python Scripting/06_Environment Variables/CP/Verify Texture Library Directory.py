import os 

os.environ['TEXTURE_LIBRARY_PATH'] = r'D:\PipelineTD\python_basics_practice\#_Sessions\M2_Python Scripting\06_Environment Variables\CP\StudioTools\Textures'

texture_path = os.getenv('TEXTURE_LIBRARY_PATH')

if texture_path and os.path.exists(texture_path):
    print(f"The Texture Library is available at: {texture_path}")
else:
    print("Texture Library path is not set or does not exist.")
