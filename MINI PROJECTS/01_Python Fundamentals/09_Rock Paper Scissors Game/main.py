"""
Rock Paper Scissors Game
Objective:
In this task, you will:
Learn how to structure interactive gameplay logic between a user and a computer opponent.
Practice decision-making using conditional checks to determine winners.
Explore how to improve user experience using emoji feedback and clear input/output handling.
Instructions:
Create a terminal-based Rock Paper Scissors game where the player competes against the computer.
Do not use the random module. The computer will use a fixed, repeating pattern for its moves: rock → paper → scissors → repeat.
Game Setup
Display a formatted welcome banner with emojis at the beginning.
Ask the user to enter their name.
Display the list of valid moves: rock, paper, scissors.
Game Flow
For each round:
Ask the user to input their move.
The computer selects its move based on the repeating pattern.
Display both choices using emojis.
Determine the winner using standard rules:
Rock 🪨 beats Scissors ✂️
Scissors ✂️ beats Paper 📄
Paper 📄 beats Rock 🪨
Show round result using friendly messages:
Example:
Alex chose ✂️   Computer chose 📄
✂️ beats 📄 → Alex wins this round!
Score Tracking
Keep track of:
Total rounds played
Player wins
Computer wins
Draws
After each round, ask:
Play another round? (yes/no):
Game End
When the player chooses to stop:
Display a final game summary:
Total rounds
Wins and draws
Final winner or tie result
Display appropriate error messages for:
Invalid move input
Unexpected choices (anything not in rock/paper/scissors)
Case sensitivity should be handled (e.g., ROCK and Rock should both work)
"""


def play_rockPaperScissors(player_name, scores, total_games):
    """
    
    Plays one round of Rock Paper Scissors using number-based input.
    Computer follows a fixed repeating pattern: rock → paper → scissors → ...
    Updates the scores dictionary in place.
    """
    moves_pattern = ["rock", "paper", "scissors"]
    # Display choices
    while True:
        print("\nValid moves: \n1 : rock\n2 : paper\n3 : scissors")
        
        choice_move = int(input("Enter your choice: ").strip())
        if choice_move in [1,2,3]:
            break
        else:
            print("Invalid choice! Enter 1,2,3.")
        

    # print(moves_pattern[choice_move-1])
    choice_user = moves_pattern[choice_move-1]
    #print(user_move)
    
    choice_computer = moves_pattern[total_games%3] 
    #print(choice_computer)

    # Show choices
    print(f"\n{player_name} chose {choice_user}, Computer chose {choice_computer}")

    # Determine winner
    if choice_user == choice_computer:
        print("🤝 It's a draw!")
    elif (
        (choice_user == "rock" and choice_computer == "scissors") or
        (choice_user == "scissors" and choice_computer == "paper") or
        (choice_user == "paper" and choice_computer == "rock")
    ): # win loase conditions 
        print(f"{choice_user} beats {choice_computer} → {player_name} wins! 🎉")
        scores[player_name] += 1

    else:
        print(f"{choice_computer} beats {choice_user} → Computer wins! 🤖")
        scores["Computer"] += 1



# main game state start handle 
def mainCoreLogic(player_name, scores, total_games):

    while True:
        play_rockPaperScissors(player_name, scores, total_games)
        total_games += 1
        
        while True:         # validating correct input 
            replay = input("Play Another round(y/n): ").strip().lower()
            
            # replay value is y
            if replay == "y":   
                print("Another round!")
                break
            
            # replay value is n
            elif replay == "n":
                print("\nThank you for playing! Goodbye! .\n")
                print(f"GAME SUMMARY ,Total Games Played : {total_games}")
                print(f"{player_name} WINS : {scores[player_name]}")
                print(f"Computer WINS : {scores['Computer']}")
                # checking scores and find final winner  
                if scores[player_name] > scores["Computer"]:
                    print(f"\nFinal Winner {player_name}!")

                elif scores[player_name] > scores["Computer"]:
                    print("\nFinal Winner Computer better luck next time!")

                else :
                    print("\n It is a draw!")
                
                return
            
            else:
                print("Invalid input. please Enter only (y/n)." )
                continue
        

# function for help state shows the rules of game 
def display_helpState():

    print("\nROCK PAPER SCISSORS HELP")
    print("----------------")
    
    print("\nRules:")
    print("- Player 1 ")
    print("- Computer")
    print("- Ask the user to input their move.\nDetermine the winner using standard rules:\nRock 🪨 beats Scissors ✂️ \nScissors ✂️ beats Paper 📄\nPaper 📄 beats Rock 🪨")
    print("- If both computer and player choose same it is draw \n")


# main function to launch game and menus 
def RockPaperScissorsGame():
    
    scores  = {}            # score data 
    total_games = 0         # total no. of games played 

    while True:
        title = "Rock 🪨 Paper 📄 Scissors ✂️"
        # title card 
        print("="*50)
        print(title.center(50))
        print("="*50)
        print("\n1. New Game")
        print("2. Get Help")
        print("3. Exit")

        try :
            state_of_game = int(input("Choose a state of Game(1/2/3) :"))
            #print(state_of_game)

            if state_of_game == 1:
                player_name = input("Enter Player Name: ")

                # score Tracking in a dictionary also adding second player as computer
                
                if player_name not in scores:
                    scores[player_name] = 0
                    scores["Computer"] = 0

                # print(scores)

                mainCoreLogic(player_name, scores, total_games)

            elif state_of_game == 2:
                # calling help state 
                display_helpState() 
                continue    # go back to menu does not exit 

            elif state_of_game == 3:
                print("Thanks For Playing !")
                return      # exit function completely 

            else: 
                print("Invalid Menu choice. Please select 1,2,or 3. ")
        
        except ValueError:
            print("Invalid Input! . Valid input is only 1,2,3 .") 
            continue

        except KeyboardInterrupt:
            print("Exiting Cleanly . ") 
            break
    
# calling main function 
RockPaperScissorsGame()