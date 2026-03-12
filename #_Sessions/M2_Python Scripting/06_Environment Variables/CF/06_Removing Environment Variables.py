# ----------- Temporarily Remove (Session Only)
import os

# os.environ.pop('MAYA_PLUG_IN_PATH', None)

# print(os.environ["MYTOOLS"])
# os.environ.pop('MYTOOLS')

# # os.environ.pop("")

# print(os.environ.get("MYTOOLS"))

# MAYA_PLUG_IN_PATH has been removed (temporarily).




# # ------------- Permanently Remove on Windows

import winreg

with winreg.OpenKey(winreg.HKEY_CURRENT_USER, r'Environment', 0, winreg.KEY_SET_VALUE) as reg_key:
    winreg.DeleteValue(reg_key, 'MYTOOLS')

print("MYTOOLS removed from system environment variables.")

# MAYA_PLUG_IN_PATH removed from system environment variables.