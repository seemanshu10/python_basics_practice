## **PA. Code Breaker**

### **Objective:**
* In this task, you will:
  * Learn to create a multi-step guessing game that compares player input to a secret code.
  * Strengthen your ability to break down logic for position-based matching.
  * Practice iterating through lists and applying conditional checks for feedback.

### **Instructions:**
* Create a terminal-based **code guessing game**, where the player tries to break a 4-digit secret code.
* Do not use the `random` module — use a **fixed secret code** (e.g., `["3", "1", "4", "2"]`) stored in a list.
* The player gets **limited attempts (e.g., 8 tries)** to guess the correct code.
* Accept guesses as a **4-digit number**, and validate:
  * Must be exactly 4 digits
  * All characters must be numbers
* After each guess:
  * Compare each digit with the secret code
  * Provide feedback for each digit:
    * **Correct digit and correct position** → `"✔"`
    * **Correct digit but wrong position** → `"→"`
    * **Digit not in the code** → `"✖"`
* **Feedback Example:**
  ```
  Secret Code: [3, 1, 4, 2]
  Player Guess: 3 4 2 8
  Feedback    : ✔ → → ✖
  ```
* If the player guesses all 4 digits in the correct positions, show a success message and stop the game.
* If the player uses all attempts without breaking the code, reveal the correct code and show a failure message.
* Track and show the number of attempts used.
* Display appropriate error messages for:
  * Invalid input (non-digit characters, wrong length)

### **Sample Output:**
```
========================================
         🧠 Welcome to Code Breaker
========================================

Guess the 4-digit secret code!
You have 8 attempts.

Enter guess 1: 3428
Feedback     : ✔ → → ✖

Enter guess 2: 3142
Feedback     : ✔ ✔ ✔ ✔

🎉 Code cracked in 2 attempts!
```
