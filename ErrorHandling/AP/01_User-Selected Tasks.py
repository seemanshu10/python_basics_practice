"""
Task Objective
Create a command-line utility where the user can select a task from a menu (e.g., math operations).
Dynamically call the selected function using a dictionary of callable functions.
Implement exception handling for:
• KeyError if the user selects a task that doesn’t exist.
• TypeError if the function signature is incorrect or used improperly.
• NameError for misreferenced or undefined callables.
• KeyboardInterrupt for clean interruption handling.

🛠 Instructions
• Define at least 3 simple functions (e.g., square, increment, negate) that accept a single number and return a result.
• Store these functions in a dictionary with a string key (e.g., 'square': square).
• Prompt the user to enter:
  - A function name to call (key from the dictionary).
  - A number to pass into that function.
• Use exception handling to:
  - Catch invalid function names (KeyError).
  - Handle passing the wrong input type or number of arguments (TypeError).
  - Guard against undefined function references (NameError).
  - Catch KeyboardInterrupt to exit cleanly.


"""
# Square function
def square(number):
    return number**2

# increment by 1 
def increment(number):
    return number + 1

# neagte by 1 
def negate(number):
    return -number

# crating all functions dixtionary 
operation_functions = {
    'square': square ,
    'increment': increment ,
    'negate': negate
}

def funtionCall():
    try:
        # user input 
        function_name = input("Enter the operation to perform (square,increment,negate)")

        # check if function exist in dictionary 
        functionType = operation_functions[function_name]

        index_value = float(input("Enter a number:"))

        # call the function pas value of number to it as argument 
        result = functionType(index_value)
        print(f"Result is: {result}")

    except TypeError:
        print("Error: Wrong Input Type. Input Integer !")
    except NameError:
        print("Error: Function name not defined !")
    except KeyboardInterrupt:
        print("Error: Program interupetd . Exiting .. !")
    except ValueError:
        print("Error : Enter a valid number . ")
    except KeyError:
        print("Error: Invalid Function Entered.")

funtionCall()

"""
Enter the operation to perform (square,increment,negate)square
Enter a number:5
Result is: 25.0

Enter the operation to perform (square,increment,negate)neg
Error: Invalid Function Entered.

Enter the operation to perform (square,increment,negate)increment
Enter a number:a
Error : Enter a valid number . 

Enter the operation to perform (square,increment,negate)negate
Enter a number:Error: Program interupetd . Exiting .. !

Enter the operation to perform (square,increment,negate)multiply
Error: Invalid Function Entered.

"""