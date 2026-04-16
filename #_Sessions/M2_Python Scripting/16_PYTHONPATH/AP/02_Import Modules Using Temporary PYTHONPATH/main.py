import sys

model_path = r"C:\Users\ANT-pc\Desktop\Cohort-EC1\#_Practice\Seemanshu\M2_Python Scripting\16_PYTHONPATH\AP\01_Import Modules from Multiple Drives\C\tools_a"

render_path = r"C:\Users\ANT-pc\Desktop\Cohort-EC1\#_Practice\Seemanshu\M2_Python Scripting\16_PYTHONPATH\AP\01_Import Modules from Multiple Drives\D\tools_b"

# print(sys.path)
# print()
sys.path.append(model_path)
sys.path.append(render_path)

# print(sys.path)

import model_tools
import render_tools

print("Both modules imported successfully")