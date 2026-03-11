# Employee Data Processing
import os 
import json

EMPLOYEE_PATH = os.path.dirname(os.path.abspath(__file__))
# weather_json_file_path = os.path.join(EMPLOYEE_PATH, "employees.json") 
# print(weather_json_file_path)
employeefile_path_Input = os.path.join(EMPLOYEE_PATH, "employees.json")
employeefile_path_Output = os.path.join(EMPLOYEE_PATH, "department_salaries.json")

try:
    with open(employeefile_path_Input ,"r") as employee_file:
        employees = json.load(employee_file)

    #print(employees)
    department_totals = {}

    for employee in employees:
        department = employee["department"]
        salary = employee["salary"]

        # print(department,salary)
        # if new department add in key otherwise add the salary 
        if department in department_totals:
            department_totals[department] += salary
        else:
            department_totals[department] = salary
    
    # dumping data in json output file 
    with open(employeefile_path_Output,"w") as output_file:
        json.dump(department_totals,output_file,indent=4)
        
    print("Department Salary Totals calculated successfully")
    print(f"Department salaries have been written to department_salaries.json .")

except FileNotFoundError:
    print(f"Error :'{employeefile_path_Input} doesn't exist'")

except json.JSONDecodeError as e:
    print(f"Json decode error: {e} ")