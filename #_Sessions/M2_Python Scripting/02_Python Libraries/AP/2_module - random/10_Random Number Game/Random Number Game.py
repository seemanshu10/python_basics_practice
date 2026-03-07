"""
Random Number Game
Task Objective
In this task, you will:

Generate a random number using the random module.
Prompt the user to guess the number.
Provide feedback to the user based on their guess.
Repeat until the user guesses the correct number.

Instructions
Import the random module.
Generate a random integer between 1 and 100.
Prompt the user to enter their guess through the console.
If the guess is too low, print a message indicating that.
If the guess is too high, print a message indicating that.
Continue prompting until the correct number is guessed.
Print a congratulatory message when the correct number is guessed.

"""

import random

random_num = random.choice(range(1,100))
print(random_num)

while True:
    try:
        user_Choice = int(input("Enter Your Number: "))
        if random_num == user_Choice:
            print(f"Congratulations! You guessed the correct number: {random_num}")
            break
        elif random_num <= user_Choice:
            print("Too high! Try Again.")
        else:
            print("Too Low! Try Again.")

    except ValueError:
        print("Only Integer between 1 to 100 can be entred. ")

