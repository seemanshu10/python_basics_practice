"""
write two functions:

One that counts the total number of tasks in the list.
One that filters out all tasks that are marked as completed and returns the remaining task IDs.

"""

def count_tasks(task_list):
    """
    Returns the total number of tasks in the list.
    """
    # print(task_list)
    return len(task_list)

def get_pending_task_ids(task_list):
    """
    Filters out completed tasks and returns a list of pending task IDs.
    """
    pending_tasks = []

    for task in task_list:
        # Task: T001 | Status: In Progress | Time: 2h
        parts = task.split('|')
        
        task_id_part = parts[0].strip()       # "Task: T001"
        status_part = parts[1].strip()        # "Status: In Progress"

        task_id = task_id_part.split(':')[1].strip()
        status = status_part.split(':')[1].strip()

        if status.lower() != "completed":
            pending_tasks.append(task_id)

    return pending_tasks