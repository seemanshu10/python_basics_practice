## 🎯 AP. Create & Manage Virtual ENV

### Task Objective

In this task you will:

* Create a virtual environment inside a project folder.
* Activate and deactivate the virtual environment.
* Install a package inside the virtual environment.
* Run a Python script that depends on the installed package.
* Observe how the virtual environment isolates project dependencies.

### Instructions
* Create a virtual environment named **myenv** inside a project folder.
* Activate the environment and install a package required by the provided Python script.
  * example.py
    ```python
    from colorama import Fore

    print(Fore.GREEN + "This is running inside the virtual environment!")
    ```
* Run the script while the environment is active and verify the output in the terminal.
* Deactivate the environment after completing the task.

### Sample Output
```
(myenv) C:\project> python example.py

This is running inside the virtual environment!
```
