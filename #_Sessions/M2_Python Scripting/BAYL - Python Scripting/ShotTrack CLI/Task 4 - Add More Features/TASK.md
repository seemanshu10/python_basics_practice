## Task 4 - Add More Features

### ✔️ Objective
* So far, your project can:
    * add shots
    * validate shot codes
    * prevent duplicates
    * save/load JSON
    * list shots
    * use modules and package structure

Now you will make the tracker more production-like.
* Each shot should now be able to store:
    * a status
    * multiple notes
    * multiple tasks
* This makes the project feel much more like a simple VFX tracking tool.
* So now, you will upgrade ShotTrack CLI from a basic shot tracker into a more realistic VFX production helper.
* By the end of this task, your program should be able to:
    * update shot status
    * validate allowed status values
    * add notes to shots
    * view notes for a shot
    * add tasks inside a shot
    * mark tasks as done
    * delete tasks
    * support basic CLI flags
    * handle missing arguments and invalid input better
    * keep a clean entry point using if **name** == "**main**":

### ✔️ What You Need to Do

* 📌 **Updated Project Structure**
* Your project should still use this structure:

```text
shottrack_cli/
├── main.py
├── shots.json
└── shottrack/
    ├── __init__.py
    ├── cli.py
    ├── commands.py
    ├── storage.py
    └── validators.py
```

* You may keep the same files and expand them.
* **New Data Structure**
    * Each shot should now look like this inside shots.json:
```json
[
    {
        "shot_code": "SH010",
        "status": "not_started",
        "notes": [
            "Need updated plate from client"
        ],
        "tasks": [
            {
                "id": 1,
                "title": "Roto cleanup",
                "status": "pending"
            },
            {
                "id": 2,
                "title": "Paint wire removal",
                "status": "done"
            }
        ]
    }
]
```
* Each sot now contains:
    * shot_code
    * status
    * notes
    * tasks
* **Allowed Shot Status Values**
    * Only these statuses should be allowed:
        * not_started
        * in_progress
        * review
        * approved
        * hold
    * If any other status is given, the program should reject it. Example:
    ```
        python main.py set-status SH010 completed
    ```
    * Output:
    ```
        Invalid status. Allowed values: not_started, in_progress, review, approved, hold
    ```
* **📌 Commands**
1. **Set shot status**
    ```
    python main.py set-status SH010 review
    ```
    * Expected:
    ```
    Status for SH010 updated to review.
    ```
2. **Add note**
    ```
    python main.py add-note SH010 "Need cleanup on left edge"
    ```
    * Expected:
    ```
    Note added to SH010.
    ```
3. **View notes**
    ```
    python main.py view-notes SH010
    ```
    * Expected:
    ```
        Notes for SH010:
        1. Need cleanup on left edge
        2. Check hair detail in frame 102
    ```
    * If no notes exist:
    ```
    No notes found for SH010.
    ```
4. **Add task to shot**
    ```
    python main.py add-task SH010 "Roto cleanup"
    ```
    * Expected:
    ```
    Task added to SH010.
    ```
5. **Mark task as done**
    ```
    python main.py done-task SH010 1
    ```
    * Expected:
    ```
    Task 1 in SH010 marked as done.
    ```
6. **Delete task**
    ```
    python main.py delete-task SH010 2
    ```
    * Expected:
    ```
    Task 2 deleted from SH010.
    ```
### 📌 Create flags
* **Show only pending shots** ( --pending )
    ```
    python main.py list-shots --pending
    ```
    * This should list only shots whose status is not approved.
* **Show only approved/done shots** (  --done )
    ```
    python main.py list-shots --done
    ```
    * This should list only shots whose status is approved.
* **Filter by exact status** ( --status )
    ```
    python main.py list-shots --status review
    ```
    * This should list only review shots.

