class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} is created.")

class Dog(Animal):
    def __init__(self, name):
        print("Dog is created.")  

dog = Dog("Buddy")

print(dog.name)  

# Output:
# Dog is created.

# Traceback (most recent call last):
#   File "c:\Users\pralhad\Desktop\project\script.py", line 12, in <module>
#     print(dog.name)  
# AttributeError: 'Dog' object has no attribute 'name'