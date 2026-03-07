# ------------ File does not exist
with open("report.txt", "x") as f:
    f.write("This is my first report.")

# Process finished with exit code 0



# ------------ File already exists
# with open("report.txt", "x") as f:
#     f.write("Trying to overwrite...")