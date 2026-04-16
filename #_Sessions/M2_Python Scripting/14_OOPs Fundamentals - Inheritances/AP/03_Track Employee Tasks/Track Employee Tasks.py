# Track Employee Tasks
class Employee:
    def __init__(self, name, employee_id):
        self.name = name
        self.employee_id = employee_id

    def assign_task(self):
        print("Employee is assigned task.")

class Manager(Employee):
    def __init__(self, name, employee_id):
        super().__init__(name, employee_id)

    def assign_task(self):
        super().assign_task()
        print("Manager is delegating tasks.")

employee1 = Employee("Alice", 101)
manager1 = Manager("Bob", 102)

employee1.assign_task()
manager1.assign_task()