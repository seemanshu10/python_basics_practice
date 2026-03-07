"""
✅ Task Objective:

• Use the input() function to collect user data.
• Store the inputs in variables using correct naming conventions.
• Combine first and last names into a single variable.
• Print all values clearly using the print() function.
• Use the type() function to display the data type of each variable.
• Use the len() function to calculate the number of characters in the full name.
• Perform an arithmetic operation on the age value to show the age after 5 years.

🛠️ Instructions:

1. Prompt the user to enter:
   • First name
   • Last name
   • Age
   • City of residence

2. Combine the first and last name into one variable called `full_name`.

3. Print the following with clear labels:
   • Full name
   • Age
   • City

4. Use the `type()` function to print the data type of each variable.

5. Use the `len()` function to:
   • Calculate the number of characters in the full name.
   • Print the character count.

6. Convert the `age` input to a number.
   • Add 5 to it.
   • Print the result as the future age.

7. Use meaningful variable names following the `snake_case` convention.

🖥️ Sample Output:

Enter your first name: Alice  
Enter your last name: Smith  
Enter your age: 25  
Enter your city of residence: Toronto

Full Name: Alice Smith  
City: Toronto  
Age: 25

Data Types:  
full_name: <class 'str'>  
age: <class 'str'>  
city: <class 'str'>

Length of full name: 11 characters  

In 5 years, you will be 30 years old.
"""

# asking for users name 

first_name = input("Enter your First name: ")
last_name = input("Enter Your Last name: ")
age = input("Enter your age: ")
city = input("Enter your city of Residence: ") 

full_name = first_name + " " + last_name

print("\nFull Name:", full_name)
print("Age:", age)
print("City:", city)

print("\nData types:")
print("Full Name:", type(full_name))
print("Age:", type(age))
print("City:", type(city))

print("\nLength of full name:", len(full_name))

int_age = int(age)
print(f"\nIn 5 years, you will be {int_age + 5} years old")