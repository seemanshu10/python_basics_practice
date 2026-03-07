## 🎯 AP. Reading VFX Config Files

### Task Objective:

In this task, you will:
* Build a Python script that reads from two separate text files one using a relative path and one using an absolute path.
* Implement basic file error handling to gracefully report missing or inaccessible files.

### Instructions:

Set up your project with the following folder structure:
```
project/
├── file_display.py
└── assets/
    └── asset_info.txt
```
* In the root of your project (`project/`), create a Python script named `file_display.py`.
* Inside the project, create a subfolder called `assets/`, and place a text file named `asset_info.txt` in it.
* Add some sample metadata to the file, such as:

```
Asset: Dragon_Rig
Version: 1.2
```
* On your local system, create or locate another text file named `system_config.txt` outside your project folder. This simulates a shared configuration file. Example paths:
    * On Windows: `C:\VFX\Config\system_config.txt`
    * On macOS/Linux: `/home/user/VFX/Config/system_config.txt`
* Add example content such as:
```
RenderEngine=Arnold
FrameRange=1001-1100
Resolution=1920x1080
```

In your `file_display.py` script:
* Build a relative path to read from `assets/asset_info.txt`.
* Use a hard-coded absolute path to read from `system_config.txt`.
* Implement a function to read and display each file's content.
* If a file is not found, catch the error and print:

```
File not found. Please check the path and try again.
```

### Sample Output:

```
Reading asset_info.txt using relative path:
Asset: Dragon_Rig
Version: 1.2

Reading system_config.txt using absolute path:
RenderEngine=Arnold
FrameRange=1001-1100
Resolution=1920x1080
```

If a file is missing or cannot be found:

```
Reading asset_info.txt using relative path:
File not found. Please check the path: assets\asset_info.txt

Reading system_config.txt using absolute path:
File not found. Please check the path: C:\VFX\Config\system_config.txt
```
