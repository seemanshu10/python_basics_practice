class Person:
    def __init__(self, name, age):
        self.name = name    # instance attribute
        self.age = age      # instance attribute

person1 = Person("Alice", 25)

print(f"Name: {person1.name}, Age: {person1.age}")
# Name: Alice, Age: 25