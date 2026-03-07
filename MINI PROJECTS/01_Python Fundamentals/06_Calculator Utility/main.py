
"""
Calculator Utility
Objective:
In this task, you will:
Learn to build a multi-utility terminal app that offers real-world conversion and calculation features.
Strengthen logic by working with conditions, arithmetic, string parsing, and user input without relying on built-in modules.
Instructions:
Create a terminal-based application that offers a menu of three major features:
Unit Converter
Basic Calculator
Statistics Analyzer
Main Menu
Show a main menu on program start:
Welcome to Smart Converter & Calculator Utility!
1. Unit Converter
2. Basic Calculator
3. Statistics Analyzer
4. Exit
Ask the user to select an option (1-4).
Unit Converter
Inside this section, display a second menu:
UNIT CONVERTER:
1. Celsius to Fahrenheit
2. Fahrenheit to Celsius
3. cm to inches
4. inches to cm
5. kg to pounds
6. pounds to kg
7. Back to Main Menu
Based on user choice, ask for the input value and show converted output.
Conversion formulas to use:
C to F: (c * 9/5) + 32
F to C: (f - 32) * 5/9
cm to inch: cm / 2.54
inch to cm: inch * 2.54
kg to lb: kg * 2.20462
lb to kg: lb / 2.20462
Basic Calculator
Display options:
BASIC CALCULATOR:
1. Add
2. Subtract
3. Multiply
4. Divide
5. Back to Main Menu
Ask user to enter two numbers.
Perform the selected operation and display the result.
Handle:
Division by zero
Invalid numeric input
Continue or go back to menu
Statistics Analyzer
Ask user to input a list of numbers, separated by comma or space.
Example input: 12, 34, 9, 56, 23
Show:
Total numbers
Sum of numbers
Average (sum / count)
Minimum value
Maximum value
Range (max - min)
Do not use built-in sum(), min(), or max() — implement the logic manually.

"""

# data statistical analyzer 
def statistical_analyzer():
    while True:
        
        data_input = input("\nEnter numbers separated by space or comma or type 'b' to go back: ")

        if data_input.lower() == "b":
            return
        
        data_input = data_input.replace(",", " ")
        list_ofNum = data_input.split()

        if not list_ofNum:
            print("No numbers entered.")
            continue

        numbers = []

        try:
            for item in list_ofNum:
                numbers.append(float(item))
        except ValueError:
            print("Invalid input. Please enter numbers only. not strings .")
            continue

        count = len(list_ofNum) # count of elemnets  in list 
        total = 0
        minimum = numbers[0]
        maximum = numbers[0]

        for num  in numbers:
            total += num        # total of number

            if num < minimum:   
                minimum = num   # minimum number find
            if num > maximum:
                maximum = num   # maximum number find 

        average = total / count
        data_range = maximum - minimum

        print("\nSTATISTICS:")
        print("Total numbers:", count)
        print("Sum:", total)
        print(f"Average: {average:.2f}")
        print("Minimum:", minimum)
        print("Maximum:", maximum)
        print("Range:", data_range)

# basic calculator for basic calculations  
def basicCalculator():
    while True:
        print("\nBASIC CALCULATOR:")
        print("\n1. Add")
        print("2. Subtract")
        print("3. Multiply")
        print("4. Divide")
        print("5. Back to Main Menu")

        basicChoice = input("Choose an option: ")

        # go to previous menu 
        if basicChoice == "5":
            return
        
        # checking if valid choice is not there 
        if basicChoice not in {"1", "2", "3", "4"}:
            print("Invalid choice! Please enter a number from 1 to 5.")
            continue
        
        # taking Two number inputs 
        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        if basicChoice == "1":
            print("Result:", num1 + num2)
        elif basicChoice == "2":
            print("Result:", num1 - num2)
        elif basicChoice == "3":
            print("Result:", num1 * num2)
        elif basicChoice == "4":
            try:
                division = num1/num2
                print("Result:", division)

            except ZeroDivisionError :
                print("Error: Division by zero is not allowed.")

        
# get a single input 
def get_number(value):
    while True:
        try:
            return float(input(value))
        except ValueError:
            print("Invalid input. Please enter a number.")

# Unit Converter 
def unitConverter():
    while True:

        print("\nUnit Converter Menu :")
        print("1. Celsius to Fahrenheit")
        print("2. Fahrenheit to Celsius")
        print("3. cm to inches")
        print("4. inches to cm")
        print("5. kg to pounds")
        print("6. pounds to kg")
        print("7. Back to Main Menu")

        choiceUnitMenu = input("Choose a conversion unit: ")
        
        if choiceUnitMenu == "7":
            return
        valueNumber = get_number("Enter number to convert: ")

        if choiceUnitMenu == "1":
            print(f"Result: {(valueNumber * 9/5) + 32}F")
        elif choiceUnitMenu == "2":
            print(f"Result: {(valueNumber - 32) * 5/9}C")
        elif choiceUnitMenu == "3":
            print(f"Result: {valueNumber / 2.54} inches" )
        elif choiceUnitMenu == "4":
            print(f"Result: {valueNumber * 2.54} cm")
        elif choiceUnitMenu == "5":
            print(f"Result: {valueNumber * 2.20462} pounds")
        elif choiceUnitMenu == "6":
            print(f"Result: {valueNumber / 2.20462} kg")
        else:
            print("Invalid choice ! . Only Enter the (1-7) . ")


# main title  display 
def calculatorMainTitle():
    title = " Smart Converter & Calculator Utility"
    print("="*60)
    print(title.center(60))
    print("="*60)

    print("\n1. Unit Converter")
    print("2. Basic Calculator")
    print("3. Statistics Analyzer")
    print("4. Exit")


# main calculator menu Call 
def MainCalculatorMenu():

    try:
        while True:
            # calculator main title 
            calculatorMainTitle()
            mainCalculatorMenu_choice = input("Select an option(1-4) :")

            if mainCalculatorMenu_choice == "1":
                unitConverter()
            elif mainCalculatorMenu_choice == "2":
                basicCalculator()
            elif mainCalculatorMenu_choice == "3":
                statistical_analyzer()
            elif mainCalculatorMenu_choice == "4":
                print("Goodbye! Close Calculator!")
                break
            else:
                print("Invalid Selection . Can only choose (1-4).")

    except KeyboardInterrupt:
        print("Exiting Cleanly! ")
        return

MainCalculatorMenu()

