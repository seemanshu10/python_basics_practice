"""
Task Objective
--------------
In this task, you will:
• Handle multiple types of exceptions while reading and validating scene data
• Use try-except-else-finally to separate error-handling, success paths,
  and cleanup code
• Raise custom exceptions using `raise` when invalid input is detected

Instructions
------------
Simulate a tool that reads a scene file name and frame range from the user.
• Prompt the user to enter:
  - A scene file name (must end with `.vscene`)
  - A start frame
  - An end frame
• Implement the following validations:
  - Raise a ValueError if the file name does not end with `.vscene`
  - Raise a ValueError if the start frame is greater than the end frame
• Handle the following exceptions:
  - ValueError for input validation errors
  - FileNotFoundError when attempting to open the scene file
  - Generic Exception for any unexpected errors
• Use:
  - An `else` block to simulate successful file processing
    (e.g., print a success message)
  - A `finally` block to simulate cleanup actions,
    such as closing the file if it was opened
"""

def toolsValidation():

    layoutFile = None   # define before try so finally can access it

    try:
        # user inputs validation 
        file_name = input("Enter scene file name: ")

        # Validate extension
        if not file_name.endswith(".vscene"):
            raise ValueError("Invalid file type. Must end with '.vscene'.")

        user_start = int(input("Enter start frame: "))
        user_end = int(input("Enter end frame: "))

        # start frame value compare 
        if user_start > user_end:
            raise ValueError("Start frame cannot be greater than end frame.")
        
        # Build full path using string concatenation
        folder_path = "Operators, Strings, & Files/"
        file_path = folder_path + file_name
        
        # open the file
        layoutFile = open(file_path, "r")
        content = layoutFile.read()

        # Extract frame_range from file
        scene_start = None
        scene_end = None

        for line in content.splitlines():
            if line.strip().startswith("frame_range"):
                parts = line.split("=")
                value = parts[1].strip()
                frames = value.split("-")
                scene_start = int(frames[0])
                scene_end = int(frames[1])
                break

        if scene_start is None:
            raise ValueError("Scene file missing frame_range.")

        if scene_start > scene_end:
            raise ValueError("Invalid frame_range inside scene file.")

        if user_start < scene_start or user_end > scene_end:
            raise ValueError("Requested frame range is outside scene frame range.")
    
    # raising value error 
    except ValueError as ve:
        print(f"Validation Error: {ve}")

    # handling file not found error 
    except FileNotFoundError:
        print("Error: Scene file not found.")

    # handling unexpected errors
    except Exception as e:
        print("Unexpected error:", e)

    else:
        print("Scene file validated successfully.")
        print(f"Processing frames {user_start} to {user_end}...")

    finally:
        if layoutFile:
            layoutFile.close()
            print("Scene file closed.")
        print("Cleanup complete.")


toolsValidation()