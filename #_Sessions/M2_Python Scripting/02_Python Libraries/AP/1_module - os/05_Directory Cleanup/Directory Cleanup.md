## 🎯 AP. Directory Cleanup

### Task Objective

In this task, you will:

* Traverse a directory and list all files.
* Identify and delete files based on their extension.
* Print logs of deleted files and confirm which files remain.
* Practice automating cleanup processes using the `os` module.

### Instructions

* In the directory named `cleanup_test`.
* Inside `cleanup_test`, add a mix of files with `.txt`, `.log`, and `.jpg` extensions.
* Write a script to:
  * List all files inside the directory.
  * Delete only the `.log` files.
  * Print the names of the deleted `.log` files.
  * List the files that remain after deletion.

---

### Sample Output

Create a Directory structure is as follows:

```
cleanup_test/
├── file1.txt
├── file2.log
├── image1.jpg
├── file3.log
└── file4.txt
```

**The output should display:**

```
Deleted files:
file2.log
file3.log
Remaining files:
file1.txt
image1.jpg
file4.txt
```
