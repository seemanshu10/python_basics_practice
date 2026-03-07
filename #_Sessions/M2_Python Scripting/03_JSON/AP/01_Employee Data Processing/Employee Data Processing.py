# Employee Data Processing

import json

employeefile_path_Input = r"#_Sessions\M2_Python Scripting\03_JSON\AP\01_Employee Data Processing\employees.json"

employeefile_path_Output = r"#_Sessions\M2_Python Scripting\03_JSON\AP\01_Employee Data Processing\department_salaries.json"

try:
    with open(employeefile_path_Input ,"r") as employee_file:
        employees = json.load(employee_file)

    #print(employees)
    department_totals = {}

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        #print(department,salary)
        # if new department add in key otherwise add the salary 
        if department in department_totals:
            department_totals[department] += salary
        else:
            department_totals[department] = salary
    
    # dumping data in json output file 
    with open(employeefile_path_Output,"w") as output_file:
        json.dump(department_totals,output_file,indent=4)
        
    print("Department Salary Totals calculated successfully")
    print(f"Results saved to {employeefile_path_Output} .")

except FileNotFoundError:
    print(f"Error :'{employeefile_path_Input} doesn't exist'")

except json.JSONDecodeError as e:
    print(f"Json decode error: {e} ")