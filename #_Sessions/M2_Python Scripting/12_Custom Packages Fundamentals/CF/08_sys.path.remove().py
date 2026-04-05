import sys
import os

# Add the custom path temporarily
custom_path = r"C:\Users\pralhad\Desktop\dev"

if custom_path not in sys.path:
    sys.path.insert(0, custom_path)

print(custom_path in sys.path)  # True


import my_package

print("Custom package imported")

# Now remove the custom path
sys.path.remove(custom_path)

# Check it's no longer there
print(custom_path in sys.path)  # Output: False