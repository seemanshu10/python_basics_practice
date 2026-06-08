## Task 1 - ShotTrack CLI

### Table of Contents
- [✔️ Objective](#️-objective)
- [✔️ What You Need To Do](#️-what-you-need-to-do)
  - [📌 Required Commands](#-required-commands)
  - [📌 Other Features](#-other-features)
- [✔️ Use Cases](#️-use-cases)
- [✔️ Learning Goals](#️-learning-goals)

### ✔️ Objective
* Build a simple command-line tool in Python to manage VFX shots.
    * By the end of this task, your program should be able to:
        * run from terminal
        * read commands using ```sys.argv```
        * create shot records
        * store data in memory
        * list all created shots
* Project Structure
    * Create this folder and file:
    ```text
    shottrack_cli/
    └── main.py
    ```
* VFX Shot Example
    * In VFX studio`s, shots are often named like:
        * SH010
        * SH020
        * SH030
    * Each shot can have a status, such as:
        * ```not_started```
        * ```in_progress```
        * ```review```
        * ```approved```
* For this task, every new shot should start with the default status: ```not_started```

### ✔️ What You Need To Do

#### 📌 Required Commands
* Your program should support:
1. **add-shot**
    * Command: ```python main.py add-shot SH010```
    * Expected result: ```Shot SH010 added successfully.```
2. **list-shots**
    * Command: ```python main.py list-shots```
    * Expected result:
        ``` 
        1. SH010 - not_started
        2. SH020 - not_started
        ```
#### 📌 Other Features
* **When adding a shot:**
    * shot code comes from terminal argument
    * default status should be ```not_started```
* **Shot data should be stored in memory using:**
    * a list
    * dictionaries inside the list
* **Example structure**:
    ```python
    shots = [
        {"shot_code": "SH010", "status": "not_started"},
        {"shot_code": "SH020", "status": "not_started"}
    ]
    ```
* Important: since the data is only stored in memory, it will reset every time you run the script again.
* If you run the file again, data will reset because it is only stored in memory.
* Because this version uses in-memory storage: ```shots = []```
* Each time you run the script, data resets.

### ✔️ Use Cases
* Test 1 → ```python main.py add-shot SH010```
* Test 2 → ```python main.py add-shot SH020```
* Test 3 → ```python main.py list-shots```

### ✔️ Learning Goals
* By doing this task, you should understand:
    * how sys.argv works
    * how terminal commands are passed to Python
    * how to build simple CLI tools
    * how to use lists and dictionaries for real data
    * how to structure a Python script
