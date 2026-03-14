## 🎯 AP. Refactor Shot Metadata Script

### Task Objective

In this task, you will:
* Analyze a Python script that reads and updates shot metadata stored in JSON files.
* Improve code readability, structure, and naming consistency.
* Improve file handling practices.
* Add meaningful documentation and comments.
* Refactor the script while keeping the program behavior the same.

### Instructions

* Below is a small project that stores shot metadata as JSON files inside a directory.
* The provided Python script scans the directory, reads each JSON file, calculates the frame count for the shot, updates the JSON data, and writes the result back to the file.
* The script works, but it contains several code quality problems
* Your task is to refactor the script to improve its code quality while keeping the functionality the same.
* Script was given in **main.py** file.
* update refactor code in **refactor.py** file
  
### Project structure:

```
project/
│
├── shots/
│   ├── shot01.json
│   ├── shot02.json
│   └── shot03.json
│
└── process_shots.py
```

### Sample Output

```
Processed shot01.json | Frame Count: 50
Processed shot02.json | Frame Count: 35
Processed shot03.json | Frame Count: 100
```

#### Updated JSON file example (shot01.json):

```
{
  "shot_name": "shot01",
  "frame_start": 1001,
  "frame_end": 1050,
  "frame_count": 50
}
```
