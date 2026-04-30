## **PA. Tic Tac Toe Game**

### **Objective:**
* In this task, you will:
  * Learn how to design and manage turn-based logic between two players.
  * Understand how to use functions to structure gameplay and handle winning conditions.
  * Practice capturing user input and managing game state using a list-based board system.

### **Instructions:**
* Create a terminal-based Tic Tac Toe game for two players.
* Display a main menu that allows the user to:
  * Start a new game
  * View help instructions
  * Exit the program
* **Help Menu**
  * Display the board layout with positions (1–9).
  * Briefly explain the rules:
    * Player 1 uses **X**
    * Player 2 uses **O**
    * First to get 3 in a row wins (horizontal, vertical, or diagonal)
* **Game Flow**
  * Ask for Player 1 and Player 2 names.
  * Display the board using the correct layout after each move.
  * Alternate turns between Player 1 and Player 2.
  * Prompt the player to enter a position (1–9).
  * Validate input:
    * Input must be a number between 1 and 9
    * Position must not already be taken
  * Update the board with the appropriate mark (X or O).
  * After each move, check:
    * If the current player has won
    * If the game is a draw
* **Winning & Replay**
  * If a player wins, display a message with their name.
  * Keep track of how many rounds each player wins.
  * Ask the user if they want to **replay** or **quit** after each round.
  * On quit, display a summary of total wins for both players.
* Display appropriate error messages for:
  * Invalid menu choice
  * Invalid board positions
  * Non-integer or unexpected input


### **Sample Output:**
```
WELCOME TO TIC TAC TOE
1. New Game
2. Get Help
3. Exit
Enter your choice (1-3): 2

HOW TO PLAY TIC TAC TOE

Board positions:
1 | 2 | 3
--+---+--
4 | 5 | 6
--+---+--
7 | 8 | 9

Rules:
- Player 1 uses X
- Player 2 uses O
- First to get 3 in a row wins

WELCOME TO TIC TAC TOE
1. New Game
2. Get Help
3. Exit
Enter your choice (1-3): 1

Enter Player 1 name: Alice
Enter Player 2 name: Bob

  |   |  
--+---+--
  |   |  
--+---+--
  |   |  

Alice enter position (1-9): 5

  |   |  
--+---+--
  | X |  
--+---+--
  |   |  

Bob enter position (1-9): 1

  |   |  
--+---+--
O | X |  
--+---+--
  |   |  

...
Bob wins this round!

Replay or Quit? (replay/quit): quit

GAME SUMMARY
Alice wins: 0
Bob wins: 1

```