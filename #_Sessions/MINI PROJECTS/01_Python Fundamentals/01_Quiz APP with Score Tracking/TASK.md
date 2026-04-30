## **PA. Quiz Application with Score Tracking**

### **Objective:**
* In this task, you will:
  * Learn to build a user-driven question loop that reads data from an external file.
  * Understand how to evaluate responses and generate a detailed result report.
  * Practice structuring data flow between input and output files.

### **Instructions:**
* Create a terminal-based quiz application that reads questions from a file and saves a performance report to a new file.
* Use `with open()` for all file operations.
* Use a folder named `data` (must be created manually in the same directory as the script) to store all input/output files.
* **Question Bank (`questions.txt`)**
  * Store all MCQs in a single file named `questions.txt` in the `data` folder.
  * Each question block must include:
    * The question text
    * Four options (A, B, C, D)
    * Correct answer (just a letter like `A`)
  * Each block should be separated by an empty line.
  * Example:
    ```
    What is the capital of France?
    A. Berlin
    B. Madrid
    C. Paris
    D. Rome
    C
    ```
* **Quiz Flow**
  * Show a welcome banner at the start.
  * Read and parse questions one at a time from the file.
  * For each question:
    * Display the question and its options.
    * Ask the user to select one answer (A/B/C/D).
    * Compare with the correct answer and keep track of:
      * Total questions attempted
      * Number of correct answers
      * Number of incorrect answers
  * Show feedback after each question:
    * ✅ Correct!
    * ❌ Wrong! (Also show the correct answer)

* **Generate Score Report**
  * After completing the quiz, save a result summary to a file named `report_card.txt` in the `data` folder.
  * The report should include:
    * Total questions
    * Attempted questions (equal to total, as all are shown)
    * Correct answers
    * Wrong answers
    * Final score
    * Pass/Fail status based on score:
      * Score ≥ 50% → Pass
      * Score < 50% → Fail
* Display appropriate error messages for:
  * File not found or empty
  * Invalid input by the user
  * Malformed question blocks (missing lines)
- **Sample Questions File** --> Given in data/questions.txt


### **Sample Output (Terminal):**
```
========================================
     Welcome to the Quiz Challenge!
========================================

Q1: What is the capital of France?
A. Berlin
B. Madrid
C. Paris
D. Rome
Enter your answer (A/B/C/D): C
✅ Correct!

Q2: Which planet is known as the Red Planet?
A. Earth
B. Mars
C. Venus
D. Jupiter
Enter your answer (A/B/C/D): A
❌ Wrong! Correct answer was B

========================================
Quiz Completed!
Summary saved to: data/report_card.txt
```

### **Sample `report_card.txt` Output:**
```
Quiz Report Card---------------------
Total Questions   : 2
Correct Answers   : 1
Wrong Answers     : 1
Score             : 50%
Result            : Pass
```
