class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id
    
    def display_info(self):
        print(f"Employee Name: {self.name}, ID {self.employee_id}")

class Manager(Employee):
    def assign_task(self):
        print(f"Manager {self.name} is assigning tasks. ")

manager= Manager("Alice", 101)

manager.display_info()
manager.assign_task()

"""
Employee Name: Alice, ID 101
Manager Alice is assigning tasks. 
"""