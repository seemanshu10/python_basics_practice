while True:

    try:
        value = int(input("Enter a number: "))
        result = 10 / value
        print("Result:", result)
        
        
        with open("read_only_file.txt","r") as file:
            content  = file.read()
            print(content)

    
    except ValueError:
        print("Please enter a valid integer.")

    except ZeroDivisionError:
        print("Cannot Divide by zero.")