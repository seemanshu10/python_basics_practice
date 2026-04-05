supported_formats = ["jpg", "png", "exr"]

def resize_image(image_path, width, height):
    return f"Resized {image_path} to {width}X{height}"

def apply_filter(image_path, filter_name):
    return f"Applied {filter_name} filter to {image_path}"