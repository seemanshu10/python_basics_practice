## 🎯 AP. Directory Traversal and File Information

### Task Objective

In this task, you will:

* Traverse through a directory and its subdirectories using the `os` module.
* Retrieve and display file sizes for each file found during traversal.
* Check and display file-level permissions (read, write, execute).
* Practice working with recursive directory structures using `os.walk()`.

### Instructions

* Create a folder named `traversal_test` and add a few subfolders and text files inside.
* Write a script that walks through the entire `traversal_test` directory structure.
* For every file found:

  * Print its name and size in bytes.
  * Check if the file is readable, writable, and executable, and print the results.
* Organize your output clearly to reflect the directory structure.

### Sample Output

```
Directory: traversal_test
  Subdirectory: subdir1
    File: file1.txt, Size: 100 bytes, Read: True, Write: True, Execute: False
  Subdirectory: subdir2
    File: file2.txt, Size: 200 bytes, Read: True, Write: True, Execute: False
  File: file3.txt, Size: 300 bytes, Read: True, Write: True, Execute: False
```
