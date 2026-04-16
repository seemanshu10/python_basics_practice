class Animal:
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(f"{self.name} is eating.")

class Dog(Animal):  # Inherits from Animal
    def bark(self):
        print(f"{self.name} is barking.")

my_dog = Dog("Buddy")

my_dog.eat()   # From Animal
my_dog.bark()  # From Dog

# Output:
# Buddy is eating.
# Buddy is barking.