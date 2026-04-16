import sys 
import os

custom_path = os.path.join(os.getcwd(), "custom_modules")
sys.path.append(custom_path)
print(sys.path)

import my_module
my_module.greet()