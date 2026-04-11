class Animals:
    def __init__(self, name):
        self.name = name
        print(f"Animal {self.name} is created! ")


class Dog(Animals):
    def __init__(self, name):
        super().__init__(name)
        print(f"Dog is created! ")
    

my_dog = Dog("Buddy")
print(my_dog.name)