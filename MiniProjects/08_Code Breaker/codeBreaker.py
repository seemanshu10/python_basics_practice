"""
Code Breaker
Objective:
In this task, you will:
Learn to create a multi-step guessing game that compares player input to a secret code.
Strengthen your ability to break down logic for position-based matching.
Practice iterating through lists and applying conditional checks for feedback.
Instructions:
Create a terminal-based code guessing game, where the player tries to break a 4-digit secret code.
Do not use the random module — use a fixed secret code (e.g., ["3", "1", "4", "2"]) stored in a list.
The player gets limited attempts (e.g., 8 tries) to guess the correct code.
Accept guesses as a 4-digit number, and validate:
Must be exactly 4 digits
All characters must be numbers
After each guess:
Compare each digit with the secret code
Provide feedback for each digit:
Correct digit and correct position → "✔"
Correct digit but wrong position → "→"
Digit not in the code → "✖"
Feedback Example:
Secret Code: [3, 1, 4, 2]
Player Guess: 3 4 2 8
Feedback    : ✔ → → ✖
If the player guesses all 4 digits in the correct positions, show a success message and stop the game.
If the player uses all attempts without breaking the code, reveal the correct code and show a failure message.
Track and show the number of attempts used.
Display appropriate error messages for:
Invalid input (non-digit characters, wrong length)


"""

SECRET_CODE = ["3", "1", "4", "2"]      # Main function TO handle main menu and inputs 
TOTAL_ATTEMPTS = 8              # total no. of attempts to be there 


def get_feedback(guessCode):
    feedback = ["✖"] * 4       # assuming everything is X first 
    remaining = [] 

    # First pass: correct position
    for i in range(4):          # adding "✔" in correct position and holds only unused secret digits
        if guessCode[i] == SECRET_CODE[i]:
            feedback[i] = "✔"
            
        else:
            remaining.append(SECRET_CODE[i]) # remaining contains all the values which is not guessed correctly 
            # print(remaining)
    # Second pass: correct digit, wrong position
    for i in range(4):
        if feedback[i] == "✖" and guessCode[i] in remaining:
            feedback[i] = "→"
            remaining.remove(guessCode[i])

    return feedback

def codeBreaker_mainLogic():
    attempts = 0  # no. of attempts done  
                
    print(f"You have {TOTAL_ATTEMPTS} attempts.")

    while attempts < TOTAL_ATTEMPTS:
        while True:
            guessCode = input("Enter your guess: ")
            #print(guessCode)

            if not guessCode.isdigit() or len(guessCode) != 4:
                print("Invalid code. Must be exactly 4 digits.")
            else:
                break   # valid input → exit inner loop

        attempts += 1
        print(f"Attempt {attempts}: {guessCode}")

        feedback = get_feedback(guessCode)
        print("Feedback is :", feedback)

        # success condition
        if feedback == ["✔", "✔", "✔", "✔"]:
            print("🎉 Congratulations! You broke the code!")
            print(f"You solved it in {attempts} attempts.")
            return
        
    # Fail Conditions 
    print("💥 You've used all attempts! , Game Over!")
    print("The correct code was:", SECRET_CODE)


# function for help state shows the rules of game 
def display_helpState():

    print("\nCODE BREAKER HELP")
    print("----------------")
    print("\nRules:")
    print("- The player gets limited attempts (e.g., 8 tries) to guess the correct code.")
    print("- Accept guesses as a 4-digit number, and validate: Must be exactly 4 digits .All characters must be numbers")
    print(
    "- Compare each digit with the secret code.\n"
    "- Provide feedback for each digit:\n"
    "- Correct digit and correct position → ✔\n"
    "- Correct digit but wrong position → →\n"
    "- Digit not in the code → ✖"
    )
    print("- If the player guesses all 4 digits in the correct positions, show a success message and stop the game.\nIf the player uses all attempts without breaking the code, reveal the correct code and show a failure message.\n")


def CodeBreakerGame():

    while True:
        title = "🧠 Welcome to Code Breaker"
        print("="*50)
        print(title.center(50))
        print("="*50)
        
        print("\n1. New Game")
        print("2. Get Help")
        print("3. Exit")
        

        try :
            state_of_game = int(input("Choose a state of Game(1/2/3) :"))

            if state_of_game == 1:
                codeBreaker_mainLogic()
                
            elif state_of_game == 2:
                # calling help state 
                display_helpState() 
                continue    # go back to menu does not exit 

            elif state_of_game == 3:
                print("Thanks For Playing !")
                return      # exit function completely 

            else: 
                print("Invalid Menu choice. Please select 1,2,or 3.")
        
        except ValueError:
            print("Invalid Input! . Valid input is only integer.") 
            continue

        except KeyboardInterrupt:           # keyboard exit cleanly 
            print("\nExiting Cleanly . ") 
            break

# calling main function 
CodeBreakerGame()