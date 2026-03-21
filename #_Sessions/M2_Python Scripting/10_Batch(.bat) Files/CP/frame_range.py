import sys
if len(sys.argv) == 3:
    start_frame = sys.argv[1]
    end_frame = sys.argv[2]
    
    print(f"Processing Frames from  {start_frame} to {end_frame}...")
else:
    print("Usage: frame_range.py <start_frame> <end_frame>")