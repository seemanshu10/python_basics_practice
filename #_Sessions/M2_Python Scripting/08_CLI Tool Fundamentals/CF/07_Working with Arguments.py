#  --------------- Checking All Passed Arguments
import sys


first_name = sys.argv[1]
last_name = sys.argv[2]
age = sys.argv[3]

print(sys.argv)



# ----------- Accessing Individual Arguments

print("Script name:", sys.argv[0])   # script.py
print("First argument:", sys.argv[1]) # apple
print("Second argument:", sys.argv[2]) # banana



# -------------- Checking the Type of sys.argv
print(type(sys.argv))