class Pet:

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def info(self):
        print(f"This is {self.name}, aged {self.age}.")

class Dog(Pet):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def info(self):
        super().info()
        print(f"{self.name} is a {self.breed}.")

class Cat(Pet):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color
    def info(self):
        super().info()
        print(f"{self.name} has a {self.color} coat.")

dog = Dog("Buddy", 3, "Golden Retriver")
dog.info()

cat = Cat("Luna", 2, "black")
cat.info()

"""
This is Buddy, aged 3.
Buddy is a Golden Retriver.
This is Luna, aged 2.
Luna has a black coat.
"""