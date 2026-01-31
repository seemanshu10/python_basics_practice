"""
Accept a simulated log entry string in the format:  
"[user_id:12345] [status:active] [action:login] [time:10:45AM]"

Use string operations to:
• Parse out each value using .split(), .find(), and slicing.  
• Remove enclosing brackets [] and labels like user_id:.  
• Reformat the parsed values into a structured, human-readable output block.  
• Use .replace(), .index(), .join(), and escape characters (\n, \t) to clean and format data.  
• Display the final log summary with consistent alignment using .ljust() or .rjust().
"""

# Prompt user for log entry
log_entry = input("Enter log entry: ").strip()

# Example expected format:
# [user_id:12345] [status:active] [action:login] [time:10:45AM]

# 1. Split the log into individual components
parts = log_entry.split("] [")

values = []

for part in parts:
    # 2. Remove brackets
    cleaned = part.replace("[", "").replace("]", "").strip()
    
    # 3. Split key and value
    colon_pos = cleaned.find(":")
    
    # 4. Slice out only the value
    value = cleaned[colon_pos + 1:]
    values.append(value)

# Assign extracted values
user_id, status, action, timestamp = values

# 5. Print formatted report
print("\n" + "=" * 40)
print("LOG SUMMARY")
print("-" * 40)

print("User ID".ljust(10) + ":\t" + user_id)
print("Status".ljust(10) + ":\t" + status)
print("Action".ljust(10) + ":\t" + action)
print("Timestamp".ljust(10) + ":\t" + timestamp)

print("-" * 40)
print("\"All data extracted successfully.\"")
print("=" * 40)