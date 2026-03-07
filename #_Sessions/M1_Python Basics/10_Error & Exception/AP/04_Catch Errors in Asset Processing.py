"""
Task Description
In this task, you will implement a script that processes VFX asset attributes such as name, resolution, and file path.  
Your task is to ensure that incorrect operations on asset attributes do not cause a crash.
Your script should:
• Retrieve asset details from a predefined dictionary.  
• Ensure valid string operations on asset names.  
• Handle cases where an invalid operation is performed on asset attributes, causing a TypeError.  
• Handle cases where the user tries to access a missing key, causing a KeyError.

🛠 Instructions
• Use a predefined dictionary of VFX asset attributes.  
• Retrieve the name and resolution of an asset.  
• Ensure that a string operation is valid (avoid incorrect method calls).  
• Handle the following exceptions:
  - TypeError: If an invalid operation is performed on an asset attribute.
  - KeyError: If an invalid key is accessed in the dictionary.
  - KeyboardInterrupt: Allow the user to exit safely.

🧪 Expected Output (User Input Scenarios)

✅ Valid Input  
Enter asset key (spaceship/explosion): spaceship  
Asset Name (Uppercase): SPACESHIP_MODEL_01  
Error: Invalid operation performed on an asset attribute.

❌ Invalid Asset Key (KeyError Handling)  
Enter asset key (spaceship/explosion): dragon  
Error: Invalid asset key. Please enter a valid key.

❌ TypeError Handling (Invalid Operation on String)  
(The .append() operation on a string should fail.)  
Error: Invalid operation performed on an asset attribute.

❌ User Interrupts (Ctrl+C)  
Enter asset key (spaceship/explosion): ^C  
Process interrupted by user. Exiting...
"""


asset_details = {
    'spaceship':{
        'name':'SpaceShipModel01',
        'file-size':'2.2GB',
        'resolution': (2048, 2048),
        'file_path': '/assets/vfx/SpaceShipModel01.exr'
    },
    'explosion':{
        'name':'Fire_ExplosionV1',
        'file-size':'2.7GB',
        'resolution':(4096, 4096),
        'file_path': '/assets/vfx/Fire_Explosion.exr'
    }

}

try:
    assetKey = input("Enter asset name(spaceship/explosion): ") 

    assetName = asset_details[assetKey]
    #print(assetName)
    try:
        # retrive asser attrributes 
        name = assetName['name']
        resolution = assetName['resolution']

        print("Asset Name in UpperCase: ",name.upper())
        print(resolution + "2048")
        # error as resolution is tuple cannot run upper
    except TypeError:
        print("Error : Invalid Operation performed .")

except KeyError:
    print("Enter The correct asset Name. Asset Not found in data.")
except KeyboardInterrupt:
    print("\nProgram Interupted. Exiting Cleanly")

"""
Enter asset name(spaceship/explosion): 
Program Interupted. Exiting Cleanly

Asset Name in UpperCase:  SPACESHIPMODEL01
Error : Invalid Operation performed .


Enter asset name(spaceship/explosion): psasa
Enter The correct asset Name. Asset Not found in data.
"""
