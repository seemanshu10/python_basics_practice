# ----------- Using wildcard import *
from my_package import *

greet()     
add(5, 3)   




# ----------- Using __all__ -----------
import sys
import os

package_path = os.path.abspath("../dev")  

if package_path not in sys.path:
    sys.path.append(package_path)

from my_package import *  

print(greet())   
print(add(3, 4))  





# ----------- Importing All Public Functions Using __all__ -----------
import sys
import os

package_path = os.path.abspath("../dev")  

if package_path not in sys.path:
    sys.path.append(package_path)

from my_package import *

print(greet())             # Hello from Module 1!
print(add(2, 3))           # 5
print(multiply(4, 5))      # 20
print(divide(10, 2))       # 5.0
print(status_check())      # Status: Active
print(get_version())       # Version: 1.0.0