import os 
import json 

# print(__file__)
print(os.path.abspath(__file__))
print(os.path.dirname(os.path.abspath(__file__)))
# EMPLOYEE_PATH = os.path.dirname
EMPLOYEE_PATH = os.path.dirname(os.path.abspath(__file__))

employee_path_input = os.path.join(EMPLOYEE_PATH, "employee.json")
employee_path_output = os.path.join(EMPLOYEE_PATH, "department_salaries.json")

print(employee_path_input)
print(employee_path_output)

try:
    with open(employee_path_input, "r") as employee_file:
        employees = json.load(employee_file)
    
    # print(employees)

except FileNotFoundError:
    print(f"Error :'{employee_path_input} doesn't exist'")

except json.JSONDecodeError as e:
    print(f"Json decode error: {e} ")

department_totals = {}

print(employees)
for employee in employees:
    department = employee["department"]
    print(department)

    salary = employee["salary"]
    print(salary)

    # if new deartement add in key otherwise add the salary 
    if department in department_totals:
        department_totals[department] += salary
    else:
        department_totals[department] = salary

print(department_totals) 

try:
    with open(employee_path_output, "w") as output_file:
        json.dump(department_totals, output_file, indent = 4)

except FileNotFoundError:
    print(f"Error :'{employee_path_output} doesn't exist'")

except json.JSONDecodeError as e:
    print(f"Json decode error: {e} ")

print("Department Salary Totals calculated successfully")
print(f"Department salaries have been written to department_salaries.json .")