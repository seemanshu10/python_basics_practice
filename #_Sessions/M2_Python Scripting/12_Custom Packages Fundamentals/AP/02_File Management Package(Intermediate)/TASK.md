## 🎯 AP. File Management Package(Intermediate)

### Task Objective
build and use a multi-level Python package using __init__.py

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
* Create the package file_manager with a subfolder named operations
    * In file_list.py, create a function that shows all files from a directory
    * In file_create.py, create a function that creates a file and writes content into it
    * In file_delete.py, create a function that deletes a file if it is available
* In operations/__init__.py, should allow access to all file operations Functions.
* In file_manager/__init__.py, should allow access to individual modules
* Create a file named use_package.py
* In use_package.py, complete the script so that, The package can be imported correctly
* Use the following code inside use_package.py:

```python
import file_manager

file_manager.list_files()
file_manager.create_file("sample.txt", "Hello, this is a test file.")

file_manager.list_files()

file_manager.delete_file("sample.txt")
file_manager.list_files()
```
* Run the script and verify the output

### Sample Output

```
Initializing file_manager package...
Initializing operations subpackage...

Files in '.': ['existing_file.txt']
File 'sample.txt' created successfully.
Files in '.': ['existing_file.txt', 'sample.txt']
File 'sample.txt' deleted successfully.
Files in '.': ['existing_file.txt']
```
