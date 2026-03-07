"""
Task Description
In this task, you will create a script that manages a list of VFX assets.  
The script will allow users to:
• Retrieve an asset from a predefined list of assets using an index.  
• Handle cases where the user enters an invalid index, which would normally cause an IndexError.  
• Handle cases where a variable is not defined properly, which would lead to a NameError.  
• Ensure the program does not crash and instead displays appropriate error messages.

🛠 Instructions
• Use a list of predefined VFX assets.  
• Prompt the user to enter an index to retrieve an asset.  
• Handle the following exceptions:
  - IndexError: If the user enters an out-of-range index.
  - NameError: If an undefined variable is used.
  - KeyboardInterrupt: If the user manually stops execution.
  - ValueError: For non-integer input.
• Ensure the user can re-enter a valid input when an exception occurs.

🧪 Expected Output (User Input Scenarios)

✅ Valid Input  
Enter asset index (0-4): 2  
Selected Asset: Smoke Simulation

❌ Invalid Index (IndexError Handling)  
Enter asset index (0-4): 5  
Error: Invalid index. Please enter a number within the valid range.

❌ Non-Integer Input (ValueError Handling)  
Enter asset index (0-4): abc  
Error: Please enter a valid integer index.

❌ User Interrupts (Ctrl+C)  
Enter asset index (0-4): ^C  
Process interrupted by user. Exiting...
"""


assetList = ['Smoke Simulation','Water FX','Fire Simulation','CharacterMain']

while True:
        try:
            assetIndex = input("\nEnter an index to retrieve an asset: ")
            index = int(assetIndex)  # may raise ValueError

            asset = assetList[index]  # may raise IndexError
            print(f"\nRetrieved Asset: {asset}")

            break  # exit loop after successful retrieval

        except ValueError:
            print("Error: Please enter a valid integer index.")

        except IndexError:
            print("Error: Index out of range. Please select a valid asset index.")

        except KeyboardInterrupt:
            print("\nProgram interrupted. Exiting cleanly.")
            break


while True:
    
    try:
        asset_name = input("\nEnter an Asset Name: ")

        # Mistake: using the wrong variable name
        print(f"You selected: {asset_name}")  # NameError here

        break

    # name error occurs as assetANme is not defined a typo 
    except NameError:
        print("Error: Asset name variable is not defined. Please try again.")

    except KeyboardInterrupt:
        print("\nProgram interrupted. Exiting cleanly.")
        break

"""
Enter an index to retrieve an asset: 2

Retrieved Asset: Fire Simulation

Enter an index to retrieve an asset: 5
Error: Index out of range. Please select a valid asset index.

Enter an index to retrieve an asset: a
Error: Please enter a valid integer index.

Enter an index to retrieve an asset:
Program interrupted. Exiting cleanly.
"""