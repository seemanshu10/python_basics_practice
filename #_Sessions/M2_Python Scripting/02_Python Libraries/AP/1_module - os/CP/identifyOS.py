import os 

# check the name of the os 

os_name = os.name

if os_name == "nt":
    print("You are using Windows.")
elif os_name == "posix":
    print("You are using a Unix_based system. ")
else:
    print("Unknown Operating System. ")