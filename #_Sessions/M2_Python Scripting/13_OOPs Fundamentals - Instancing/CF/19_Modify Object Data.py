class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def introduce(self):
        print(f"Hi, my name is {self.name} and I am {self.age} years old.")

    def have_birthday(self):  # Modifies object state
        self.age += 1
        print(f"Happy Birthday, {self.name}! You are now {self.age} years old.")


person = Person("Charlie", 29)

person.introduce()
person.have_birthday()
person.introduce()