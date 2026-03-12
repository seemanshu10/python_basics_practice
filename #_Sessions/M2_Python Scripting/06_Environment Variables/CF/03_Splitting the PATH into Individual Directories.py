import os

path = os.getenv("PATH")
directories = path.split(";")  # Split by semicolon on Windows

for d in directories:
    print(d)