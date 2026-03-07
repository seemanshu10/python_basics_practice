## 🎯 AP. Reading Nested Files

### Task Objective:

In this task, you will:
* Use Python to read a text file located within a deeply nested folder structure using a relative path.
* Implement error handling to manage missing file cases and provide clear feedback to the user.

### Instructions:

Set up the following folder structure inside your project:

```
repo/
├── data/
│   └── raw/
│       └── samples/
│           └── sample.txt
└── main.py
```

* In the `repo/` folder, create a Python script named `main.py`.
* Inside `repo/data/raw/samples/`, create a file named `sample.txt` and add a few lines of sample text, such as:
```
Scene: ForestBattle
Take: 03
Camera: WideAngle
```
In `main.py`:
* Use the relative path `data/raw/samples/sample.txt` to access the file.
* Open the file and print its contents to the terminal.
* If the file is missing or not found, catch the error and print:

```
File not found. Please check the path and try again.
```

### Sample Output:

```
Scene: ForestBattle
Take: 03
Camera: WideAngle
```

If the file is missing or moved:

```
File not found. Please check the path and try again.
```
