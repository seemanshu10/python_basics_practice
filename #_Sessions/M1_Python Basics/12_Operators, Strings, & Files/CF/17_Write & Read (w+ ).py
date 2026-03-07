# with open("demo_w+.txt", "w+") as f:
#     f.write("First Content")
#     f.seek(0)
#     print("Reading:", f.read())

# # Reading: First Content






# # --------------- Append & Read (a+) --------------
# with open("demo_a+.txt", "w") as f:
#     f.write("Line 1\n")

# Open with a+
with open("demo_a+.txt", "a+") as f:
    f.write("Line 2")     
    f.seek(3)               
    print("Reading:\n", f.read())


# Reading:
#  Line 1
# Line 2

