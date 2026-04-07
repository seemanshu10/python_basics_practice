## 🎯 AP. Render Job Class L1

### Task Objective
create a class and implement methods with no arguments, single arguments, multiple arguments, and default arguments in a render job system.

### Instructions

In this task, you will build a simple render job tool using a class.
You are required to:
* Create a class named RenderJob
* Create at least one object from this class
* **Expected Usage**
    ```py
    job1 = RenderJob()

    job1.show_job_info()
    job1.set_frame_range("1-120")
    job1.submit_render("Riya", "High")

    job1.output()
    job1.output("png")
    ```
* **Sample Output**
```
Job Name: TestRender
Renderer: Arnold
Status: Pending

Frame range set to 1-120

Render submitted by Riya with High priority.

Render output will be saved as exr format.
Render output will be saved as png format.
```
* Inside the class, define the following methods:
* **Method 1: No Arguments**
    * Create a method named show_job_info
    * This method should not take any arguments other than self
    * It should display the following default values:
        * Job Name → "TestRender"
        * Renderer → "Arnold"
        * Status → "Pending"
* **Method 2: Single Argument**
    * Create a method named set_frame_range
    * It should take one argument named frame_range
    * It should display:
        * "Frame range set to X"
        * Example value: "1-120"
* **Method 3: Multiple Arguments**
    * Create a method named submit_render
    * It should take two arguments:
        * artist_name
        * priority
    * It should display:
        * "Render submitted by X with Y priority"
* **Method 4: Default Argument**
    * Create a method named output
    * It should take one argument named format with default value "exr"
    * It should display:
        * "Render output will be saved as X format"
    * If no value is passed, use the default value
    * If a value is passed, use the provided value
* Call all methods using the object to verify the output
