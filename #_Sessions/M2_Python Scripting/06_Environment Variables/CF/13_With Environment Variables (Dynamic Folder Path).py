import os, json

def load_config(config_filename):
    config_folder = os.environ.get('CONFIG_FOLDER')

    if not config_folder:
        print("❌ Error: CONFIG_FOLDER environment variable is not set.")
        return

    config_path = os.path.join(config_folder, config_filename)

    try:
        with open(config_path, 'r') as file:
            config = json.load(file)
            print(f"\n✅ Loaded configuration from: {config_path}")
            print(json.dumps(config, indent=2))
    except FileNotFoundError:
        print(f"❌ File not found: {config_filename}")
    except json.JSONDecodeError:
        print(f"❌ Invalid JSON in file: {config_filename}")

# Run
load_config('database.json')
load_config('logging.json')
