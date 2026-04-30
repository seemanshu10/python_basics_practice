## **PA. Calculator Utility**


### **Objective:**

* In this task, you will:
  * Learn to build a multi-utility terminal app that offers real-world conversion and calculation features.
  * Strengthen logic by working with conditions, arithmetic, string parsing, and user input without relying on built-in modules.

### **Instructions:**
* Create a terminal-based application that offers a menu of three major features:
  * **Unit Converter**
  * **Basic Calculator**
  * **Statistics Analyzer**
#### **Main Menu**
* Show a main menu on program start:
  ```
  Welcome to Smart Converter & Calculator Utility!
  1. Unit Converter
  2. Basic Calculator
  3. Statistics Analyzer
  4. Exit
  ```
* Ask the user to select an option (1–4).

#### **Unit Converter**
* Inside this section, display a second menu:
  ```
  UNIT CONVERTER:
  1. Celsius to Fahrenheit
  2. Fahrenheit to Celsius
  3. cm to inches
  4. inches to cm
  5. kg to pounds
  6. pounds to kg
  7. Back to Main Menu
  ```
* Based on user choice, ask for the input value and show converted output.
* **Conversion formulas** to use:
  * C to F: `(c * 9/5) + 32`
  * F to C: `(f - 32) * 5/9`
  * cm to inch: `cm / 2.54`
  * inch to cm: `inch * 2.54`
  * kg to lb: `kg * 2.20462`
  * lb to kg: `lb / 2.20462`

#### **Basic Calculator**
* Display options:
  ```
  BASIC CALCULATOR:
  1. Add
  2. Subtract
  3. Multiply
  4. Divide
  5. Back to Main Menu
  ```
* Ask user to enter two numbers.
* Perform the selected operation and display the result.
* Handle:
  * Division by zero
  * Invalid numeric input
  * Continue or go back to menu

#### **Statistics Analyzer**
* Ask user to input a list of numbers, separated by comma or space.
* Example input: `12, 34, 9, 56, 23`
* Show:
  * Total numbers
  * Sum of numbers
  * Average (sum / count)
  * Minimum value
  * Maximum value
  * Range (max - min)
* Do not use built-in `sum()`, `min()`, or `max()` — implement the logic manually.

#### Additional Notes
* Use only core Python features (no `math`, `random`, or external libraries).
* Validate user inputs and handle errors clearly.
* Format output with clear headings, spacing, and separators for readability.
* Use functions for each feature to keep code modular and maintainable.


### Sample Output Snippet:
```
=======================================
  Smart Converter & Calculator Utility
=======================================

1. Unit Converter
2. Basic Calculator
3. Statistics Analyzer
4. Exit

Enter your choice: 1
 UNIT CONVERTER ---
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
...

Enter your choice: 1
Enter temperature in Celsius: 100
Result: 100°C = 212.0°F

Do you want to convert again? (yes/no):
```


