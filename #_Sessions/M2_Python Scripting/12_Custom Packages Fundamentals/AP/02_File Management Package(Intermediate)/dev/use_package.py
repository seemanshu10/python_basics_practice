import sys, os

# dynamic path take sys. path 


package_path = os.path.dirname(os.path.abspath(__file__))

if package_path not in sys.path:
    sys.path.append(package_path)

sys.path.append(package_path)

import file_manager

# List files
file_manager.list_files(package_path)
print()
file_manager.create_file(os.path.join(package_path,"sample.txt"), "Hello, this is a test file.")
file_manager.list_files(package_path)
print()
file_manager.delete_file(os.path.join(package_path,"sample.txt"))
print()
file_manager.list_files(package_path)