# __init__.py (After)
print("Initializing my_package")



# ----- Wild card import  -----
from .module1 import greet




# ------- Using __all__
from .module1 import greet, add

__all__ = ["greet"]  




# ------  Import All Public Functions Using __all__
from .module1 import greet, add
from .module2 import multiply, divide
from .module3 import status_check
from .module4 import get_version

__all__ = [
    "greet", "add",
    "multiply", "divide",
    "status_check",
    "get_version"
]
