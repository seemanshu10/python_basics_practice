import os 

os.environ['NUKE_LIBRARY_PATH'] = r'D:\PipelineTD\python_basics_practice\#_Sessions\M2_Python Scripting\06_Environment Variables\CP\StudioTools\NukeScripts'

nuke_scripts_path = os.getenv('NUKE_LIBRARY_PATH')

if nuke_scripts_path and os.path.isdir(nuke_scripts_path):
    print("Available Nuke Scripts: ")
    for script in os.listdir(nuke_scripts_path):
        print(f"- {script}")
else:
    print("Nuke Script directory not found.")
