## 🎯 AP. Pipeline Tool Package (Basic)

### Task Objective
create and use a multi-level Python package from another folder

### Instructions

In this task, you will:
* Create the following folder structure:

```
dev/
├── pipeline_tools/
│   ├── __init__.py
│   └── project_config/
│       ├── __init__.py
│       ├── settings.py
│       ├── validator.py
│       └── report.py
tools/
└── use_package.py
```
* Create a package named pipeline_tools
* Inside it, create a subpackage named project_config
* Add an empty __init__.py file inside both pipeline_tools and project_config
* In settings.py, create a function that returns default project settings:
    * Project name
    * Resolution (example: "1920x1080")
    * FPS
* In validator.py, create a function that checks if a resolution is in valid format (widthxheight)
* In report.py, create a function that takes the settings and returns formatted project details
* Create a file named use_package.py inside the tools folder
* In use_package.py:
    * Add the path of the dev folder using sys.path
    * Import functions using the full package path
    * Call the functions in this order:
        * get settings
        * validate resolution
        * generate report
    * Print the validation result and the report
* Run the script and verify the output

### Sample Output

```
Resolution is valid.
Project Report
--------------
Name       : Dragon Quest
Resolution : 1920x1080
FPS        : 24
```
