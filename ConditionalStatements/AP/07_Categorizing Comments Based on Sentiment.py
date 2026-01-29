"""
Accept a user's comment or message as input.
Normalize the input using .strip() and .lower().
Use membership operators to check for specific keywords (e.g., “excellent”, “bad”, “average”, “worst”, “great”).
Based on these keywords:
• Classify the comment as Positive, Neutral, or Negative.
• Use conditional logic with string comparisons and in/not in to determine the sentiment category.
• Display a categorized summary using f-strings and a decorative line created with repetition.
• Format the summary using newlines (\n) and escape sequences to keep it readable.
"""

# Enter The User review string 

# Enter the user input Password 
or_comment = input("Enter Your Comment: ")

# normalize the input 
re_Spaces = or_comment.strip()
norm_Comment = re_Spaces.lower()

# determine categories 

if "excellent" in norm_Comment or "great" in norm_Comment or "good" in norm_Comment:
    category = "Positive"

elif "bad" in norm_Comment or "worst" in norm_Comment or "poor" in norm_Comment:
    category = "Negative"

else:
    category = "Neutral"

# Divider line 
divider_line = "="*50

# display results 
print(
    f"\n{divider_line}\n"
    f"Original Comment:\n{or_comment}\n\n"
    f"Sentiment Category:{category}\n\n"
    f"Thanks you for your feedback!\n"
    f"{divider_line}\n"
)

"""
Output : 
Enter Your Comment: This app is excellent and easy to use!

==================================================
Original Comment:
This app is excellent and easy to use!

Sentiment Category:Positive

Thanks you for your feedback!
==================================================
"""
