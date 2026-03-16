# Environment Variable Management

import os

path_value = os.getenv("PATH")
print("Existing Path: ",path_value)

print("\nDirectories in PATH:")

path_dirs = path_value.split(";")

for i, path in enumerate(path_dirs):
    print(f"{i}. {path}")
