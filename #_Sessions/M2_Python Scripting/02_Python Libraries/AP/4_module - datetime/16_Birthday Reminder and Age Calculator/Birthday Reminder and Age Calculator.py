"""

Birthday Reminder and Age Calculator
Task Objective
In this task, you will:

Store a list of names and birthdates.
Identify birthdays occurring within the next 30 days.
Calculate and display the age of each person based on the current date.
Instructions
Create a list of birthdays using the format: "Name: YYYY-MM-DD".
Write a function to store the data in a dictionary with datetime objects.
Write a function that checks for upcoming birthdays within the next 30 days.
Write a function that calculates each person's age.
Print all stored birthdays.
Print the list of people with birthdays coming up within 30 days.
Print the name and age of each person.

"""

from datetime import datetime, timedelta

# Store raw birthday list

birthday_list = [
    "Alice: 1995-03-15",
    "Bob: 1988-03-25",
    "Charlie: 2000-04-10",
    "Diana: 1992-01-05"
]


# Convert list into dictionary with datetime objects

def create_birthday_dict(birthday_data):
    birthday_dict = {}
    
    for entry in birthday_data:
        name, date_str = entry.split(": ")
        birth_date = datetime.strptime(date_str, "%Y-%m-%d")
        birthday_dict[name] = birth_date
        
    return birthday_dict



# Find birthdays in the next 30 days

def upcoming_birthdays(birthday_dict):
    today = datetime.today()
    #print(today)
    next_30_days = today + timedelta(days=30) # add 30 fdays to today date
    # print(next_30_days)
    
    upcoming = []
    
    for name, birth_date in birthday_dict.items():
       
        # Create this year's birthday
        this_year_birthday = birth_date.replace(year=today.year)
        #print(this_year_birthday,name)
        
        if today <= this_year_birthday <= next_30_days:
            upcoming.append(name)
    
    return upcoming


# Calculate age function 

def calculate_age(birth_date):
    today = datetime.today()
    #print(today)
    age = today.year - birth_date.year
    
    # Adjust if birthday hasn't occurred yet this year
    if (today.month, today.day) < (birth_date.month, birth_date.day):
        age -= 1
        
    return age


# Main Execution

birthdays = create_birthday_dict(birthday_list)

print("All Stored Birthdays:")
for name, birth_date in birthdays.items():
    print(name + ":", birth_date.strftime("%Y-%m-%d"))

print("\nBirthdays in the Next 30 Days:")
upcoming = upcoming_birthdays(birthdays)
for name in upcoming:
    print(name)

print("\nCurrent Ages:")
for name, birth_date in birthdays.items():
    age = calculate_age(birth_date)
    print(name + " is", age, "years old.")