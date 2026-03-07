"""
Random Vacation Destination Picker
Task Objective
In this task, students will create a program that suggests a random vacation destination from a predefined list of destinations.
The program will also randomly select an activity and a cuisine specific to the destination.
Instructions
Import the random module.
Create a dictionary where each key is a vacation destination.
For each destination, define a list of activities and a list of cuisines.
Randomly select one destination from the dictionary.
Randomly select one activity and one cuisine related to that destination.
Print the full vacation plan to the console.

"""

import random 


# Dictionary of vacation destinations
vacations_dest = {
    "Paris": {
        "activities": ["Visit the Eiffel Tower", "Louvre Museum tour", "Seine River cruise"],
        "cuisines": ["French pastries", "Croissants", "Baguettes"]
    },
    "Tokyo": {
        "activities": ["Explore Shibuya", "Visit Senso-ji Temple", "Take a sushi class"],
        "cuisines": ["Sushi", "Ramen", "Tempura"]
    },
    "New York": {
        "activities": ["Visit Statue of Liberty", "Broadway show", "Central Park walk"],
        "cuisines": ["Bagels", "Pizza", "Cheesecake"]
    },
    "Rome": {
        "activities": ["Colosseum tour", "Vatican Museums", "Piazza Navona stroll"],
        "cuisines": ["Pasta Carbonara", "Gelato", "Pizza Margherita"]
    },
    "Bangkok": {
        "activities": ["Grand Palace visit", "Floating market tour", "Thai massage"],
        "cuisines": ["Pad Thai", "Green Curry", "Mango Sticky Rice"]
    }
}

# randomly select the vacation destination 
destination = random.choice(list(vacations_dest.keys()))
# print(destination)

# Randomly select an activity and cuisine for the chosen destination
activity = random.choice(vacations_dest[destination]["activities"])
cuisine = random.choice(vacations_dest[destination]["cuisines"])

# print vacation plan 

print("Welcome to the Random Vacation Destination Picker!")
print("Your Vacation Plan: ")
print(f"Destination: {destination}")
print(f"Activity: {activity}")
print(f"Cuisine: {cuisine}")

