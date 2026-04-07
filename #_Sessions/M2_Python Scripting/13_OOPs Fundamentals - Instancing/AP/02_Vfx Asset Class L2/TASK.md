## 🎯 AP. VFX Asset Class L2

### Task Objective
use __init__, instance attributes, instance methods, and a class-level Static method in a VFX asset class.

### Instructions
In this task, you are required to:
* Create a class named VFXAsset
* Create an object by passing the following values during creation:
    * name
    * asset_type
    * version
* Inside the class, use the __init__ method to store these values as instance attributes
* **Expected Usage**
    ```py
    asset1 = VFXAsset("Dragon", "Character", 1)

    asset1.display_info()
    asset1.set_version(2)
    asset1.publish("Aman", "Modeling")
    asset1.export()
    asset1.export("fbx")
    VFXAsset.pipeline_note()
    ```
* **Sample Output**
```
Asset Name: Dragon
Asset Type: Character
Version: 1

Dragon version updated to 2

Dragon published by Aman from Modeling department.

Dragon exported in abc format.
Dragon exported in fbx format.

All VFX assets must follow studio naming conventions.
```
* Define the following instance methods:
    * **Method 1: No Extra Argument**
        * Create a method named display_info
        * It should only take self
        * It should display:
            * Asset Name → (use stored value)
            * Asset Type → (use stored value)
            * Version → (use stored value)
    * **Method 2: Single Argument**
        * Create a method named set_version
        * It should take one argument named new_version
        * It should update the stored version
        * It should display:
            * "AssetName version updated to X"
    * **Method 3: Multiple Arguments**
        * Create a method named publish
        * It should take two arguments:
            * artist_name
            * department
        * It should display:
            * "AssetName published by X from Y department"
    * **Method 4: Default Argument**
        * Create a method named export
        * It should take one argument named format with default value "abc"
        * It should display:
            * "AssetName exported in X format"
            * If no value is passed, use the default value
            * If a value is passed, use the provided value
* Define a class-level Static method:
    * **Static Method**
        * Create a method named pipeline_note
        * It should not use self
        * It should display:
            * "All VFX assets must follow studio naming conventions."
        * Call this method using the class name
* Call all methods to verify the output
