# Exploring System Information

import os
import time
import ctypes

print("========== SYSTEM INFORMATION ==========\n")

# 1. Print the current working directory
print("Current Working Directory")
print(f"Directory: {os.getcwd()}")

# check the name of the os 
os_name = os.name

if os_name == "nt":
    print("You are using Windows.")
elif os_name == "posix":
    print("You are using a Unix_based system. ")
else:
    print("Unknown Operating System. ")

# check the number of cpus 
print(f"Number of cpus available: ",os.cpu_count())

# Show the current user's login name.
userhome = os.path.expanduser('~')  # returns the current user's home folder  
print("User's home Dir: " + userhome)
# Gives username by splitting path based on OS
print("username: " + os.path.split(userhome)[-1]) # folder path , last folder name userername 

# Environment Variables
# print("\nEnvironment Variables:")
# for key, value in os.environ.items():
#     print(f"   {key} = {value}")

# uptime seconds 
print("===== WINDOWS SYSTEM UPTIME =====\n")

# Get uptime in milliseconds
uptime_ms = ctypes.windll.kernel32.GetTickCount64()

# Convert milliseconds to seconds
uptime_seconds = uptime_ms / 1000.0

# Convert seconds into readable time (HH:MM:SS)
uptime_string = time.strftime("%H:%M:%S", time.gmtime(uptime_seconds))

print("Uptime in seconds:", int(uptime_seconds))
print("Uptime (HH:MM:SS):", uptime_string)

print("\n========== END ==========")