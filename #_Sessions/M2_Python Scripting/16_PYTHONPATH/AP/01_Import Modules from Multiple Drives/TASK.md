## 🎯 AP. Import Modules from Multiple Drives

### Task Objective
Practice setting a system-level PYTHONPATH variable so Python can import two custom modules stored in different locations.

### Instructions
* Use the two custom modules given below.
* Keep both module folders in different locations.
* Create a system-level PYTHONPATH variable.
* Add both module folder paths inside that variable.
* Create a main.py file in a completely different location.
* In main.py, importing both modules.
* Run the script and check whether both modules import correctly without any error.

#### Folder Structure
```
C:\
└── tools_a
    └── model_tools.py

D:\
└── tools_b
    └── render_tools.py
```

### File Content
**C:\tools_a\model_tools.py**
```python
print("model_tools imported")
```
**D:\tools_b\render_tools.py**
```python
print("render_tools imported")
```

### Sample Output
```
model_tools imported
render_tools imported
Both modules imported successfully
```
