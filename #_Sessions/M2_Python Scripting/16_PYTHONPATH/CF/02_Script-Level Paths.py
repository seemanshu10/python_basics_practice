import sys
import os

custom_path = r"C:\Users\pralhad\Desktop\dev"

sys.path.append(custom_path)

for path in sys.path:
    print(path)


import my_package


# Output:
# c:\Users\pralhad\Desktop\dev\tools
# C:\Users\pralhad\AppData\Local\Programs\Python\Python39\python39.zip
# C:\Users\pralhad\AppData\Local\Programs\Python\Python39\DLLs
# C:\Users\pralhad\AppData\Local\Programs\Python\Python39\lib
# C:\Users\pralhad\AppData\Local\Programs\Python\Python39
# C:\Users\pralhad\AppData\Roaming\Python\Python39\site-packages
# C:\Users\pralhad\AppData\Local\Programs\Python\Python39\lib\site-packages
# C:\Users\pralhad\AppData\Local\Programs\Python\Python39\lib\site-packages\win32
# C:\Users\pralhad\AppData\Local\Programs\Python\Python39\lib\site-packages\win32\lib
# C:\Users\pralhad\AppData\Local\Programs\Python\Python39\lib\site-packages\Pythonwin
# C:\Users\pralhad\Desktop\dev
# Initializing my_package