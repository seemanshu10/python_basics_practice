import sys

input_path = None
output_path = None

# Check for --input
if "--input" in sys.argv:
    idx = sys.argv.index("--input") + 2
    print(idx)
    if idx < len(sys.argv):
        input_path = sys.argv[idx]
        # print(input_path)

# Check for --output
if "--output" in sys.argv:
    idx = sys.argv.index("--output") + 1
    if idx < len(sys.argv):
        output_path = sys.argv[idx]

# Print the results
if input_path:
    print(f"Input folder: {input_path}")
else:
    print("No input folder provided.")

if output_path:
    print(f"Output folder: {output_path}")
else:
    print("No output folder provided.")