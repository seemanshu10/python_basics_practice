"""
Working with Dates and Times
Task Objective
In this task, you will:

Perform operations using the datetime and timedelta classes.
Work with dates, times, intervals, formatting, and date arithmetic.
Use this knowledge to solve real-world scheduling and time-handling scenarios.

"""

# Import the datetime module
from datetime import datetime
# Calculate the Number of Days Between Two Dates
# Subtask 1: Calculate the Number of Days Between Two Dates

# Input two dates in YYYY-MM-DD format
date1_str = "2024-01-01"
date2_str = "2024-07-22"

date1 = datetime.strptime(date1_str, "%Y-%m-%d")
date2 = datetime.strptime(date2_str, "%Y-%m-%d")

# difference b/w date 
delta = date2 - date1

# print the number of days 
print(f"The number of days between {date1_str} and {date2_str} is {delta.days} days.")

# The number of days between 2024-01-01 and 2024-07-22 is 203 days.

# Subtask 2: Format a Date to DD/MM/YYYY
#Instruction Convert a date from the format YYYY-MM-DD to DD/MM/YYYY.


# Input dates in YYYY-MM-DD format
date_str = "2024-01-01"

# Convert the string to a datetime object
date = datetime.strptime(date1_str, "%Y-%m-%d")

# Format the datetime object to DD/MM/YYYY
formatted_date = date.strftime("%d/%m/%Y")

# Print the formatted date
print(f"The date {date_str} in DD/MM/YYYY format is {formatted_date}.")

"""
Subtask 3: Add Seconds to a Given Time
Instruction Input a time in HH:MM:SS format and a number of seconds. Return the new time.
"""
from datetime import datetime, timedelta
# Input time and number of seconds
time_str = "12:30:15"
seconds_to_add = 3600

# Convert string to datetime object
time_obj = datetime.strptime(time_str, "%H:%M:%S")

# Add seconds using timedelta
new_time = time_obj + timedelta(seconds=seconds_to_add)

# Format back to HH:MM:SS
result_time = new_time.strftime("%H:%M:%S")

# Print result
print(f"Original time: {time_str}")
print(f"After adding {seconds_to_add} seconds: {result_time}")

"""

Subtask 4: Calculate Age from Birthdate
Instruction Input a birthdate in the format YYYY-MM-DD. Return the person's age in years (based on today’s date).
"""

# import the database module 
from datetime import datetime, date

birthdate_str = "2000-05-15"

# Convert the string to a datetime object
birthdate  = datetime.strptime(birthdate_str, "%Y-%m-%d").date()

# Get today's date
today = date.today()

# Calculate age
age = today.year - birthdate.year

# Adjust if birthday hasn't occurred yet this year
if (today.month, today.day) < (birthdate.month, birthdate.day):
    age -= 1

# Print result
print(f"Birthdate: {birthdate_str}")
print(f"Age: {age} years old")
