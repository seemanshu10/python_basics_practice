import sys

# -------- Using Direct Append
sys.path.append(r"C:\Users\pralhad\Desktop\dev")

from my_package import module1, module2, module3, module4

print(module1.greet())             # Hello from Module 1!
print(module1.add(5, 3))           # 8

print(module2.multiply(4, 2))      # 8
print(module2.divide(8, 2))        # 4.0

print(module3.status_check())      # Status: Active
print(module4.get_version())       # Version: 1.0.0






#  ----------- Using os.path.abspath())
import os

package_path = os.path.abspath("../dev")  

print(package_path)
# Output: C:\Users\pralhad\Desktop\dev

if package_path not in sys.path:
    sys.path.append(package_path)


from my_package import module1, module2, module3, module4

print(module1.greet())             # Hello from Module 1!
print(module1.add(5, 3))           # 8

print(module2.multiply(4, 2))      # 8
print(module2.divide(8, 2))        # 4.0

print(module3.status_check())      # Status: Active
print(module4.get_version())       # Version: 1.0.0


