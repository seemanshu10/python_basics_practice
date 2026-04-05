import sys

# Add custom package path at the beginning (highest priority)
sys.path.insert(0, "/path/to/my_custom_package")

import my_custom_package
print("Custom package imported with priority!")