'''
# macOS/Linux
export PYTHONPATH="/path/to/custom/library"

# Windows CMD
set PYTHONPATH=C:\path\to\custom\library

'''



import os
import sys

custom_path = os.environ.get('MY_CUSTOM_PATH')

if custom_path not in sys.path:
    sys.path.append(custom_path)

import my_module
