## **PA. Battleship Lite**

### **Objective:**
* In this task, you will:
  * Learn how to design a grid-based game using lists and coordinate systems.
  * Practice handling user input for position-based logic.
  * Strengthen your ability to manage game state and validate win conditions.

### **Instructions:**
* Create a **terminal-based Battleship game** between a single player and the computer.
* The game board should be a **5×5 grid**.
* The computer’s ship locations will be **predefined** (no `random` module is allowed).
* The player must guess coordinates to "hit" ships.
* The goal is to **sink all enemy ships**.
* **Game Setup**
  * Display a welcome screen and game title.
  * Show an empty grid (e.g., `-` for unguessed positions).
  * Use a 5x5 grid with coordinates ranging from (0,0) to (4,4).
* **Computer's Ship Placement**
  * Predefine 3 ship positions in the code:
    * Each ship occupies **1 cell**
    * Example: `[(1,1), (2,3), (4,0)]`
* **Gameplay Loop**
  * Ask the player to enter a target coordinate (row and column).
  * Validate input:
    * Must be numbers
    * Must be within the 0–4 range
    * Must not be a previously guessed location
  * Update the board after each guess:
    * `X` for hit
    * `O` for miss
  * Display updated board after every turn.
  * Track total hits and guesses.
* **Game End**
  * Once all 3 ships are hit:
    * Display victory message
    * Show number of total guesses
    * Optionally ask if the user wants to replay (optional)
* Display appropriate error messages for:
  * Invalid input types
  * Out-of-range coordinates
  * Repeated guesses

### **Sample Output:**
```
========================================
       🚢 Battleship Lite - Terminal
========================================

5x5 Grid Initialized. Enemy ships hidden!

  0 1 2 3 4
0 - - - - -
1 - - - - -
2 - - - - -
3 - - - - -
4 - - - - -

Enter row (0-4): 2
Enter column (0-4): 3
💥 Hit!

  0 1 2 3 4
0 - - - - -
1 - - - - -
2 - - - X -
3 - - - - -
4 - - - - -

Hits: 1 | Misses: 0 | Total Guesses: 1

...

Enter row (0-4): 1  
Enter column (0-4): 1  
💥 Hit!

  0 1 2 3 4
0 - - - - -
1 - X - - -
2 - - - X -
3 - - - - -
4 - - - - -

Hits: 2 | Misses: 0 | Total Guesses: 2

...

Enter row (0-4): 4  
Enter column (0-4): 0  
💥 Hit!

  0 1 2 3 4
0 - - - - -
1 - X - - -
2 - - - X -
3 - - - - -
4 X - - - -

Hits: 3 | Misses: 0 | Total Guesses: 3

🎉 Congratulations!  
You sank all ships in 3 guesses.

```
