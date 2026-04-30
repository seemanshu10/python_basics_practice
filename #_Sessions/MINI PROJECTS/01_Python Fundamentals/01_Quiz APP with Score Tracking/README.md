# **Quiz Application with Score Tracking**

## **Description**
User-driven question loop that reads data from an external file. Displays question and waits for user input for the answer . And based on the the user answer give out the report for the quiz . 


##  Features
- Store all MCQs in a single file named `questions.txt` in the `data` folder.
- Each question block must include:
  1. The question text
  2. Four options (A, B, C, D)
  3. Correct answer (just a letter like `A`)

## **Quiz Flow**

- Welcome banner at the start.
- Read and parse questions one at a time from the file.
- For each question:
  1. Total questions attempted
  2. Number of correct answers
  3. Number of incorrect answers
- Show feedback after each question:
    - ✅ Correct!
    - ❌ Wrong! (Also show the correct answer)


## Requirements
- Python 3.10 or higher  

---

##  Installation
1. Clone the repository:
   ```
   git clone https://github.com/seemanshu10/python_basics_practice.git
   ```

2. Clone the repository on project folder. 


### Folder Structure

```
Quiz APP with Score Tracking/
├── data/
│   ├── questions.txt
│   └── report_card.txt
├── main.py
├── README.md
```

## Usage
1. Place files inside the folder where the project needs to be stored . 
2. Can Do git clone on the or download from the github manually through the above github link . 
3. Open the project folder in the vscode or any other editor .
4. Run the Python script main.py

### Generate Score Report

---

- After completing the quiz, save a result summary to a file named `report_card.txt` in the `data` folder.
- The report include:
  - Total questions
  - Attempted questions (equal to total, as all are shown)
  - Correct answers
  - Wrong answers
  - Final score
  - Pass/Fail status based on score:
    1. Score ≥ 50% → Pass
    2. Score < 50% → Fail
- **Sample Questions File** --> Given in `data/questions.txt`
- **Sample Reports File** --> Given in `data/report_card.txt`

### **Sample Output (Terminal):**

```
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

###  License:
---

> This project is under MIT license 