*  📌 CLI Edge Cases to Handle
    * Your program should handle these clearly:
        * No command provided
            * Output: ```Please provide a command.```
        * Unknown command
            * Output: ```Invalid command: remove-shot```
        * Missing shot code
            * Output: ```Please provide a shot code.```
        * Missing note text
            * Output: ```Please provide note text.```
        * Missing task title
            * Output: ```Please provide task title.```
        * Missing status
            * Output: ```Please provide a status value.```
        * Invalid status
            * Output: ```Invalid status. Allowed values: not_started, in_progress, review, approved, hold```
        * Invalid shot code
            * Output: ```Invalid shot code format. Use format like SH010.```
        * Shot not found
            * Output: ```Shot SH050 not found.```
        * Invalid task ID
            * Output: ```Task ID must be a number.```   
        * Task ID not found
            * Output: ```Task 3 not found in SH010.```
        * No notes found
            * Output: ```No notes found for SH010.```

* 📌 Update CLI parsing
    * In cli.py, update run() so it can read and route:
        * ```set-status```
        * ```add-note```
        * ```view-notes```
        * ```add-task```
        * ```done-task```
        * ```delete-task```
        * ```list-shots --pending```
        * ```list-shots --done```
        * ```list-shots --status review```

### ✔️Use Cases
* **Add first shot**
    ```bash
    python main.py add-shot SH010
    ```
    * Output:
    ```bash
    Shot SH010 added successfully.
    ```

* **Add second shot**
    ```bash
    python main.py add-shot SH020
    ```
    * Output:
    ```bash
    Shot SH020 added successfully.
    ```
* **Update status of SH010**
    ```bash
    python main.py set-status SH010 review
    ```
    * Output:
    ```bash
    Status for SH010 updated to review.
    ```
* **Update status of SH020**
    ```bash
    python main.py set-status SH020 approved
    ```
    * Output:
    ```bash
    Status for SH020 updated to approved.
    ```
* **Add first note to SH010**
    ```bash
    python main.py add-note SH010 "Need better edge cleanup"
    ```
    * Output:
    ```bash
    Note added to SH010.
    ```
* **Add second note to SH010**
    ```bash
    python main.py add-note SH010 "Check frame 102"
    ```
    * Output:
    ```bash
    Note added to SH010.
    ```
* **View notes for SH010**
    ```bash
    python main.py view-notes SH010
    ```
    * Output:
    ```bash
    Notes for SH010:
        1. Need better edge cleanup
        2. Check frame 102
    ```
* **Add first task to SH010**
    ```bash
    python main.py add-task SH010 "Roto cleanup"
    ```
    * Output:
    ```bash
    Task added to SH010.
    ```
* **Add second task to SH010**
    ```bash
    python main.py add-task SH010 "Paint wire removal"
    ```
    * Output:
    ```bash
    Task added to SH010.
    ```
* **Mark task 1 as done**
    ```bash
    python main.py done-task SH010 1
    ```
    * Output:
    ```bash
    Task 1 in SH010 marked as done.
    ```
* **Delete task 2**
    ```bash
    python main.py delete-task SH010 2
    ```
    * Output:
    ```bash
    Task 2 deleted from SH010.
    ```
* **List pending shots**
    ```bash
    python main.py list-shots --pending
    ```
    * Output:
    ```bash
    1. SH010 - review
    ```
* **List approved shots**
    ```bash
    python main.py list-shots --done
    ```
    * Output:
    ```bash
    1. SH020 - approved
    ```
* **List only review shots**
    ```bash
    python main.py list-shots --status review
    ```
    * Output:
    ```bash
    1. SH010 - review
    ```

* **Example shots.json** 
    ```json
    [
        {
            "shot_code": "SH010",
            "status": "review",
            "notes": [
                "Need better edge cleanup",
                "Check frame 102"
            ],
            "tasks": [
                {
                    "id": 1,
                    "title": "Roto cleanup",
                    "status": "done"
                }
            ]
        },
        {
            "shot_code": "SH020",
            "status": "approved",
            "notes": [],
            "tasks": []
        }
    ]
    ```

### ✔️ Learning Goals
* What you Learn in This Task
    * how nested JSON structures work
    * how to store notes and tasks inside a shot
    * how to validate status values
    * how to work with IDs
    * how to support CLI flags
    * how to handle edge cases more professionally
    * how to keep main.py clean
    * how a real CLI tool grows step by step
