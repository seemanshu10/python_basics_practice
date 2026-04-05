## 🎯 AP. File Management Package(Basic)

### Task Objective
create a Python package and use it from a separate script using proper imports.

### Instructions

In this task, you will:
* Create the following folder structure:

```
dev/
├── file_manager/
│   ├── __init__.py
│   └── operations/
│       ├── __init__.py
│       ├── file_list.py
│       ├── file_create.py
│       ├── file_delete.py
└── use_package.py
```
* Create a package named file_manager
* Add an empty __init__.py file inside file_manager
* Create a folder operations inside the package
* In file_list.py, create a function that shows all files from a directory
* In file_create.py, create a function that creates a file and writes content into it
* In file_delete.py, create a function that deletes a file if it is available
* In use_package.py:
    * Import functions using the package path
    * Call the functions in this order:
    * list files
    * create a file
    * list files again
    * delete the file
    * list files again
* Run the script and verify the output

### Sample Output

```
Files in '.': ['existing_file.txt']
File 'sample.txt' created successfully.
Files in '.': ['existing_file.txt', 'sample.txt']
File 'sample.txt' deleted successfully.
Files in '.': ['existing_file.txt']
```
