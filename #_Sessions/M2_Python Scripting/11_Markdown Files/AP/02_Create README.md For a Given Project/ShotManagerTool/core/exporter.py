import json

def export_shots_to_json(shots, filepath="shots_export.json"):
    with open(filepath, "w") as f:
        json.dump(shots, f, indent=4)

    print(f"Shots exported to {filepath}")