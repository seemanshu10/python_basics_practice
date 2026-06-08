## Task 6 - Docs, Export & Batch

### Table of Contents
- [✔️ Objective](#️-objective)
- [✔️ What You Need to Do](#️-what-you-need-to-do)
  - [📌 Updated Project Structure](#-updated-project-structure)
  - [📌 Create MD File README.md](#-create-md-file-readmemd)
  - [📌 Markdown Exporter](#-markdown-exporter)
  - [📌 Batch Files](#-batch-files)
  - [📌 Required Command](#required-command)
  - [📌 Implementation Tasks](#-implementation-tasks)
- [✔️ Use Cases](#️use-cases)
  - [📌 Normal Use](#-normal-use)
  - [📌 Batch Files Uses](#-batch-files-uses)
- [✔️ Learning Goals](#️-learning-goals)

### ✔️ Objective
So far, your project already works as a CLI tool.
* Now, you will make it feel more like a real software project by adding three practical improvements:
    * Project documentation using README.md
    * A simple Markdown exporter that creates a daily report file
    * Windows batch files to run the project more easily
* By the end of this task, your project should:
    * contain a proper README.md
    * generate a daily_report.md file from shot data
    * include run.bat
    * include daily_report.bat

### ✔️ What You Need to Do
#### 📌 Updated Project Structure
* Your project should now look like this:
```text
shottrack_cli/
├── main.py
├── README.md
├── daily_report.md
├── run.bat
├── daily_report.bat
├── .env_example.txt
└── shottrack/
    ├── __init__.py
    ├── cli.py
    ├── commands.py
    ├── storage.py
    ├── validators.py
    ├── constants.py
    ├── config.py
    └── exporter.py
```
#### 📌 Create MD File README.md
* Create a README.md file for the project.
    * The README.md should include:
        * project title
        * project description
        * features
        * commands supported
        * setup instructions
        * virtual environment setup
        * example usage
* It should clearly explain:
    * what the project does
    * how to set it up
    * how to activate virtual environment
    * how to run commands
    * how to export the report
* Minimum README.md Structure
    ```markdown
    # ShotTrack CLI

    ## Project Description
    A simple VFX-themed Python CLI tool for managing shots, notes, tasks, and statuses.

    ## Features
    - Add shots
    - List shots
    - Update shot status
    - Add notes
    - Add tasks
    - Export daily report

    ## Setup
    ...

    ## Commands
    ...

    ## Example Usage
    ...
    ```

#### 📌 Markdown Exporter
* Add one simple feature:
    ```text
    python main.py export-report
    ```
    * This command should create a file named: daily_report.md
* **What the exporter should do**
    * It should read all shot data from the JSON file and write a Markdown report.
        ```markdown
        # Daily Shot Report

        ## SH010
        - Status: review
        - Notes Count: 2
        - Pending Tasks: 1
        - Done Tasks: 1

        ## SH020
        - Status: approved
        - Notes Count: 0
        - Pending Tasks: 0
        - Done Tasks: 2
        ```
#### 📌 Batch Files
* **`run.bat`**
    * This batch file should allow students to run any CLI command more quickly.
    * Usage:
        ```
        run.bat list-shots
        run.bat add-shot SH050
    ```
* **`daily_report.bat`**
    * This batch file should generate the markdown report quickly.
        * Usage:
            * double-click the file
            * or run it from terminal

#### 📌 Required Command
Your program must support:
```text
python main.py export-report
```
Expected output:
```text
Daily report exported successfully to daily_report.md
```

#### 📌 Implementation Tasks
* Create expo**rter.py
    * Create a new module:
    ```
    shottrack/exporter.py
    ```
* Inside it, create a function that:
* loads shot data
    * converts it into markdown text
    * writes the markdown into `daily_report.md`
* Update `commands.py`
    * Add a new command function: `export_report()`
    * This should call the exporter.
* **Update `cli.py`**
    * Add support for: → python main.py export-report
* **Create Batch Files**
    * Create: → `run.bat` , `daily_report.bat`

### ✔️Use Cases

#### 📌 Normal Use
* Add a shot → `python main.py add-shot SH010`
* List shots →` python main.py list-shots`
* Update shot status → `python main.py set-status SH010 review`
* Add a note → `python main.py add-note SH010 "Need cleanup in top corner"`
* Add a task → `python main.py add-task SH010 "Roto cleanup"`
* Export daily report → `python main.py export-report`

#### 📌 Batch Files Uses
* Run commands quickly → `run.bat list-shots`
* Generate markdown report → `daily_report.bat`
* Example `daily_report.md`
    ```markdown
    # Daily Shot Report

    ## SH010
    - Status: review
    - Notes Count: 2
    - Pending Tasks: 1
    - Done Tasks: 1

    ## SH020
    - Status: approved
    - Notes Count: 0
    - Pending Tasks: 0
    - Done Tasks: 2
    ```

### ✔️ Learning Goals
* markdown file basics
* writing project documentation
* structuring a `README.md`
* writing markdown from Python
* creating a simple exporter module
* creating `.bat `files
* basic Windows automation
* improving project usability
