# Creating a Colorful Menu with Colorama

from colorama import init, Fore , Style

# reset to default after every print 
init(autoreset=True)

# menu display with different colors 
print(Fore.RED + Style.BRIGHT + "1. Red Message")
print(Fore.GREEN + Style.BRIGHT + "2. Green Message") 
print(Fore.YELLOW + Style.BRIGHT + "3. Yellow Message") 
print(Fore.BLUE+ Style.BRIGHT + "4. Blue Message") 
print(Style.BRIGHT + "5. Exit") 


while True:
    
    user_choice = input("Please select an option (1-5): ")
    
    
    if user_choice == "1":
        print(Fore.RED + Style.BRIGHT + "You have selected the Red Message.")

    elif user_choice == "2":
        print(Fore.GREEN + Style.BRIGHT + "You have selected the Green Message.")

    elif user_choice == "3":
        print(Fore.YELLOW + Style.BRIGHT + "You have selected the Yellow Message.")

    elif user_choice == "4":
        print(Fore.BLUE + Style.BRIGHT + "You have selected the Blue Message.")

    elif user_choice == "5":
        print("Exiting the program. Goodbye!")
        break

    else:
        print("Invalid User Input ")
        
