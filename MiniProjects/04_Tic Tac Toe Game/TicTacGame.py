"""
Objective:
In this task, you will:
Learn how to design and manage turn-based logic between two players.
Understand how to use functions to structure gameplay and handle winning conditions.
Practice capturing user input and managing game state using a list-based board system.


Instructions:
Create a terminal-based Tic Tac Toe game for two players.
Display a main menu that allows the user to:
Start a new game
View help instructions
Exit the program
Help Menu
Display the board layout with positions (1-9).
Briefly explain the rules:
Player 1 uses X
Player 2 uses O
First to get 3 in a row wins (horizontal, vertical, or diagonal)

Game Flow
Ask for Player 1 and Player 2 names.
Display the board using the correct layout after each move.
Alternate turns between Player 1 and Player 2.
Prompt the player to enter a position (1-9).
Validate input:
Input must be a number between 1 and 9
Position must not already be taken
Update the board with the appropriate mark (X or O).
After each move, check:
If the current player has won
If the game is a draw
Winning & Replay
If a player wins, display a message with their name.
Keep track of how many rounds each player wins.
Ask the user if they want to replay or quit after each round.
On quit, display a summary of total wins for both players.
Display appropriate error messages for:
Invalid menu choice
Invalid board positions
Non-integer or unexpected input

"""
def get_valid_position(board):
    while True:
        try:
            position = int(input("Choose a position (1-9): "))
            if position < 1 or position > 9:
                print("Position must be between 1 and 9.")
            elif board[position - 1] != " ":
                print("That position is already taken.")
            else:
                return position - 1
        except ValueError:
            print("Please enter a valid number.")

def check_drawState(board):
    # checking if the state is draw or not so uf there are spaces the win or lose conditions is not there 

    for space in board:
        if space == " ":
            return False
    
    return True

def play_gameState(player1, player2, scores):

    # play game state Definition 
    board = [" "]*9
    current_player = player1
    current_mark = "X"

    while True:

        display_board(board)
        print(f"{current_player}'s turn ({current_mark})")
        move = get_valid_position(board)
        board[move] = current_mark

        if check_win(board, current_mark):
            display_board(board)
            print(f"{current_player} wins this round!")
            scores[current_player] += 1
            break

        if check_drawState(board):
            display_board(board)
            print("It's a draw!")
            break

        # Switch player condition 
        if current_player == player1:
            current_player = player2
            current_mark = "O"
        else:
            current_player = player1
            current_mark = "X"

#  store allthe win conditions and check if any win state is satisfied with one symbol 
def check_win(board, mark):
    win_combinations = [
        (0,1,2),(3,4,5),(6,7,8), # rows win states 
        (0,3,6),(1,4,7),(2,5,8), # columns Win states
        (0,4,8),(2,4,6)          # diagonals win state   
    ]

    for combination in win_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == mark:
            return True
    
    return False

# help function which diplays the rules for game detailed 
def display_helpState():

    print("\nTIC TAC TOE HELP")
    print("----------------")
    print("Board Positions:")
    print(" 1 | 2 | 3 ")
    print("---+---+---")
    print(" 4 | 5 | 6 ")
    print("---+---+---")
    print(" 7 | 8 | 9 ")
    print("\nRules:")
    print("- Player 1 uses X")
    print("- Player 2 uses O")
    print("- First player to get 3 in a row (horizontal, vertical, or diagonal) wins")
    print("- If the board fills with no winner, the game is a draw\n")

# displays the current board
 
def display_board(board):
    print("\n")
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("---+---+---")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("---+---+---")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\n")

# main Tictac Game logic call 
def TicTacGame():
    # Creating main controls for game 
    scores = {}         # scores values 
    total_games = 0     # total games counter 
    while True:
        print("\nWELCOME TO TIC TAC TOE")
        print("1. New Game")
        print("2. Get Help")
        print("3. Exit")

        state_OfGame = input("Choose an option: ")  # choosing inputs 

        if state_OfGame == "1": # game starts 
            player1 = input("Enter Player 1 name: ")
            player2 = input("Enter Player 2 name: ")

            # score tracking 
            if player1 not in scores:
                scores[player1] = 0

            if player2 not in scores:
                scores[player2] = 0
            # print(scores) 
            while True:
                play_gameState(player1, player2, scores)
                total_games += 1
                replay = input("Play another round? (y/n): ").lower()
                
                if replay != "y":
                    print(f"GAME SUMMARY ,Total Games Played : {total_games}")
                    print(f"{player1} WINS : {scores[player1]}")
                    print(f"{player2} WINS : {scores[player2]}")
                    break

        elif state_OfGame == "2":
            display_helpState()

        elif state_OfGame == "3":
            print("Thanks for playing! ")
            break

        else:
            print("Invalid menu choice. Please select 1, 2, or 3.")

TicTacGame()    


