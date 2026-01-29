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

# Ask the user to enter the log entry
log_entry = input("Enter log entry: ")

# Input Crireria [user_id:12345] [status:active] [action:login] [time:10:45AM]

# split log into parts 
splitParts = log_entry.split("] [")
print(splitParts) 

# remove brackets from List 
remove_Bracket = []
for part in splitParts:
    part = part.replace("[","").replace("]","")
    remove_Bracket.append(part)

print(remove_Bracket)

# empty data 
data = {}