import os 
import json

DIR_PATH = os.path.dirname(os.path.abspath(__file__))
# print(DIR_PATH)

# enironment - files 
ENV_FILES = {
    "dev": "dev_settings.json",
    "test": "test_settings.json",
    "prod": "prod_settings.json"
} 

# Read the RENDER_ENV system environment variable
renderEnv_value = os.environ.get("RENDER_ENV")
print("Existing Render Env Value: ",renderEnv_value)

# if render is none or missing 
if renderEnv_value is None:
    print("WARNINGL Render varaible not set. Deafault to dev environment.")
    renderEnv_value = "dev"

# if invalid env given 
if renderEnv_value not in ENV_FILES:
    print(f"Error: ")
    print(f"ERROR: Invalid RENDER_ENV value '{renderEnv_value}'.")
    print("Allowed values: dev, test, prod")
    exit()

# Get the corresponding file
settings_file = ENV_FILES[renderEnv_value]

try:
    # Load JSON file
    setting_path_Input = os.path.join(DIR_PATH,"RenderSettings", settings_file)
    print(setting_path_Input)
    with open(setting_path_Input, "r") as file:
        settings = json.load(file)

    print(f"\nLoaded settings for environment: {renderEnv_value}\n")
    print(json.dumps(settings, indent=4))

except FileNotFoundError:
    print(f"ERROR: Settings file '{settings_file}' not found.")
except json.JSONDecodeError:
    print(f"ERROR: '{settings_file}' contains invalid JSON.")