class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

person1 = Person("Alice", 25, "New York")
person2 = Person("Bob", 30, "Los Angeles")

print(f"Name: {person1.name}, Age: {person1.age}, City: {person1.city}")
print(f"Name: {person2.name}, Age: {person2.age}, City: {person2.city}")