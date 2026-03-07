## 🎯 AP. Render Module

### Task Objective

* You will build a system that can read and analyze a list of render tasks.
* The system will calculate the total number of tasks.
* It will identify which tasks are still pending and exclude completed ones.
* All logic will be separated into clean, reusable parts to keep things organized.
* The results will be displayed in a clear, structured summary.

### Instructions

Inside a folder named `render_manager/`, create three files: `task_reader.py`, `task_processor.py`, and `main.py`.

In `task_reader.py`, write a function to read all tasks from a given file and return them as a list of strings.

In `task_processor.py`, write two functions:

* One that counts the total number of tasks in the list.
* One that filters out all tasks that are marked as completed and returns the remaining task IDs.

In `main.py`:

* Import the above two modules.
* Load and process the task data from a file named `render_tasks.txt`.
* Print the total number of tasks and a list of pending task IDs.

### Sample Output

Given a `render_tasks.txt` file with the following content:

```
Task: T001 | Status: In Progress | Time: 2h  
Task: T002 | Status: Completed | Time: 1h  
Task: T003 | Status: Failed | Time: 3h  
Task: T004 | Status: In Progress | Time: 4h  
Task: T005 | Status: Completed | Time: 2.5h  
```

Running `main.py` should produce:

```
Total Tasks: 5  
Pending Tasks: ['T001', 'T003', 'T004']  
```
