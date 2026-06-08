## 🎯 AP. Preview or Delete Temporary Files

### Task Objective

In this task, you will:
* Build a CLI script that scans a directory for temporary files.
* Accept a directory path as a positional argument.
* Implement flags to preview or delete .tmp files.
* Add a --help flag to display usage instructions.
* Validate the directory before performing any operation.

### Instructions

* Create a Python command-line script that manages temporary files inside a directory.
* The script must accept one positional argument: A directory path.
* The script must also support the following flags:
  * --preview to list all .tmp files found in the directory.
  * --delete to remove all .tmp files from the directory.
  * --help to display usage instructions.
* The program should:
  * Display a help message when the help flag is used.
  * Validate that the directory exists before scanning it.
  * Search the directory and identify files ending with .tmp.
  * List the files when preview mode is selected.
  * Remove the files when delete mode is selected.
  * If the flag is invalid or arguments are missing, the program should display an error message.

### Folder Structure

```
temp_project/
│
├── images/
│   ├── render_preview.tmp
│   ├── lighting_test.tmp
│
├── cache/
│   ├── fluid_cache.tmp
│   ├── sim_data.tmp
│
├── misc/
│   ├── log.tmp
│   ├── debug.tmp
│
└── notes.txt
```
* Your script should detect all .tmp files inside every folder.

### Sample Output

**Case 1 — Help Message**

Command:

```
python script.py --help
```

Output:

```
Usage: python script.py <directory_path> [--delete | --preview]

Options:
  --delete   Delete all .tmp files in the specified directory.
  --preview  List all .tmp files without deleting them.
  --help     Show this help message and exit.

Description:
  This script simulates file deletion. It either previews the files or deletes
  temporary (.tmp) files in the specified directory based on the provided flag.

Examples:
  python script.py ./test_folder --preview
  python script.py ./test_folder --delete
```

**Case 2 — Preview Temporary Files**

Command:

```
python script.py ./test_folder --preview
```

Output:

```
Temporary files:
cache.tmp
render_output.tmp
temp_data.tmp
```

**Case 3 — Delete Temporary Files**

Command:

```
python script.py ./test_folder --delete
```

Output:

```
Temporary files deleted.
```

**Case 4 — Invalid Directory**

Command:

```
python script.py ./missing_folder --preview
```

Output:

```
Error: Directory not found.
```

