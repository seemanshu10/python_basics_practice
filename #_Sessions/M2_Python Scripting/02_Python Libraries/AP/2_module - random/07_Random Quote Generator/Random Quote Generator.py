"""
Random Quote Generator
Task Objective
In this task, students will create a program that displays a random inspirational quote from a predefined list.
The program will randomly select a quote and print it to the console.
Instructions
Import the random module.
Define a list containing multiple inspirational quotes as string elements.
Randomly select one quote from the list.
Print a welcome message followed by the selected quote in a formatted output.
"""

import random
# List of quotes
quotes = [
    '"The best way to predict the future is to invent it." - Alan Kay',
    '"Life is what happens when you\'re busy making other plans." - John Lennon',
    '"Do not take life too seriously. You will never get out of it alive." - Elbert Hubbard',
    '"In the middle of difficulty lies opportunity." - Albert Einstein',
    '"Success is not final, failure is not fatal: it is the courage to continue that counts." - Winston Churchill'
]

print("Welcomne to random Name picker ")

choice_rand = random.choice(quotes)
print("Your inspirational quote is:",choice_rand)