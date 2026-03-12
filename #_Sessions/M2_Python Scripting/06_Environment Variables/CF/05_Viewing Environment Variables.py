import os

# Print all variables
# for key, value in os.environ.items():
#     print(f"{key}: {value}")

# Access a specific variable
# maya_plugin_path = os.environ.get('MAYA_PLUG_IN_PATH')
maya_plugin_path = os.environ['MAYA_PLUG_IN_PATH']

print(f"Maya Plugin Path: {maya_plugin_path}")

