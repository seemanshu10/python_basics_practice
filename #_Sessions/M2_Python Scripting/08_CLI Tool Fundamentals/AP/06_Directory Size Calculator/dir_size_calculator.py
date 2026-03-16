import sys
import os

def directory_size_calculator(directory_path, size_format):
    """
    Calculate the total size of all files inside a directory (recursively).

    Args:
        directory_path (str): Path to the directory.
        size_format (str): Output format - bytes, kilobytes, or megabytes.
    """

    # Check if directory exists
    if not os.path.isdir(directory_path):
        print(f"Error: '{directory_path}' does not exist.")
        return

    total_size = 0

    # Walk through directory and sum file sizes
    for root, _ , files in os.walk(directory_path):
        for file in files:
            path = os.path.join(root, file)
            total_size += os.path.getsize(path)

    size_format = size_format.lower()

    # Format output size
    if size_format == "bytes":
        print("Total size:", total_size, "bytes")
    elif size_format == "kilobytes":
        print("Total size:", total_size / 1024, "KB")
    elif size_format == "megabytes":
        print("Total size:", total_size / (1024 * 1024), "MB")
    else:
        print("Invalid format given.")

def main():
    if len(sys.argv) < 2 or len(sys.argv) > 3:
        print("Usage: python directory_size.py <directory_path> [bytes|kilobytes|megabytes]")
        sys.exit(1)

    directory_path = sys.argv[1]

    if len(sys.argv) == 3:
        size_format = sys.argv[2]
    else:
        size_format = "bytes"   # default value if nonone given 

    directory_size_calculator(directory_path, size_format)

if __name__ == "__main__":
    main()


"""
python dir_size_calculator.py test_size_dir
Total size: 10240 bytes

 python dir_size_calculator.py test_size_dir kilobytes
Total size: 10.0 KB

python dir_size_calculator.py test_size_dir megabytes
Total size: 0.009765625 MB
"""