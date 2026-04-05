## 🎯 AP. Pipeline Tool Package (Intermediate)

### Task Objective
Create and use a multi-level package with __init__.py and import it using sys.path.insert().

### Instructions

In this task, you will:
* Create the following folder structure:

```
day/
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
* In project_config/__init__.py:
* Print a message when the package is loaded
* Make all three functions available at the package leve
* In use_package.py:
* Complete the missing setup so the package can be imported
* Use sys.path.insert() to add the correct path
* Use the following code inside use_package.py:
```python
from pipeline_tools.project_config import (
    get_default_settings,
    validate_resolution,
    generate_report
)

settings = get_default_settings()

if validate_resolution(settings["resolution"]):
    print("Resolution is valid.")
else:
    print("Resolution is invalid.")

print(generate_report(settings))
```
* Add any missing code required to make this script run successfully
* Run the script and verify the output

### Sample Output

```
Initializing project_config package...
Resolution is valid.
Project Report
--------------
Name       : Dragon Quest
Resolution : 1920x1080
FPS        : 24
```
