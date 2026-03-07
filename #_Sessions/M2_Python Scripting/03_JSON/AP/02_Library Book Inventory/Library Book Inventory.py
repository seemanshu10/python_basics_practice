# Library Book Inventory

import json

authorfile_path_Input = r"#_Sessions\M2_Python Scripting\03_JSON\AP\02_Library Book Inventory\books.json"

authorfile_path_Output = r"#_Sessions\M2_Python Scripting\03_JSON\AP\02_Library Book Inventory\author_inventory.json"

try:
    with open(authorfile_path_Input ,"r") as employee_file:
        authorData = json.load(employee_file)

    #print(authorData)
    author_totals = {}

    for author in authorData:
        authorName = author["author"]
        quantity_number = author["quantity"]

        # if new department add in key otherwise add the salary 
        if authorName in author_totals:
            author_totals[authorName] += quantity_number
        else:
            author_totals[authorName] = quantity_number
    
    # dumping data in json output file 
    with open(authorfile_path_Output,"w") as output_file:
        json.dump(author_totals,output_file,indent=4)
        
    print("Department Salary Totals calculated successfully")
    print(f"Results saved to {authorfile_path_Output} .")

except FileNotFoundError:
    print(f"Error :'{authorfile_path_Input} doesn't exist'")

except json.JSONDecodeError as e:
    print(f"Json decode error: {e} ")