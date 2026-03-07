"""
🎯 AP. Validating Render Metadata

Task Objective
--------------
In this task, you will:
• Use the `assert` keyword to enforce assumptions about render data
• Catch and handle runtime errors using try-except
• Use string methods like `isidentifier()` to validate naming conventions
• Ensure render metadata is valid before processing or publishing

Instructions
------------
• Create a dictionary called `render_metadata` that includes:
  - "resolution" as a list of two integers: [width, height]
  - "frame_range" as a list of two integers: [start_frame, end_frame]
  - "channels" as a list of strings (e.g., ["R", "G", "B"])
  - "shot_name" as a string
• Write a function `validate_metadata(metadata)` that:
  - Uses `assert` to check that:
    • All required keys are present
    • Resolution and frame range lists contain exactly two positive numbers
    • Start frame is less than or equal to end frame
    • "channels" includes "R", "G", and "B"
    • Total frame count is not greater than 2000
  - Uses `try-except` to catch `AssertionError`
    • Prints a clean, user-friendly error message
  - Uses `isidentifier()` to validate the shot name
    • Shot name must not contain spaces or special characters
• Call the function and display a success message if all checks pass


Sample Output
-------------
When all data is valid:
✅ Metadata validation passed for shot_010

When a validation check fails:
❌ Metadata validation failed: Channel B is missing from render output

When the shot name is invalid:
❌ Invalid shot name: shot 010 is not a valid identifier
"""

# Render metadata dictionary
render_metadata = {"resolution": [1920, 1080],"frame_range": [1001, 1200],"channels": ["R", "G", "B"],"shot_name": "Shot001"}

def validate_Metadata(shot_data):
    try:
        # all requred keys defined 
        keys = ['resolution','frame_range','channels','shot_name']
        for key in keys:
            assert key in shot_data,f"Missing required keys: {key}"

        # Resolution validation 
        resolution = shot_data["resolution"]
        print (resolution)
        assert type(resolution) == list and len(resolution) == 2,"Resolution must be a list of two values."
        assert all(type(x) == int and x > 0 for x in resolution),"Resolution values must be positive integers."
        
        # frame range validation 
        frame_range = shot_data["frame_range"]
        assert type(frame_range) == list and len(frame_range) == 2,"Frame Range must be a list of two values Start and End."
        assert all(type(x) == int and x > 0 for x in frame_range),"Frame Range values must be positive integers."

        startFrame , EndFrame = frame_range
        assert startFrame <= EndFrame,"Start Frame must be less than or equal to end frame."

        totalFrames = EndFrame - startFrame+1
        assert totalFrames <=2000,"Total frame count must not exceed 2000"

        # channle Validations assert 
        channels = shot_data["channels"]
        assert "R" in channels,"R channel is missing."
        assert "G" in channels,"G channel is missing."
        assert "B" in channels,"B channel is missing."

        # shot name validations 
        shot_name = shot_data["shot_name"]
        assert type(shot_name) == str ,"Shot name must be string."

        print("Metadata validation successful. Ready for render/publish.")

    except AssertionError as error:
        print(f"Metadata validation failed: {error}")

validate_Metadata(render_metadata)