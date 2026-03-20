import sys 
import random
import string

def generate_password(length_of_password, use_uppercase, use_numbers, use_special):
    
    """
    Generate a random password with user given character types.
    The password will always contain lowercase letters as mentioned . Optionally, it can include
    uppercase letters, digits, and special characters. 

    Parameters:
    length_of_password : int
        The total length of the password to generate. Must be greater than zero.
    use_uppercase : bool
        If True, include uppercase letter (A-Z) in the pasword.
    use_numbers : bool
        If True,include digits(0-9) in the password.
    use_special : bool
        If True, include special characters (!@#$%^&*) in the password.

    returns: str
        A randomly generated password string .
    """

    # contains all the set of characters 
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    numbers = string.digits 
    special = string.punctuation
    
    #added the lowercaase to char_pool 
    char_pool = list(lowercase)
    # print(char_pool)
    required_chars = []

    if use_uppercase:
        char_pool.extend(uppercase)

    if use_numbers:
        char_pool.extend(numbers)
        
    if use_special:
        char_pool.extend(special)

    
    # password_chars = required_chars + [random.choice(char_pool) for _ in range(length_of_password)]
    for i in range(length_of_password):
        random_character = random.choice(char_pool)
        required_chars.append(random_character)

    return "".join(required_chars)

def main():
    
    arguments = sys.argv[1:]
    
    length_of_password = 8
    use_uppercase = False
    use_numbers = False
    use_special = False
    if len(arguments) > 0:
        try:
            length_of_password = int(arguments[0])
            options = arguments[1:]
        except ValueError:
            print("Error: First argument must be password length.")
            sys.exit(1)
    else:
        options = []

    for opt in options:
        if opt.lower() == "--uppercase":
            use_uppercase = True
        elif opt.lower() == "--numbers":
            use_numbers = True
        elif opt.lower() == "--special":
            use_special = True
        else:
            print(f"Unknown option: {opt}")
            sys.exit(1)
    
    new_password = generate_password(length_of_password, use_uppercase, use_numbers, use_special)
    print(new_password)
    
if __name__ == "__main__":
    main()

"""
python .\password_generator_flag.py 12 --numbers --special --uppercase
3?dhMoV#PxzT

python .\password_generator_flag.py  --numbers --special --uppercase      
Error: First argument must be password length.

 python .\password_generator_flag.py  12                                   
ppssntqurfdr
"""