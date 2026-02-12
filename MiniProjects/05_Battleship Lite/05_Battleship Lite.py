"""
Battleship Lite
Objective:
In this task, you will:
Learn how to design a grid-based game using lists and coordinate systems.
Practice handling user input for position-based logic.
Strengthen your ability to manage game state and validate win conditions.
Instructions:
Create a terminal-based Battleship game between a single player and the computer.
The game board should be a 5x5 grid.
The computer's ship locations will be predefined (no random module is allowed).
The player must guess coordinates to "hit" ships.
The goal is to sink all enemy ships.
Game Setup
Display a welcome screen and game title.
Show an empty grid (e.g., - for unguessed positions).
Use a 5x5 grid with coordinates ranging from (0,0) to (4,4).
Computer's Ship Placement
Predefine 3 ship positions in the code:
Each ship occupies 1 cell
Example: [(1,1), (2,3), (4,0)]
Gameplay Loop
Ask the player to enter a target coordinate (row and column).
Validate input:
Must be numbers
Must be within the 0-4 range
Must not be a previously guessed location
Update the board after each guess:
X for hit
O for miss
Display updated board after every turn.
Track total hits and guesses.
Game End
Once all 3 ships are hit:
Display victory message
Show number of total guesses
Optionally ask if the user wants to replay (optional)
Display appropriate error messages for:
Invalid input types
Out-of-range coordinates
Repeated guesses

"""

# Function to check guess and update board
def get_valid_position(row, col, ships, board):
    if (row, col) in ships:
        print("💥 Hit!")
        board[row][col] = "X"
        return True
    else:
        print("Miss 💦")
        board[row][col] = "O"
        return False

# taking in players guess for row and column 
def player_guess(guessed_position):
    while True:
        row = input("Enter row (0-4): ").strip()
        column = input("Enter Column (0-4): ").strip()

        # Check if input is numeric
        if not row.isdigit() or not column.isdigit():
            print("Error: Please enter numbers only.")
            continue

        row, column = int(row), int(column)

        # Check range
        if row < 0 or row > 4 or column < 0 or column > 4:
            print("Error: Coordinates must be between 0 and 4.")
            continue

        # Check repeated guesses
        if (row, column) in guessed_position:
            print("Error: You already guessed that location.")
            continue

        guessed_position.add((row, column))
        return row, column

# battleship Board loop 
def battleship_board(board):
    print("\n  0 1 2 3 4")
    for i, row in enumerate(board):
        print(f"{i} " + " ".join(row))
    print()

# core game loop for player 
def play_battleShip(player_name):
    # Create 5x5 board
    board = [["-" for _ in range(5)] for _ in range(5)]
    ships = [(1, 1), (2, 3), (4, 0)]                    # ships predefined position 
    hits = 0 
    misses = 0 
    guesses = 0 
    guessed_position = set()
    battleship_board(board)

    while hits < len(ships):
        row, column = player_guess(guessed_position)
        guesses += 1
        if get_valid_position(row, column, ships, board):
            hits +=1
        else:
            misses += 1

        battleship_board(board)
        print(f"Hits: {hits} | Misses: {misses} | Total Guesses: {guesses}")

    print(f"🎉 Congratulations {player_name}! You sank all ships in {guesses} guesses!\n")
    return


# help state which gives out all the rules 
def display_helpState():
    # bringing rules from rules txt file 
    try:
        ruleText_filePath = r"MiniProjects\05_Battleship Lite\battleshipRule.txt"
        with open(ruleText_filePath,"r") as rule_file:
            print("\n"+rule_file.read())

    except FileNotFoundError:
        print(f"File Not Found Error. Check Path:",ruleText_filePath)     


# main menu call 
def BattleShipLiteGame():

    scores = {}             # score data 
   
    while True:
        title = "🚢 Battleship Lite - Terminal"
        # title card 
        print("="*50)
        print(title.center(50))
        print("="*50)

        # printing main menu 
        print("\n1. New Game")
        print("2. Get Help")
        print("3. Exit")

        try:
            state_OfGame = input("Choose an option: ").strip()      # choosing inputs 

            # if input is empty 
            if not state_OfGame:
                print("Please enter a choice cannot be empty!")
                continue

            if state_OfGame == "1":
                player_name = input("Enter Player Name: ")

                # score Tracking in a dictionary also adding second player as computer
                
                if player_name not in scores:
                    scores[player_name] = 0
                    
                # main core logic
                play_battleShip(player_name)

            elif state_OfGame == "2":
                display_helpState()

            elif state_OfGame == "3":
                print("Thanks For Playing!")
                return
            
            else:
                print("Invalid choice. Please select only 1, 2, or 3.")

        except KeyboardInterrupt:           # keyboard interrupt error catch 
            print("Exiting Cleanly! ")
            return

BattleShipLiteGame()