import sys
import os

# TODO: use insert for sys.path 
# Multi level packages creation 
# new AP creation 

package_path = os.path.dirname(os.path.abspath(__file__))
# print(package_path)
if package_path not in sys.path:
    sys.path.insert(0,package_path)
# print(sys.path)

from vfx_utils import (
    list_files, create_file,
    resize_image, apply_filter,
    start_render, stop_render,
    log_info, log_error

)

packages = os.path.join(os.path.dirname(package_path))
print(list_files(os.path.dirname(package_path)))
print(create_file(packages, "new_asset.txt"))

print(resize_image("image.jpg", 1920, 1080))
print(apply_filter("image.jpg", "Sepia"))

print(start_render("Scene_01"))
print(stop_render())

print(log_info("All System operational"))
print(log_error("Render Emgine Crashed"))