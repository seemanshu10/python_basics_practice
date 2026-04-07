## 🎯 AP. Render Job Class L2

### Task Objective
Understand how to use __init__, instance attributes, instance methods, and a class-level utility method in a render job system.

### Instructions
In this task you are required to:
* Create a class named RenderJob
* Create an object by passing the following values during creation:
    * job_name
    * renderer
    * status
* Inside the class, use the __init__ method to store these values as instance attributes
* **Expected Usage**
    ```py
    job1 = RenderJob("Shot01_Render", "Arnold", "Pending")
    
    job1.show_job_info()
    job1.set_frame_range("1-120")
    job1.submit_render("Riya", "High")
    job1.output()
    job1.output("png")
    RenderJob.render_note()
    ```
* **Sample Output**
```
Job Name: Shot01_Render
Renderer: Arnold
Status: Pending

Frame range set to 1-120 for Shot01_Render

Shot01_Render submitted by Riya with High priority

Shot01_Render will output in exr format
Shot01_Render will output in png format

Always check frame range before submitting render jobs.
```
* Define the following instance methods:
    * **Method 1: No Extra Argument**
        * Create a method named show_job_info
        * It should only take self
        * It should display:
            * Job Name → (use stored value)
            * Renderer → (use stored value)
            * Status → (use stored value)
    * **Method 2: Single Argument**
        * Create a method named set_frame_range
        * It should take one argument named frame_range
        * It should display:
            * "Frame range set to X for JobName"
    * **Method 3: Multiple Arguments**
        * Create a method named submit_render
        * It should take two arguments:
            * artist_name
            * priority
        * It should display:
            * "JobName submitted by X with Y priority"
    * **Method 4: Default Argument**
        * Create a method named output
        * It should take one argument named format with default value "exr"
        * It should display:
            * "JobName will output in X format"
            * If no value is passed, use the default value
            * If a value is passed, use the provided value
* Define a class-level Static method:
    * **Static Method**
        * Create a method named render_note
        * It should not use self
        * It should display:
        * "Always check frame range before submitting render jobs."
        * Call this method using the class name
* Call all methods to verify the output