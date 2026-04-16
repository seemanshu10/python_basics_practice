import os
import sys

# Get the current script's directory (i.e., tools/)
script_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one level to DEV/ (the parent of tools/)
parent_dir = os.path.abspath(os.path.join(script_dir, ".."))

# Add the DEV/ directory to sys.path (so Python can find my_package/)
if parent_dir not in sys.path:
    sys.path.append(parent_dir)

# Now import the package
import my_package

print("Imported my_package successfully!")

# Initializing my_package
# Imported my_package successfully!