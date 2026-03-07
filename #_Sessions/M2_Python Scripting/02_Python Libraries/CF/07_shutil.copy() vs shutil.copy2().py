#  ------------ Checking the Last Modified Time of a File

import shutil
import os

# modified_time = os.path.getmtime("original.txt")

# print("Last modified time:", modified_time)
# Last modified time: 1772118687.3988593



# ----------- Copy Using copy() and copy2()

# import os

shutil.copy("original.txt", "copy_file.txt")
shutil.copy2("original.txt", "copy2_file.txt")


# # Read Metadata from All Files
original_time = os.path.getmtime("original.txt")
copy_time = os.path.getmtime("copy_file.txt")
copy2_time = os.path.getmtime("copy2_file.txt")

print("Original:", original_time)
print("copy():  ", copy_time)
print("copy2(): ", copy2_time)