import os

from shottrack.storage import load_json_shot_data
from shottrack.config import get_shot_data_file_path

def generate_markdown_report():
    shots = load_json_shot_data()

    lines = []
    lines.append("# Daily Shot Report\n")

    if not shots:
        lines.append("No shots available.\n")
        return "\n".join(lines)

    for shot in shots:
        shot_id = shot.get("shot_code")
        status = shot.get("status")

        notes = shot.get("notes", [])
        tasks = shot.get("tasks", [])
        number_pending_task = 0
        number_done_task = 0
        for task in tasks:
            # print(pending_task["status"])
            if task["status"] == "done":
                number_done_task += 1
            elif task["status"] in ["hold", "not_started", "in_progress","review"]:
                number_pending_task += 1
                

        lines.append(f"## {shot_id}")
        lines.append(f"- Status: {status}")
        lines.append(f"- Notes Count: {len(notes)}")
        lines.append(f"- Pending Tasks: {number_pending_task}")
        lines.append(f"- Done Tasks: {number_done_task}\n")

    return "\n".join(lines)

def export_report():
    content = generate_markdown_report()
    print(content)
    export_report_file_json_path = get_shot_data_file_path()
    # print(os.path.dirname(export_report_file_json_path))

    daily_report_file_path = os.path.join(os.path.dirname(export_report_file_json_path),"daily_report.md")
    with open(daily_report_file_path, "w") as f:
        f.write(content)

    print("Daily report exported successfully to daily_report.md")

if __name__ == "__main__":
    export_report()