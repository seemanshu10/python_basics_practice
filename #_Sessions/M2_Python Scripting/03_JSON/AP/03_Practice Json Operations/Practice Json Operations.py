# Practice JSON Operations
import json
import os

EMPLOYEE_PATH = os.path.dirname(os.path.abspath(__file__))

personfile_path_Input = os.path.join(EMPLOYEE_PATH, "person.json")
personfile_path_Output = os.path.join(EMPLOYEE_PATH, "output.json")

try:
    # Load JSON Data
    with open(personfile_path_Input ,"r") as persons_file:
        persons = json.load(persons_file)

    # print(persons)
    
    # Access Simple Key-Value Pairs
    names=persons["name"]
    age=persons["age"]
    print(f"Names: {names}, Age: {age}")

    """
    Access Nested Objects
    Access "street" and "city" inside the "address" object.
    """
    streetName = persons["address"]["street"]
    cityName = persons["address"]["city"]

    print(f"Street: {streetName}, City: {cityName}")
    
    """
    Access Elements in an Array
    Access both elements in the "phoneNumbers" list.
    """
    phone_home = persons["phoneNumbers"][0]["number"]
    phone_work = persons["phoneNumbers"][1]["number"]

    print(f"Home Phone: {phone_home}, Work Phone: {phone_work}")

    """
    Modify JSON Data
    Change "age" to 31.
    Update the "city" in "address" to "New Wonderland".
    Append a new phone number object: {"type": "mobile", "number": "555-9876"}
    """

    persons["age"] = 31
    persons["address"]["city"] = "New Wonderland"
    persons["phoneNumbers"].append({"type": "mobile", "number": "555-9876"})

    # Add New Elements
    persons["email"] = "alice@example.com"
    persons["address"]["country"] = "Wonderland"

    with open(personfile_path_Output, "w") as Output_file:
        json.dump(persons, Output_file, indent=4)
    print("Modified data successfully saved to output.json")

except FileNotFoundError:
    print(f"Error :'{personfile_path_Input} doesn't exist'")

except json.JSONDecodeError as e:
    print(f"Json decode error: {e} ")