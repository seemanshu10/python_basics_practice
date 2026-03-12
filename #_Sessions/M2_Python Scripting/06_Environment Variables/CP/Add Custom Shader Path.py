import os 

os.environ['ARNOLD_SHADER_PATH'] = r'D:\PipelineTD\python_basics_practice\#_Sessions\M2_Python Scripting\06_Environment Variables\CP\StudioTools\ArnoldShaders'

shader_path = os.getenv('ARNOLD_SHADER_PATH')

if shader_path:
    print(f"Arnold Shader Path set to: {shader_path}")
else:
    print("Arnold Shader path not defined.")
