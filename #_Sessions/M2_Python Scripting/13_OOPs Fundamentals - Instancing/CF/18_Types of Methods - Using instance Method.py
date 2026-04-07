class Person:
    def __init__(self, name, age):
        self.name = name  # Instance attribute
        self.age = age    # Instance attribute

    def introduce(self):  # Instance method
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")


person1 = Person("Alice", 25)
person2 = Person("Bob", 30)

person1.introduce()
person2.introduce()
