"""
✅ Task Objective:

Accept a simulated log entry string in the format:  
"[user_id:12345] [status:active] [action:login] [time:10:45AM]"

Use string operations to:
• Parse out each value using .split(), .find(), and slicing.  
• Remove enclosing brackets [] and labels like user_id:.  
• Reformat the parsed values into a structured, human-readable output block.  
• Use .replace(), .index(), .join(), and escape characters (\n, \t) to clean and format data.  
• Display the final log summary with consistent alignment using .ljust() or .rjust().

🛠 Instructions:
• Ask the user to paste a full log line in the format:  
  [user_id:12345] [status:active] [action:login] [time:10:45AM]
• Extract each data component (user_id, status, action, time) from the string using slicing and splitting.  
• Clean up the raw data by removing brackets and keys.  
• Use .replace(), .split(), .strip(), and slicing to isolate just the values.  
• Reconstruct and print a readable, aligned report:  
  - One line per key-value pair, aligned using .ljust() and \t.  
  - Include a decorative border and a closing note with escaped quotation marks.

📤 Sample Output:

Enter log entry: [user_id:12345] [status:active] [action:login] [time:10:45AM]

========================================  
LOG SUMMARY  
----------------------------------------  
User ID   :	12345  
Status    :	active  
Action    :	login  
Timestamp :	10:45AM  
----------------------------------------  
"All data extracted successfully."  
========================================
"""

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
    # Remove brackets
    cleaned = part.replace("[", "").replace("]", "").strip()
    
    #Split key and value
    colon_pos = cleaned.find(":")
    
    #Slice out only the value
    value = cleaned[colon_pos + 1:]
    values.append(value)

# Assign extracted values
user_id, status, action, timestamp = values

#  Print formatted report
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
