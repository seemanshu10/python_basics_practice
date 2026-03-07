import os  

mac_path = "/Users/pralhad/Desktop/Work/tst/r.md"  

cross_platform_path = mac_path.replace("/", os.sep)  

print("Converted path:", cross_platform_path)