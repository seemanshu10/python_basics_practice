"""
Import the above two modules.
Load and process the task data from a file named render_tasks.txt.
Print the total number of tasks and a list of pending task IDs.
"""

from render_manager import task_reader as tr
from render_manager import task_processor as tp

# main function call 
def main():
    file_path = r"#_Sessions\M2_Python Scripting\01_Python Modules\AP\02_Render Module\renderData\render_tasks.txt"

    tasks = tr.read_tasks(file_path)
    total = tp.count_tasks(tasks)
    pending = tp.get_pending_task_ids(tasks)

    print(f"Total Tasks: {total}")
    print(f"Pending Tasks: {pending}")

main()