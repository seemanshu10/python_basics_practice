class Employee:
    def work(self):
        print("The Employee is working.")

class Developer(Employee):
    def work(self):
        super().work()

        print("The Employee os Coding.")

employee = Employee()
employee.work()

developer = Developer()
developer.work()

"""
The Employee is working.
The Employee is working.
The Employee os Coding.
"""