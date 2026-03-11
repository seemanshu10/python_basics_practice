def calculate_file_size_in_kb(file_size_bytes):

    """Converts file size from bytes to kilobytes (KB)."""

    return file_size_bytes / 1024 

# example usage 

file_size_kb = calculate_file_size_in_kb(2048)
print(f"File size: {file_size_kb} KB")
# output : file size : 2.0 KB

def format_shot_name(sequence_number, shot_number):

    """Formats shot name as 'SEQ###_Shot##'."""

    return f"SEQ{sequence_number:03d}_SHOT{shot_number:03d}"

shot_name = format_shot_name(12,5)
print(shot_name)