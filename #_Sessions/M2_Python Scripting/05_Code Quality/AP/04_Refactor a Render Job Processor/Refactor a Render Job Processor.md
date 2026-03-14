## 🎯 AP. Refactor a Render Job Processor

### Task Objective

In this task, you will:
* Analyze a Python script that processes render job JSON files in a directory.
* Improve the readability and maintainability of the code.
* Break down a large block of logic into smaller reusable functions.
* Improve variable naming, formatting, and documentation.
* Improve file handling and error messages

### Instructions
* Your task is to refactor the script to improve its code quality while keeping the functionality the same.
* A render pipeline stores job information as JSON files inside a directory.
* Each file contains information about a render job, including:
  * job name
  * start frame
  * end frame
* render time per frame
* The script scans the directory, reads each JSON file, calculates:
  * frame count
  * total render time
* It then updates the JSON file with these values.
* The script works, but it contains multiple code quality issues
* Script was given in **main.py** file.
* update refactor code in **refactor.py** file

### Project structure:

```
project/
│
├── jobs/
│   ├── shot01.json
│   ├── shot02.json
│   └── shot03.json
│
└── process_jobs.py
```

### Sample Output

```

Processed shot01.json | Frames: 50 | Total Render Time: 100
Processed shot02.json | Frames: 35 | Total Render Time: 105
Processed shot03.json | Frames: 100 | Total Render Time: 200
Total Render Time Across All Jobs: 405

```

### Updated JSON example (shot01.json):

```
{
  "shot": "shot01",
  "frame_start": 1001,
  "frame_end": 1050,
  "render_time_per_frame": 2,
  "frame_count": 50,
  "total_render_time": 100
}
```
