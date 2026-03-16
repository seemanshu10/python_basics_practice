# Environment Variable Management

import os 

#  Read and print an existing environment variable (e.g., `PATH`).

path_value = os.environ.get("PATH")
print("Existing Path: ",path_value)

# Set a new environment variable named `MY_VAR` with a value of `"HelloWorld"`.
os.environ["MY_VAR"] = "HelloWorld"
print("MY_VAR Set to: ", os.environ["MY_VAR"])

#Verify and print the value of the newly set environment variable.

print("MY_VAR value:", os.environ.get("MY_VAR"))

# the value of `MY_VAR` to `"HelloPython"`.
os.environ["MY_VAR"] = "HelloPython"
print("Updated MY_VAR to: ", os.environ["MY_VAR"])

# Verify and print the updated value of `MY_VAR`.
print("Updated MY_VAR value:", os.environ.get("MY_VAR"))

# Delete the environment variable `MY_VAR` 
del os.environ["MY_VAR"]

# Verify and print the deletion status of `MY_VAR`.
if "MY_VAR" not in os.environ:
    print("MY_VAR deleted successfully.")
else:
    print("MY_VAR still exists.")
print("Updated MY_VAR value:", os.environ.get("MY_VAR"))