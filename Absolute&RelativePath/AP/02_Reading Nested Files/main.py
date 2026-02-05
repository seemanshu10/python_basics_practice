"""
Reading Nested Files

Use Python to read a text file located within a deeply nested folder structure using a relative path.
Implement error handling to manage missing file cases and provide clear feedback to the user.
"""

try:
    #  open file 
    with open(r"Absolute&RelativePath\AP\02_Reading Nested Files\repo\raw\samples\sample.txt", "r") as nestedFiles:
        file_content = nestedFiles.read()   # reading All content of file 
        print(file_content)

    # file not found error handling 
except FileNotFoundError:
    print("File not found. Please Check path .")

"""
Scene: ForestBattle
Take: 03
Camera: WideAngle
"""