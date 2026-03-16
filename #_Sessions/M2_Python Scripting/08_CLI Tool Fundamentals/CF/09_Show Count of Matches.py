import sys

log_file = sys.argv[1]

with open(log_file, 'r') as file:
    log_lines = file.readlines()


keyword = sys.argv[2].upper()
count = 0


for line in log_lines:
    if keyword in line:
        print(line.strip())
        count += 1
        
# Print the total count
print(f"\nTotal {keyword} entries: {count}")