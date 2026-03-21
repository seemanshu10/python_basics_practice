# print("Hello Everyone")
# print("Running First Python Script using TERMINAL")


import sys

if len(sys.argv) > 1:
    print("Arguments passed to the script:")
    for arg in sys.argv[1:]:
        print(arg)
else:
    print("No arguments passed.")