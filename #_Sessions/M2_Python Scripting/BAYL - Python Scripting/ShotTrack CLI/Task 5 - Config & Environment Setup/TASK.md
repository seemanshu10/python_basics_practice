## Task 5 - Config & Environment Setup 

### Table of Contents
- [✔️ Objective](#️-objective)
- [✔️ What You Need to Do](#️-what-you-need-to-do)
    - [📌 Updated Project Structure](#-updated-project-structure)
    - [📌 What You Need to Build](#-what-you-need-to-build)
    - [📌 ENV Variables to Support](#-env-variables-to-support)
    - [📌 You Must ](#-you-must)
- [✔️ Expected Behavior](#️-expected-behavior)
- [✔️ Use Cases ](#️-use-cases)
    - [📌 Normal Use](#-normal-use)
    - [📌 Testing Configuration ](#-testing-configuration)
- [✔️ Learning Goals](#️-learning-goals)

### ✔️ Objective
Right now, your project stores shot data in a fixed file like:
```text
"shots.json"
```
That means the file location is hard-coded. This is not flexible.
In real projects, configuration should be changeable without editing source code.
* So in this task, you will make the JSON file path configurable using:
    * constants.py
    * config.py
    * environment variable: SHOT_DATA_FILE

In this task, you will improve ShotTrack CLI by removing hard-coded values and making the JSON file path configurable.

By the end of this task, your project should:
* use a constants.py file
* use a config.py file
* read the JSON file path from an environment variable
* use a default JSON file if no environment variable is set
* remove hard-coded file names from the code
* use the os module for path handling
* run properly inside a virtual environment

### ✔️ What You Need to Do

#### 📌 Updated Project Structure

Your project should now look like this:

```text
shottrack_cli/
├── main.py
├── .env_example.txt
├── venv/
└── shottrack/
    ├── __init__.py
    ├── cli.py
    ├── commands.py
    ├── storage.py
    ├── validators.py
    ├── constants.py
    └── config.py
```
You may still have your JSON file, but now its location should be configurable.

#### 📌 What You Need to Build
You will now add:
* **constants.py**
    * This file will store fixed values like:
        * allowed statuses
        * default JSON file name
* **config.py**
    * This file will read values from environment variables and provide defaults if they are missing.
    * Example environment variables: SHOT_DATA_FILE
* **Update all path handling**
* Wherever you build file/folder paths, use os.path.join() only.
    * Do not use:
        * hard-coded full absolute paths
        * pathlib
* **Virtual environment setup**
    * you should create and activate a virtual environment for this project.

#### 📌 ENV Variables to Support
* `SHOT_DATA_FILE`
* This is the path to the JSON file storing shot data.
    * Example:
    ```text
        SHOT_DATA_FILE=shots.json
    ```
    * or
    ```text
       SHOT_DATA_FILE=data\shots.json
    ```

#### 📌 You Must
* If `SHOT_DATA_FILE` is not set, use default shots.json
* If `SHOT_DATA_FILE` is set, use that file instead
* If the folder does not exist, create it automatically
* Keep `main.py` clean
* Use only os for file path handling
* **you should do all of the following:**
    * create constants.py
    * create config.py
    * replace hard-coded values
    * use os.getenv() for config
    * use os.path.join() if building paths
    * update storage.py to use config
    * test with default values
    * test with custom environment variables
    * create a virtual environment
    * run the project inside the virtual environment

### ✔️ Expected Behavior
Your project should work in these two cases:
* **Case 1: No environment variables set**
    * Then the project should use defaults, such as: `shots.json`
* **Case 2: Environment variables are set**
    * Then the project should use the custom values.
    * For example: `SHOT_DATA_FILE=data\custom_shots.json`
    * Then the program should use those values instead of the defaults.

### ✔️ Use Cases
#### 📌 Normal Use
* **Use Case 1: Run with Default Config**
    * If no environment variables are set, the project will automatically use the default file: shots.json
    * Command
    ```
    python main.py list-shots
    ```
    * Expected Output (if no shots exist)
    ```
    No shots available.
    ```
    * Expected Output (if shots already exist)
    ```
    1. SH030 - in_progress
    2. SH100 - not_started
    ```
* **Use Case 2: Add a New Shot**
    * Command
    ```
    python main.py add-shot SH030
    ```    
    * Expected Output
    ```
    Shot SH030 added successfully.
    ```
    * If Shot Already Exists
    ```
    Shot SH030 already exists.
    ```
* **Use Case 3: Update Shot Status**
    * Command   
    ```
    python main.py set-status SH030 in_progress
    ```
    * Expected Output
    ```
    Status for SH030 updated to in_progress.
    ```
    * Verify by Listing Shots
    ```
    python main.py list-shots
    ```
    * Output
    ```
    1. SH030 - in_progress
    ```

#### 📌 Testing Configuration

* **Test 1: No Environment Variables**
    * When no environment variables are set, the project should use: shots.json
    * Run Commands
    ```
    python main.py add-shot SH100
    python main.py list-shots
    ```
    * Expected Output
    ```
    Shot SH100 added successfully.

    1. SH100 - not_started
    ```
    * This confirms the program created and used the default JSON file.

* **Test 2: Custom data file**
    * set
    ```
    set SHOT_DATA_FILE=data\my_shots.json
    ```
    * Run
    ```
    python main.py add-shot SH200
    python main.py list-shots
    ```
    * Expected Output
    ```
    Shot SH200 added successfully.

    1. SH200 - not_started
    ```
* Now the program should use data\my_shots.json.

### ✔️ Learning Goals
* What you Learn in This Task
    * why hard-coded paths are bad
    * how constants improve maintainability
    * how config improves flexibility
    * how environment variables work
    * how to use the os module for paths
    * how to prepare projects using virtual environments
    * how professional Python projects become portable across systems
