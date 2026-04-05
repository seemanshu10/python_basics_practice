import sys
import os

# Add package path dynamically
package_path = os.path.abspath("path/to/vfx_utils")
if package_path not in sys.path:
    sys.path.append(package_path)

# Import utilities directly from the package
from vfx_utils import (
    list_files, create_file,
    resize_image, apply_filter,
    start_render, stop_render,
    log_info, log_error
)

# File Manager
print(list_files("/project/assets"))
print(create_file("/project/assets", "new_asset.txt"))

# Image Processor
print(resize_image("image.jpg", 1920, 1080))
print(apply_filter("image.jpg", "Sepia"))

# Renderer
print(start_render("Scene_01"))
print(stop_render())

# Logger
print(log_info("All systems operational"))
print(log_error("Render engine crashed"))
