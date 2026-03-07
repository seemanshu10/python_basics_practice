"""
Task Description

In this task, you will create a user input validation system for an asset management tool used in a VFX pipeline.  
The tool requires users to input Asset IDs (which must be integers) and Asset Names (which must be non-empty strings).  
Your implementation should prevent crashes due to incorrect input by handling exceptions appropriately.

You will implement the following exception handling:
• ValueError: Raised when the user enters a non-integer for Asset ID.  
• AttributeError: Raised when the user enters an empty Asset Name.  
• NameError: Handled in case an undefined variable is accessed.  
• KeyboardInterrupt: Ensures the program exits gracefully if the user manually stops execution (e.g., pressing Ctrl+C).
Your program should continue prompting the user until they enter valid data, providing clear error messages when an exception occurs.

🛠 Instructions
• Implement a function to prompt for an Asset ID, ensuring that only integer values are accepted.  
• Implement another function to prompt for an Asset Name, ensuring it is a non-empty string.  
• Use try and except blocks to handle potential errors and guide the user to enter correct input.  
• Ensure that if a user interrupts the program (KeyboardInterrupt), it exits gracefully.  
• Once valid input is received, display a message confirming successful asset entry.

🧪 Expected Output (User Input Scenarios)

✅ Valid Input  
Enter Asset ID (integer only): 101  
Enter Asset Name (non-empty string): Spaceship_Model_01  
Successfully added asset: ID 101, Name 'Spaceship_Model_01'

❌ Invalid Asset ID (String Instead of Integer)  
Enter Asset ID (integer only): abc  
Error: Asset ID must be an integer. Please try again.  
Enter Asset ID (integer only): 42

❌ Invalid Asset Name (Empty String)  
Enter Asset Name (non-empty string):   
Error: Asset Name cannot be empty.  
Enter Asset Name (non-empty string): Explosion_Effect

❌ User Interrupts (Ctrl+C)  
Enter Asset ID (integer only): ^C  
Process interrupted by user. Exiting...
"""


def assetID():
    """
    user input for Asset ID 
    Must be integer . keeps asking until correct input entered 

    """

    while True:
        try:
            # keeps asking input until correct is entered 
            asset_id = int(input("Enter AssetID(integer): "))
            return asset_id
        except ValueError:
            print("Error: Asset ID must be an integer. Please Try Again!")
        except KeyboardInterrupt:
            print("\nProgram interupted.Exiting Cleanly.")
            break #  exit 

def assetName():
    """
    user Input for an Asset Name.
    Must be a non-empty string. Keeps asking until valid input is received.

    """
    while True:
        try:
            # keeps asking input until correct is entered 
            asset_Name = input("Enter AssetName(non_empty string): ")
            
            if asset_Name.strip() == "":
                print("Asset Name cannot be empty")
            else:
                return asset_Name
        except AttributeError:
            print("Asset Name cannot be empty ! Enter A valid name. ")
        except KeyboardInterrupt:
            print("\nProgram interupted.Exiting Cleanly.")
            break #  exit 

def assetDetails():
    try:
        asset_id = assetID()
        asset_name = assetName()

        print("\nAsset Successfully registered!")
        print(f"Asset ID: {asset_id}")
        print(f"Asset Name: {asset_name}")

    except KeyboardInterrupt:
        print("Shutdown compolete. GoodBye.")

assetDetails()

"""

Asset Successfully registered!
Asset ID: 223
Asset Name: FX001

"""