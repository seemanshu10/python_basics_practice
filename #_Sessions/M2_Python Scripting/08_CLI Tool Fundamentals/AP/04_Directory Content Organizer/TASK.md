## 🎯 AP. Directory Content Organizer

### Task Objective

In this task, you will:

* Write a script that organizes files in a directory by file extension.
* Create subdirectories named after each file extension.
* Move each file into the correct subdirectory based on its extension.
* Skip files that are already organized.
* Show clear messages for missing or empty directories.

### Instructions

* Create a script named `organize_directory.py`.
* The script should accept **one command line argument**: the path to the target directory.
* Check if the directory exists.
* List all files in that directory.
* For each file:
  * Check its extension.
  * Create a subdirectory (e.g., `jpg`, `txt`, etc.) if it doesn’t exist.
  * Move the file into the correct subdirectory.
  * Skip files that are already in their correct location.
* Print messages showing which files were **moved** or **skipped**.
* Print an error if the directory **does not exist** or **contains no files**.

---

### Sample Output

```
# Organizing files
$ python organize_directory.py /path/to/directory
Moved 'photo.jpg' to 'jpg/photo.jpg'
Moved 'notes.txt' to 'txt/notes.txt'
Moved 'slide.pptx' to 'pptx/slide.pptx'
```

```
# Skipping files already organized
Skipped 'image.jpg' (already in 'jpg/image.jpg')
```

```
# Directory doesn't exist
$ python organize_directory.py /nonexistent/dir
Error: Directory '/nonexistent/dir' does not exist.
```

```
# Directory is empty
$ python organize_directory.py /empty/dir
No files found in the directory '/empty/dir'.
```
