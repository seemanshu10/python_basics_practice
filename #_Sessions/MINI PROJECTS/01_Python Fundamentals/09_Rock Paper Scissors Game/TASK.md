## **PA. Rock Paper Scissors Game**

### **Objective:**
* In this task, you will:
  * Learn how to structure interactive gameplay logic between a user and a computer opponent.
  * Practice decision-making using conditional checks to determine winners.
  * Explore how to improve user experience using emoji feedback and clear input/output handling.

### **Instructions:**
* Create a terminal-based Rock Paper Scissors game where the player competes against the computer.
* Do not use the `random` module. The computer will use a fixed, repeating pattern for its moves:
  `rock → paper → scissors → repeat`.
* **Game Setup**
  * Display a formatted welcome banner with emojis at the beginning.
  * Ask the user to enter their name.
  * Display the list of valid moves: `rock`, `paper`, `scissors`.
* **Game Flow**
  * For each round:
    * Ask the user to input their move.
    * The computer selects its move based on the repeating pattern.
    * Display both choices using emojis.
    * Determine the winner using standard rules:
      * Rock 🪨 beats Scissors ✂️
      * Scissors ✂️ beats Paper 📄
      * Paper 📄 beats Rock 🪨
    * Show round result using friendly messages:
      * Example:
        ```
        Alex chose ✂️   Computer chose 📄
        ✂️ beats 📄 → Alex wins this round!
        ```
* **Score Tracking**
  * Keep track of:
    * Total rounds played
    * Player wins
    * Computer wins
    * Draws
  * After each round, ask:
    ```
    Play another round? (yes/no):
    ```
* **Game End**
  * When the player chooses to stop:
    * Display a final game summary:
      * Total rounds
      * Wins and draws
      * Final winner or tie result
* Display appropriate error messages for:
  * Invalid move input
  * Unexpected choices (anything not in `rock/paper/scissors`)
  * Case sensitivity should be handled (e.g., `ROCK` and `Rock` should both work)


### **Sample Output:**
```
====================================
     🎮 Rock Paper Scissors Game 🎮
====================================

Enter your name: Alex
 Round 1 ---
Valid moves: rock, paper, scissors

Alex, enter your move: scissors

Alex chose ✂️   Computer chose 📄
✂️ beats 📄 → Alex wins this round!

Play another round? (yes/no): yes
 Round 2 ---
...
```