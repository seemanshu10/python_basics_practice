class Animal:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} is created.")

class Dog(Animal):
    def __init__(self, name):
        super().__init__(name)   
        print("Dog is created.")


dog = Dog("Buddy")

print(dog.name)  

# Output:
# Animal Buddy is created.
# Dog is created.
# Buddy