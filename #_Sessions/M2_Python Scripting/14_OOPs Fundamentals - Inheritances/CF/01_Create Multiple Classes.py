class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"My name is {self.name}, and I am {self.age} years old.")
        
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"This is a {self.brand} {self.model}.")


person1 = Person("Alice", 25)
car1 = Car("Toyota", "Corolla")

person1.introduce()  # My name is Alice, and I am 25 years old.
car1.display_info()  # This is a Toyota Corolla.