## Task 3 - Validation, Error Handling, Refactor

### ✔️ Objective
* So far, your ShotTrack CLI can:
    * add shots
    * save shots to shots.json
    * load shots from shots.json
    * list saved shots
* Limitations in the current version:
    * users can enter invalid shot codes
    * duplicate shot codes can be added
    * all source code is inside one file
    * error messages are very basic
    * project is not yet organized like a real Python package
* In this task, you will fix all of that.
    * You will improve your existing ShotTrack CLI project by making it Modular
    * By the end of this task, your program should:
        * validate shot codes before saving
        * prevent duplicate shot codes
        * show clear and friendly error messages
        * separate code into multiple modules
        * convert the project into a custom package structure

### ✔️ What You Need to Do

* 📌 **Valid Shot Code Format**
* A shot code must follow this format:
```
SH010
SH020
SH105
```
* Rules:
    * must start with SH
    * must be followed by digits only
    * should be at least 3 digits after SH
    * Valid examples:
        * SH010
        * SH001
        * SH999
    * Invalid examples:
        * 010
        * shot10
        * SH1
        * AB010
        * SH01A
* If the shot code is invalid, show:
```
Invalid shot code format. Use format like SH010.
```
### 📌 Prevent Duplicate Shot Codes
* If SH010 already exists, it should not be added again. Example:
```
python main.py add-shot SH010
python main.py add-shot SH010
```
* Expected output on second command:

```
Shot SH010 already exists.
```
### 📌 Better Error Messages
Your program should handle these situations clearly:
* **No command provided**
    ```
    python main.py
    ```    
    * Output:
    ```
    Please provide a command.
    ```
* **Missing shot code**
    ```
    python main.py add-shot
    ```
    * Output
    ```
    Please provide a shot code.
    ```
* **Invalid command**
    ```
    python main.py update-shot SH010
    ```
    * Output:
    ```
    Invalid command: update-shot
    ```
* **Invalid shot format**
    ```
    python main.py add-shot shot10
    ```
    * Output:
    ```
    Invalid shot code format. Use format like SH010.
    ```
* **Duplicate shot code**
    ```
    python main.py add-shot SH010
    python main.py add-shot SH010
    ```
    * Output:
    ```
    Shot SH010 already exists.
    ```
* **Empty shot list**
    ```
    python main.py list-shots
    ```
    * Output:
    ```
    No shots available.
    ```
### 📌 Modular Code
Instead of writing everything in main.py, you should separate the logic into different modules.
* **Suggested Project Structure**
* Refactor your project so it looks like this:  
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
* **What Each File Should Do**
    * main.py->  Entry point of the program
    * shottrack/cli.py →  Reads sys.argv and decides which command to run
    * shottrack/commands.py →  Contains command functions like add_shot() and list_shots()
    * shottrack/storage.py->  Handles JSON loading and saving
    * shottrack/validators.py →  Checks whether the shot code is valid
    * shottrack/**init**.py->  Makes shottrack a Python package
* **Package Structure**
    * The shottrack/ folder must become a package using: **init**.py
    * This teaches students how custom packages work in real projects.

### ✔️ Use Cases

* **Add shot**
```
python main.py add-shot SH010
```
* **List shots**
```
python main.py list-shots
```
* Validations Expected Behavior
    * Case 1: Add valid shot
    ```
        python main.py add-shot SH010
    ```
    * Output:
    ```
    Shot SH010 added successfully.
    ```   
    * Case 2: Add duplicate shot
    ```
        python main.py add-shot SH010
    ```
    * Output:
    ```
        Shot SH010 already exists.
    ```
    * Case 3: Invalid shot code
    ```
        python main.py add-shot shot10
    ```
    * Output:
    ```
        Invalid shot code format. Use format like SH010.
    ```
    * Case 4: Missing shot code
    ```
        python main.py add-shot
    ```
    * Output:
    ```
        Please provide a shot code.
    ``` 
    * Case 5: Invalid command
    ```
        python main.py remove-shot SH010
    ```
    * Output:
    ```
        Invalid command: remove-shot
        Available commands:
        python main.py add-shot SH010
        python main.py list-shots
    ```
    * Case 6: List shots
    ```
        python main.py list-shots
    ```
    * Output:
    ```
    1. SH010 - not_started
    2. SH020 - not_started
    ``` 

* **Example shots.json**
    * After adding shots, the file should look like this: Example shots.json
```json
[
    {
        "shot_code": "SH010",
        "status": "not_started"
    },
    {
        "shot_code": "SH020",
        "status": "not_started"
    },
    {
        "shot_code": "SH030",
        "status": "not_started"
    }
]
```

* If No Shots Exist Yet
```
[]
```
### ✔️ Learning Goals

* why refactoring matters
* how to organize code into modules
* how custom packages work
* how validation improves quality
* how to prevent duplicate data
* how to write better CLI tools
* how better error messages improve user experience
