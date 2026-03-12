import os 

plugins_path = os.getenv('MAYA_PLUGIN_PATH')

if plugins_path:
    if os.path.isdir(plugins_path):
        print(f"Maya Plugin Path is set correctly: {plugins_path} ")
    else:
        print(f"Error: Maya Plugin Path directory does not exists : {plugins_path} ")
else:
    print("Error: Maya Plugin Path is not set.")