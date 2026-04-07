class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


person1 = Person("Alice", 25)


print("Before birthday:", person1.age)  # Output: 25

person1.age = 26

print("After birthday:", person1.age)  # Output: 26