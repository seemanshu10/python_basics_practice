# Create file first
with open("demo_r+.txt", "w") as f:
    f.write("Python")


# Open with r+
with open("demo_r+.txt", "r+") as f:
    f.seek(4)                   
    f.write("Hello")      
    f.seek(0)
    f.write("hey there !")


    
    # f.seek(0)
    # print("After:", f.read()) 


# Before: Python
# After: Hellon