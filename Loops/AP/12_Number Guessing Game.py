"""

number guessing game where the computer randomly selects a number between 1 and 50, 
and the user has to guess it in as few attempts as possible. 
Provide feedback if the guess is too high or too low.
"""

# use list.choice in this instead 
import random
# computer selects random num ftom 1 to 50 
random_num = random.randint(1,50)

# keep asking user until guess is correct 

while True:
    # user input thier guess 
    guess = int(input("Guess a number Between 1 and 50:"))

    # check if guess is correct 
    if guess == random_num:
        print(" Congratulations! You guessed the correct number.")
        break
    elif guess > random_num:
        print(" Too High Guess! try Again!.")
    else :
        print(" Too Low Guess! try Again!.")
"""
Guess a number Between 1 and 50:25
 Too Low Guess! try Again!.
Guess a number Between 1 and 50:45
 Too High Guess! try Again!.
Guess a number Between 1 and 50:40
 Congratulations! You guessed the correct number.
"""
