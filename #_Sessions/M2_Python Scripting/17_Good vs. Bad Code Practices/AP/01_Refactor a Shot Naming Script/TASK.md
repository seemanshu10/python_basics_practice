## 🎯 AP. Refactor a Shot Naming Script

### Task Objective

Your task is to refactor an unstructured Python script that generates VFX shot names. You will improve code readability, modularity, and error handling, and follow PEP 8 standards throughout.


### Instructions

Your refactored script must:

* Accept the following user inputs:
  * `sequence` (e.g., SQ001)
  * `shot` (e.g., SH010)
  * `version` (e.g., V003)
* Generate a shot name in the format: 
  `SEQUENCE_SHOT_VERSION` → example: `SQ001_SH010_V003`  
* Handle missing or invalid inputs gracefully.
* Follow Python best practices:
  * Use functions to separate logic.
  * Add docstrings to all functions.
  * Apply PEP 8 formatting (consistent indentation, spacing, naming).
  * Use meaningful variable names.


### Original (Poor) Code

```python
def main():
    s = input("Enter sequence: ")
    n = input("Enter shot: ")
    v = input("Enter version: ")
    if s and n and v:
        print(s + "_" + n + "_" + v)
    else:
        print("Invalid input")
main()
```


### Expected Output

```
Enter sequence (e.g., SQ001): SQ005
Enter shot number (e.g., SH010): SH020
Enter version (e.g., V003): V001
Generated Shot Name: SQ005_SH020_V001
```
