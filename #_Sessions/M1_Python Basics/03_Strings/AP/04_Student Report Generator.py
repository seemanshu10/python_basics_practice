"""
✅ Task Objective:
Accept input for a student’s name, subject, and score.
Remove extra spaces using the strip() method.
Format the student name in lowercase and capitalize the subject.
Use the .format() method to generate a formatted report sentence.
Use an f-string to summarize the performance.
Add a divider line using repetition (*) and show it above and below the report.

🛠 Instructions:
• Ask the user to enter the student’s name, subject, and score.
• Clean each input string using strip().
• Convert the name to lowercase and the subject to title case (capitalize the first letter of each word).
• Use * 40 to create a decorative line.
• Construct a sentence like "Student John has scored 87 in Mathematics." using .format().
• Create a summary sentence using f-string, like "john’s performance in Mathematics is satisfactory."
• Display both sentences surrounded by divider lines.

📤 Sample Output:

Enter student name:  JOHN  
Enter subject:   mathematics  
Enter score: 87

****************************************
Student John has scored 87 in Mathematics.
john’s performance in Mathematics is satisfactory.
****************************************
"""


# Ask the user for input
name = input("Enter student's name: ").strip()
subject = input("Enter subject: ").strip()
score = input("Enter score: ").strip()

# Convert string formats
name_lower = name.lower()
subject_title = subject.title()

# Create decorative line
line = "*" * 40

# Construct sentences
sentence1 = "Student {} has scored {} in {}.".format(name, score, subject_title)
sentence2 = f"{name_lower}'s performance in {subject_title} is satisfactory."

# Display output
print(line)
print(sentence1)
print(sentence2)
print(line)