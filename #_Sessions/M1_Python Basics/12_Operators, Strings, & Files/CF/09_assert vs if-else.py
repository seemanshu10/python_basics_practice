# ------- Using if-else 
def validate_exr_channels(channels):
    if "R" not in channels:
        print("R channel missing")
        return
    if "G" not in channels:
        print("G channel missing")
        return
    if "B" not in channels:
        print("B channel missing")
        return

# print("EXR channel validation passed.")

# # validate_exr_channels({"R": 1.0, "G": 1.0, "B": 1.0})
# validate_exr_channels({"R": 1.0, "B": 1.0})

# Output:
# EXR channel validation passed.
# G channel missing





# -------- Using assert 
def validate_exr_channels_assert(channels):
    assert "R" in channels, "R channel missing"
    assert "G" in channels, "G channel missing"
    assert "B" in channels, "B channel missing"

print("EXR channel validation passed.")

# validate_exr_channels_assert({"R": 1.0, "G": 1.0, "B": 1.0}) 
validate_exr_channels_assert({"R": 1.0, "B": 1.0})

# Output:
# EXR channel validation passed.
# AssertionError: G channel missing

