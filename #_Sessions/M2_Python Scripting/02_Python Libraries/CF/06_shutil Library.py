# ----------- Copying a File
import shutil

# shutil.copy("original.txt", "backup/")
# # print("File copied.")



# # # ---------- Copying a File with Metadata
# shutil.copy2("my_file.txt", "backup/")
# print("File copied with metadata.")




# # ---------- Moving a File
# shutil.move("draft_version.mov", "backup/")
# print("File moved.")




# ---------- Deleting a Folder & All Its Contents
import os

# path = r"C:\Users\pralhad\Desktop\CF\backup"

# if os.path.exists(path):    
#     shutil.rmtree(path)
#     print("Temporary cache deleted.")



# ------------- Archiving a Folder (Creating a .zip)
# shutil.make_archive("backup_assets", "zip", "assets")
# print("Archive created: backup_assets.zip")




# ---------- Checking Disk Usage
# import shutil

usage = shutil.disk_usage("C:/")
print(usage)

print(f"Total: {usage.total}")
print(f"Used: {usage.used}")
print(f"Free: {usage.free}")
print()


# Convert bytes to GB
total = usage.total / (1024 ** 3)
used = usage.used / (1024 ** 3)
free = usage.free / (1024 ** 3)


print(f"Total: {total:.2f} GB")
print(f"Used: {used:.2f} GB")
print(f"Free: {free:.2f} GB")
