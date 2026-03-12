import os

maya_plugin_path = os.environ['MAYA_PLUG_IN_PATH']

print(f"Maya Plugin Path: {maya_plugin_path}")


# ------------- Best Practice for safety
# try:
#     maya_plugin_path = os.environ['NUKE_PATH']
#     print(f"Maya Plugin Path: {maya_plugin_path}")
# except KeyError:
#     print("Error: MAYA_PLUG_IN_PATH environment variable is not set.")
