## Task 2 - Save & Load Shot Data

### ✔️ Objective
In Task 1, shot data was stored only in memory using: ```shots = []```
This means that once the program stops running, all shot data is lost.
* In this task, you will
    * you will improve the ShotTrack CLI by saving shot data into a file ```shots.json```
    * This will allow the program to remember previously added shots even after restarting.

### ✔️ What You Need to Do

* 📌 **Project Structure**
* Your project should now look like this:
```text
shottrack_cli/
├── main.py
└── shots.json
```
* If ```shots.json``` does not exist, the program should create it automatically.
* 📌 **Required Commands**
1. **add-shot**
```
python main.py add-shot SH010
```
* Expected behavior:
    * load existing shots from ```shots.json```
    * add the new shot
    * save updated data back to ```shots.json```
2. **list-shots**
```
python main.py list-shots
```
* Expected behavior:
    * load shot data from ```shots.json```
    * show all saved shots
* **Required JSON Structure**
* After running:
```
python main.py add-shot SH010
python main.py add-shot SH020

```
* Your shots.json should look like:
```json
[
    {
        "shot_code": "SH010",
        "status": "not_started"
    },
    {
        "shot_code": "SH020",
        "status": "not_started"
    }
]
```

### 📌 Other Features
* The file name must be ```shots.json```
* Each shot must be stored as a dictionary
* All shots must be stored inside a list
* When the file does not exist, create it with an empty list: ```[]```
* When listing shots, load data from file first
* When adding a shot, load data first, then append, then save
* handle invalid JSON safely.
* For example:
    * if shots.json is empty
    * if JSON is broken
    * if file contains wrong data
* They do not have to solve that immediately, but it is a great discussion point.

### ✔️ Use Cases

* **First run**
```
python main.py list-shots
```
* Output:

```
No shots available.
```
And shots.json should now exist.

* **Add a shot**

```
python main.py add-shot SH010
```
* Output:

```
Shot SH010 added successfully.
```
* **Add another shot**

```
python main.py add-shot SH020
```
* Output:

```
Shot SH020 added successfully.
```
* **List again**

```
python main.py list-shots
```
* Output:
```
1. SH010 - not_started
2. SH020 - not_started
```
* **Restart program and list again**

```
python main.py list-shots
```
* Output should still be:

```
1. SH010 - not_started
2. SH020 - not_started
```
* That confirms persistent storage is working.

### ✔️ Learning Goals
By doing this task, you should understand:
* how to open files in Python
* how to read JSON data from files
* how to write Python data into JSON
* how to handle missing files
* how to persist CLI tool data
