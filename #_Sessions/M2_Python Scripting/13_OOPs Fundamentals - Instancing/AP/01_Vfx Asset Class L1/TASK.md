## 🎯AP. VFX Asset Class L1

### Task Objective
Create a class and use methods with no arguments, single arguments, multiple arguments, and default arguments.

### Instructions
In this task, you are required to:
* Create a class named VFXAsset
* Create at least one object from this class
*  **Expected Usage**
    ```py
    asset1 = VFXAsset()

    asset1.display_info()
    asset1.set_version(2)
    asset1.publish("Aman", "Modeling")
    asset1.export()
    asset1.export("fbx")
    ```
* **Sample Output**
```
Asset Name: DefaultAsset
Asset Type: Prop
Version: 1

Version updated to 2

Asset published by Aman from Modeling department

Asset exported in abc format
Asset exported in fbx format
```
* Inside the class, define the following methods:
* **Method 1: No Arguments**
    * Create a method named display_info
    * This method should not take any arguments other than self
    * It should display the following default values:
        * Asset Name → "DefaultAsset"
        * Asset Type → "Prop"
        * Version → 1
* **Method 2: Single Argument**
    * Create a method named set_version
    * It should take one argument named version
    * It should display:
        * "Version updated to X"
        (where X is the value passed)
* **Method 3: Multiple Arguments**
    * Create a method named publish
    * It should take two arguments:
        * artist_name
        * department
    * It should display:
        * "Asset published by X from Y department"
* **Method 4: Default Argument**
    * Create a method named export
    * It should take one argument named format with a default value "abc"
    * It should display:
        * "Asset exported in X format"
    * If no value is passed, use the default value
    * If a value is passed, use the provided value
* Call all methods using the object to verify the output

