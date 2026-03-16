## 🎯 AP. Setting Up Virtual ENV & Installing Modules

### Task Objective

In this task, you will:
* Set up a dedicated virtual environment for a project.
* Install the required module from the `requirements.txt` file.
* Run the provided script inside the virtual environment.
* Verify that the script runs successfully and displays the expected output.

### Instructions

* Create a virtual environment named `.venv` in your project directory.
* Activate the virtual environment before proceeding.
* Use `pip` to install the module from the `requirements.txt` file.
* Save the provided code in a Python script file named `process_items.py`.
* Run the script and check that the progress bar and processed output appear in the terminal.


### `process_items.py`

```python
import time
from tqdm import tqdm

def process_items(items):
    for item in tqdm(items, desc="Processing items"):
        time.sleep(0.1)
        processed_item = item * 2
        print(f"Processed: {processed_item}")

if __name__ == "__main__":
    items_to_process = list(range(100))
    process_items(items_to_process)
```


### Sample Output

```
(myenv) C:\YourProject> python process_items.py
Processing items: 100%|████████████████████████████| 100/100 [00:10<00:00,  9.95it/s]
Processed: 0
Processed: 2
Processed: 4
...
Processed: 198
```
