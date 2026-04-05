from file_manager.operations.file_list import list_files, list_files_dir
from file_manager.operations.file_create import create_file
from file_manager.operations.file_delete import delete_file


# List files
list_files(".")
print()
# list_files_dir(".")
# print()
# # Create a file
create_file(r"file_manager/sample.txt", "Hello, this is a sample file.")
print()
# # List files again
list_files(".")

# # Delete the file
print()
delete_file(r"file_manager/sample.txt")
print()
# # List files again
list_files(".")

r"""
python .\use_package.py

Operations Package initialized.
use_package.py
__init__.py
operations\file_create.py
operations\file_delete.py
operations\file_list.py
operations\__init__.py
operations\__pycache__\file_create.cpython-310.pyc
operations\__pycache__\file_delete.cpython-310.pyc
operations\__pycache__\file_list.cpython-310.pyc
operations\__pycache__\__init__.cpython-310.pyc
__pycache__\__init__.cpython-310.pyc


File 'sample.txt' created successfully.

sample.txt
use_package.py
__init__.py
operations\file_create.py
operations\file_delete.py
operations\file_list.py
operations\__init__.py
operations\__pycache__\file_create.cpython-310.pyc
operations\__pycache__\file_delete.cpython-310.pyc
operations\__pycache__\file_list.cpython-310.pyc
operations\__pycache__\__init__.cpython-310.pyc
__pycache__\__init__.cpython-310.pyc

File 'sample.txt' deleted successfully.

use_package.py
__init__.py
operations\file_create.py
operations\file_delete.py
operations\file_list.py
operations\__init__.py
operations\__pycache__\file_create.cpython-310.pyc
operations\__pycache__\file_delete.cpython-310.pyc
operations\__pycache__\file_list.cpython-310.pyc
operations\__pycache__\__init__.cpython-310.pyc
__pycache__\__init__.cpython-310.pyc

"""