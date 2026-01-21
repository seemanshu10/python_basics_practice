# 

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