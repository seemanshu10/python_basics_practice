"""
A nested if means putting one if statemnet inside another . 
"""

# checking For Student Scholorship Eligibility 

grade = 88
extra_curricular = True

if grade >=85:
    if extra_curricular:
        print("Eligible For Scholarship. ")
    else:
        print("No Eligible For Scholarship .")
else:
    print("Not Eligible For scholarship(grade too low).")

# Output : Eligible For Scholarship. 

# Checking A discount Based Age and membership Status 

age = 30
is_member = False

if age >=25:
    if is_member:
        print("Discount: 20%")
    else:
        print("Discount: 18%")
else:
    print("Not Discount.")

# Output : 
# Discount: 18%

# Determing Eligibility for a special Event 
is_weekend = True
has_invite = False

if is_weekend:
    if has_invite:
        print("You can Attend the event.")
    else:
        print("You cannot Attend the event(no invite).")
else:
    print("You cannot Attend the event(not a weekend).")

# Output : You cannot Attend the event(no invite).

# Checking For Summer Internship Eligibility 

gpa = 3.5
completed_course = False

if gpa >=3.1:
    if completed_course:
        print("Eligible For Summer internship.")
    else:
        print("Not eligible For Summer internship(Course not Completed).")
else:
    print("Not eligible For Summer internship (GPA Too low).")
# OutPut : 
# Not eligible For Summer internship(Course not Completed).