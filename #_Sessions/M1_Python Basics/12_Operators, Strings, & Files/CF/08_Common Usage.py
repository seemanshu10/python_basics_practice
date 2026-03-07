# ----------- Validating Function Preconditions 
def calculate_frame_time(fps):
    assert fps > 0, "FPS must be greater than 0"
    return 1 / fps

# print(calculate_frame_time(24))   # Valid
# print(calculate_frame_time(0))  # Invalid



# ------------  Verifying Pipeline Assumptions 
def process_exr_metadata(metadata):
    assert "width" in metadata, "EXR width missing"
    assert "height" in metadata, "EXR height missing"

    print("Processing EXR:", metadata["width"], "x", metadata["height"])

# process_exr_metadata({"width": 1920, "height": 1080})
# process_exr_metadata({"width": 1920})




# ------------ Catching Logic Errors Early 
def normalize_value(value):
    result = value / 10
    assert 0 <= result <= 1, "Normalized value out of range"
    return result

print(normalize_value(5))
print(normalize_value(50))

