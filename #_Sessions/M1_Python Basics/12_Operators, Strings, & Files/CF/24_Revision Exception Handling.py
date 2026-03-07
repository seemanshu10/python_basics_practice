try:
    # Simple try-except
    num = int(input("Enter a number: "))
    print("You entered:", num)

    
    # Multiple try-except
    x = int(input("\nEnter numerator: "))
    y = int(input("Enter denominator: "))
    
    result = x / y
    print("Result:", result)
    

    # Catching all exceptions
    val = int(input("\nEnter a number for all-exception demo: "))
    print("Value entered:", val)
    

except ValueError:
    print("Invalid input! Please enter numbers only.")
    

except ZeroDivisionError:
    print("Cannot divide by zero!")
    

except Exception as e:
    print("Something went wrong:", e)
