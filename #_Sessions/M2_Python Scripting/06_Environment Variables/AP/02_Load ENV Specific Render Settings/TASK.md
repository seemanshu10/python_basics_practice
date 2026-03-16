## 🎯 AP. Load Environment-Specific Render Settings

## Task Objective

In this task, you will:
* Create a custom system-level environment variable on Windows
* Use that environment variable to detect the current render environment
* Automatically load the correct render settings JSON file
* Read and print the actual JSON data
* Handle invalid or missing environment values with:
  * A default fallback
  * A clear error message

This simulates how production pipelines switch between dev, test, and production environments.

### Files Provided to You

You will be given the following three JSON files:
* devsettings.json
* testsettings.json
* prodsettings.json

Each file contains different render settings data.

### Instructions

#### Create a System-Level Environment Variable (Windows)

You must first create a custom system environment variable with:

* **Variable name** : `RENDER_ENV`
* **Values Allowed** : `dev`, `test`, `prod`

**How to Set It (Windows)**

* Open Start Menu
* Search for Environment Variables
* Click "Edit the system environment variables"
* Click "Environment Variables…"
* Under System Variables, click New
* Enter:
  * **Variable Name**: `RENDER_ENV`
  * **Variable Value**: `dev` (or `test`, or `prod`)
* Click OK on all windows
* Restart your terminal / VS Code

#### Create Script

You must create a Python script named: `load_render_settings.py`

Your script must:

* Read the `RENDER_ENV` system environment variable
* Based on its value:
  * `dev` → load `devsettings.json`
  * `test` → load `testsettings.json`
  * `prod` → load `prodsettings.json`
* Open the selected JSON file
* Print the contents of the JSON file

Handle these cases properly:

* ✅ **Valid Environment**:

  * Load and print the JSON data.

* ⚠️ **If `RENDER_ENV` is missing**:

  * Fall back to `dev`
  * Print a warning message

* ❌ **If `RENDER_ENV` has an invalid value** (example: `"staging"`):

  * Do NOT load any file
  * Print a clear error message

### Expected Behavior

| RENDER_ENV Value | Expected Output                       |
| ---------------- | ------------------------------------- |
| dev              | Load and print devsettings.json       |
| test             | Load and print testsettings.json      |
| prod             | Load and print prodsettings.json      |
| (not set)        | Warning + default to devsettings.json |
| staging          | Error message only                    |

### Advantage of These Files

These JSON files clearly demonstrate real pipeline logic:

| Feature       | Dev    | Test   | Prod    |
| ------------- | ------ | ------ | ------- |
| Resolution    | 720p   | 1080p  | 4K      |
| Samples       | 32     | 96     | 256     |
| Denoiser      | ✅      | ✅      | ❌       |
| Motion Blur   | ❌      | ✅      | ✅       |
| DOF           | ❌      | ❌      | ✅       |
| Output        | JPG    | PNG    | EXR     |
| Render Engine | GPU    | GPU    | CPU     |
| Max Time      | 10 min | 45 min | 240 min |
