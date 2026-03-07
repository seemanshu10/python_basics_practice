"""
Event Duration Calculator
Task Objective
In this task, you will:

Use the datetime module to parse two date-time strings.
Calculate the time difference between two events.
Convert the duration into days, hours, minutes, and seconds.
Display the result in a clear, readable format.
Instructions
Import the datetime module.
Define two datetime strings in the format "YYYY-MM-DD HH:MM:SS".
Parse the strings into datetime objects.
Calculate the time difference using subtraction.
Extract the days, hours, minutes, and seconds from the result.
Print the full duration in a formatted output.

"""
# Import the datetime module
from datetime import datetime

# Define two datetime strings
datetime_str1 = "2024-07-01 12:00:00"
datetime_str2 = "2024-07-02 14:30:15"

# Parse strings into datetime objects
dt1 = datetime.strptime(datetime_str1, "%Y-%m-%d %H:%M:%S")
dt2 = datetime.strptime(datetime_str2, "%Y-%m-%d %H:%M:%S")

# Calculate the time difference
time_difference = dt2 - dt1

# Extract days
days = time_difference.days

# Extract remaining seconds
remaining_seconds = time_difference.seconds

# Convert remaining seconds to hours, minutes, seconds
hours = remaining_seconds // 3600
minutes = (remaining_seconds % 3600) // 60
seconds = remaining_seconds % 60

# Print formatted result
print(f"Start: {datetime_str1}")
print(f"End:   {datetime_str2}")
print("Duration:")
print(f"{days} days, {hours} hours, {minutes} minutes, {seconds} seconds")