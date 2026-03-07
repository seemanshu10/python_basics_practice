"""

"""

# Displaying Book Information

def book_info(title , author , year):
    print(f" {title} by {author} ,publish {year}. ")

book_info("1984","George Orwell",1949)

#  1984 by George Orwell ,publish 1949.

# Calculating the Perimeter of a Rectangle

def calculate_perimeter(length,width):
    peri = 2*(length+width)
    print(f"The Perimeter of Rectangle is {peri} units . ")

calculate_perimeter(10,6)

# The Perimeter of Rectangle is 32 units .

# Food Order Example

def food_order(main_course , side_dish , drink):
    print(f" You ordered {main_course} with {side_dish} and a {drink}. ")

food_order("Burger","Fries","Coke")

# You ordered Burger with Fries and a Coke.

# keyword arguments 

def introduce(name,age,city):
    print(f"My name is {name}, I'm {age} years old, and I live in {city} . ")

introduce(name = "Alice",city="London",age=25)

# My name is Alice, I'm 25 years old, and I live in London .

# sending an email notification 

def send_email(subject, recipient,message):
    print(f"Sending Email to {recipient} with subject '{subject}' and message : {message}")

send_email(subject="Meeting Remainder",recipient='John@exaple.com',message="Don't forget our meeting at 10 AM.")
# Sending Email to John@exaple.com with subject 'Meeting Remainder' and message : Don't forget our meeting at 10 AM.

# default Arguments 

# Greeting with a Default Name

def greet(name = "Guest"):
    print(f"Hello ,{name}!")

greet()
# Hello ,Guest!
greet("David")
# Hello ,David!

# Sending a Reminder with Default Time

def send_reminder(task, time = "09:00 AM"):
    print(f"Remainder {task} at {time}.")

send_reminder("Team Meeting ! ")
# Remainder Team Meeting !  at 09:00 AM.

send_reminder ("Doctor's Appointment ","03:00 PM")
# Remainder Doctor's Appointment  at 03:00 PM.

# Making a Pizza Order with Default Size

def order_pizza(size = "Medium", toppings = None):
    if toppings is None:
        toppings = []

    print(f"Ordering a {size} pizza with toppings : {','.join(toppings)}.")

order_pizza()
# Ordering a Medium pizza with toppings : .

order_pizza(size="Large",toppings=["Pepporoni","Mushrooms"])
# Ordering a Large pizza with toppings : Pepporoni,Mushrooms.