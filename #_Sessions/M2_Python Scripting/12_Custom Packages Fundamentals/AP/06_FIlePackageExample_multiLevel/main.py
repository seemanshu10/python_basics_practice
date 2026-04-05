import sys
import os

# TODO: use insert for sys.path 
# Multi level packages creation 
# new AP creation 

package_path = os.path.dirname(os.path.abspath(__file__))
# print(package_path)
if package_path not in sys.path:
    sys.path.insert(0,package_path)

import vfx_utils

packages = os.path.join(os.path.dirname(package_path))
print(vfx_utils.list_files_func(os.path.dirname(package_path)))

print(vfx_utils.create_file_func(packages, "new_asset.txt"))

print(vfx_utils.resize_image_func("image.jpg", 1920, 1080))
print(vfx_utils.apply_filter_func("image.jpg", "Sepia"))

print(vfx_utils.start_render_func("Scene_01"))
print(vfx_utils.stop_render_func())

print(vfx_utils.log_info_func("All System operational"))
print(vfx_utils.log_error_func("Render Emgine Crashed"))
