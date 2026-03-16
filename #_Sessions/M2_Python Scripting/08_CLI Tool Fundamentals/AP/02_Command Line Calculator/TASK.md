## 🎯 AP. Command Line Calculator

### Task Objective

In this task, you will:
* Build a Python script that takes numbers and an operator from the command line.
* Use those inputs to perform a basic math operation (add, subtract, multiply, or divide).
* Handle cases where input is missing, the operator is invalid, or division by zero is attempted.
* Display the result or an appropriate error message.

### Instructions

* Create a script named `calculator.py`.
* Make the script accept three command line arguments: a number, an operator, and another number.
* Use `sys.argv` to read the values.
* Support only the four operators: `+`, `-`, `*`, and `/`.
* If the user gives fewer or more than three arguments, show an error.
* If the operator is not valid, show an error.
* If dividing by zero, show a message that division by zero is not allowed.
* Print the result if the operation is valid.

---

### Sample Output

```
# Valid operations
$ python calculator.py 5 + 3
Result: 8.0

$ python calculator.py 10 - 4
Result: 6.0

$ python calculator.py 7 * 2
Result: 14.0

$ python calculator.py 9 / 3
Result: 3.0
```

```
# Invalid operator
$ python calculator.py 5 & 3
Error: Invalid operator. Please use one of +, -, *, /.
```

```
# Division by zero
$ python calculator.py 5 / 0
Error: Division by zero is not allowed.
```

```
# Missing arguments
$ python calculator.py 5 +
Error: Please provide exactly three arguments: <number1> <operator> <number2>
```
