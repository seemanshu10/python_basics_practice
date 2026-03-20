import sys

if "--simulate" in sys.argv:
    print("Simulation mode: No files will be deleted.")
else:
    print("Cleaning up temporary files...")
