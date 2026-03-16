## 🎯 AP. Capture Global Dependencies

### Task Objective
In this task you will:
* View the list of libraries installed in the global Python environment.
* Generate a requirements.txt file from the global environment.
* Create a virtual environment for a project.
* Install dependencies inside the virtual environment using the requirements.txt file.
* Verify that the libraries were installed in the virtual environment.

### Instructions
* First, inspect the libraries installed in your global Python environment.
* Create a requirements.txt file that records those installed libraries and their versions.
* Create a virtual environment inside a new project folder and activate it.
* Use the generated requirements.txt file to install the dependencies into the virtual environment.

### Sample Output

```
C:\my_project> pip list
Package     Version
----------- -------
colorama    0.4.6
requests    2.26.0
pip         23.2.1
setuptools  65.5.0
```

Example requirements.txt

```
colorama==0.4.6
requests==2.26.0
```
