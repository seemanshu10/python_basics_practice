## Task 7 - Debug & Showcase 

### Table of Contents
- [✔️ Objective](#️-objective)
- [✔️ What You Need to Do](#️-what-you-need-to-do)
  - [📌 Must Check For](#-must-check-for)
  - [📌 Debugging Common Issues](#-debugging-common-issues)
  - [📌 Code Quality Checklist](#-code-quality-checklist)
- [✔️ Use Cases](#️-use-cases)
  - [📌 Using CLI Commands](#-using-cli-commands)
  - [📌 Using Batch Files](#-using-batch-files)
- [✔️ Final Review Checklist](#️-final-review-checklist)
  - [📌 Demo Video](#-demo-video)
  - [📌 Showcase Preparation](#-showcase-preparation)
  - [📌 Task Submission Checklist](#-task-submission-checklist)
- [✔️ Learning Goals](#️-learning-goals)

### ✔️ Objective
* Your project now includes:
    * modular package structure
    * JSON storage
    * validations
    * shot status system
    * notes
    * tasks
    * CLI flags
    * config/constants
    * environment variables
    * markdown report export
    * batch files
    * documentation
> `Now the goal is to turn a working project into a polished portfolio project.`

This is the final Task of the ShotTrack CLI project.
* In this you will polish the project and prepare it for presentation.
    * By the end of this task, you should be able to:
        * improve code quality
        * refactor repeated logic
        * clean messy code
        * test all features
        * debug common issues
        * verify the project structure
        * prepare a demo video
        * prepare presentation slides
        * confidently showcase the project
* This is the professional finishing stage of the project.

### ✔️ What You Need to Do
* **Final Deliverables**
    * You must submit:
        * final working source code
        * cleaned/refactored project folder
        * tested application
        * updated README.md
* **Final Refactoring**
    * Improve code readability, structure, and maintainability.

#### 📌 Must Check For
* **Repeated Logic**
    * Examples: 
    * repeated `find_shot()` patterns
        * repeated validation messages
        * repeated file loading/saving patterns
        * repeated task lookup loops
    * If repeated logic exists:
        * move it into helper functions
        * reuse functions
        * simplify large functions
* **Improve Naming**
    * Check if names are clear:
        * Bad: → `x = load_shots()`
        * Better: →` shots = load_shots()`
        * Bad: → a =` sys.argv[2]`
        * Better: → `shot_code = sys.argv[2]`
* **Improve Function Size**
    * If a function is too large:
        * split it into smaller functions
        * each function should do one clear job
* **Improve Comments**
    * Add comments only where useful.
    * Example:
    ```python
    # Load all saved shots from JSON file
    shots = load_shots()
    ```
* **Remove Unused Code**
    * unused variables
    * old test prints
    * commented-out code
    * dead functions

### 📌 Debugging Common Issues
you should fix any problems found during testing.
* **Common Issues to Check**
* **Import Errors**
    * Example: → `ModuleNotFoundError`
    * Fix:
        * check folder names
        * check `__init__.py`
        * run from project root
* **JSON Errors**
    * Example: → `JSONDecodeError`
    * Fix:
        * correct broken JSON
        * reset file to: `[]`
* **Wrong Paths**
    * Fix:
        * verify environment variables
        * verify `os.path.join()`
* **Missing Arguments**
    * Ensure program shows helpful messages.
* **Wrong Task IDs**
    * Ensure numeric validation works.

### 📌 Code Quality Checklist
* You should verify:
    * clean folder structure
    * meaningful names
    * no duplicated logic
    * readable output formatting
    * proper indentation
    * PEP8-style formatting as much as possible
    * consistent spacing
    * small reusable functions
    * clear error messages

### ✔️ Use Cases
* **Objective**
    * Manually test every feature of the project.
    * You should test all commands and verify the expected output.

#### 📌 Using CLI Commands
* **Add Shots**
    * Command:
    ```text
    python main.py add-shot SH100
    python main.py add-shot SH101
    ```
    * Expected Output:
    ```text
    Shot SH100 added successfully.
    Shot SH101 added successfully.
    ```
* **List Shots**
    * Command:
    ```text
    python main.py list-shots
    ```
    * Expected Output:
    ```text
    1. SH100 - not_started
    2. SH101 - not_started
    ```
* **Duplicate Validation**
    * Command:
    ```text
    python main.py add-shot SH100
    ```
    * Expected Output:
    ```text
    Shot SH100 already exists.
    ```
* **Invalid Shot Code**
    * Command:
    ```text
    python main.py add-shot test
    ```
    * Expected Output:
    ```text
    Invalid shot code format. Use format like SH010.
    ```
* **Update Status**
    * Command:
    ```text
    python main.py set-status SH100 review
    python main.py set-status SH100 approved
    ```
    * Expected Output:
    ```text
    Status for SH100 updated to review.
    Status for SH100 updated to approved.
    ```
* **Invalid Status**
    * Command:
    ```text
    python main.py set-status SH100 finished
    ```
    * Expected Output:
    ```text
    Invalid status...
    ```
* **Notes**
    * Command:
    ```text
    python main.py add-note SH100 "Need cleanup"
    python main.py view-notes SH100
    ```
    * Expected Output:
    ```text
    Note added to SH100.
    Notes for SH100:
    1. Need cleanup
    ```
* **Tasks**
    * Command:
    ```text
    python main.py add-task SH100 "Roto cleanup"
    python main.py done-task SH100 1
    python main.py delete-task SH100 1
    ```
    * Expected Output:
    ```text
    Task added to SH100.
    Task 1 in SH100 marked as done.
    Task 1 deleted from SH100.
    ```
* **Flags**
    * Command:
    ```text
    python main.py list-shots --pending
    python main.py list-shots --done
    python main.py list-shots --status review
    ```
    * Expected Output:
    ```text
    Displays filtered shot lists based on status.
    ```
* **Export Report**
    * Command:
    ```text
    python main.py export-report
    ```
    * Expected Output:
    ```text
    Daily report exported successfully to daily_report.md
    ```
    * Check File:
    ```text
    daily_report.md
    ```
#### 📌 Using Batch Files
* **Run Commands Quickly**
    * Command:
    ```text
    run.bat list-shots
    ```
    * Expected Output:
    ```text
    Displays the list of shots.
    ```
* **Add Shot Using Batch File**
    * Command:
    ```text
    run.bat add-shot SH200
    ```
    * Expected Output:
    ```text
    Shot SH200 added successfully.
    ```
* **Generate Daily Report**
    * Command:
    ```text
    daily_report.bat
    ```
    * Expected Output:
    ```text
    Daily report exported successfully to daily_report.md
    ```

### ✔️ Final Review Checklist
* You should review:
    * does every command work?
    * does JSON save correctly?
    * does data load after restart?
    * does README explain usage?
    * does report export work?
    * do batch files run?
    * is code clean?
    * are file names correct?
    * is project understandable?

#### 📌 Demo Video
**Objective** → Create a short demo video (2–5 minutes).
* Suggested Flow
    * Introduce project
    * Show folder structure
    * Run CLI commands
    * Add a shot
    * Update status
    * Add note
    * Add task
    * Export report
    * Show README
    * Show batch files
    * Final summary

#### 📌 Showcase Preparation
* you should practice explaining:
    * what the project does
    * why it was built
    * how commands work
    * what Python concepts were used
    * what they learned
    * what could be improved later

#### 📌 Task Submission Checklist
* You should submit:
    * full project folder
    * source code
    * README.md
    * daily_report.md
    * .bat files
    * demo video

### ✔️ Learning Goals
* refactoring mindset
* debugging process
* quality assurance
* project presentation skills
* software delivery mindset
* portfolio building
* confidence in explaining code
