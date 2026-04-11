class Animals:
    def __init__(self, name):
        self.name = name
        self.age = 2 

    def eat(self):
        print(f"{self.name} is eating! ")

class Dog(Animals):

    def __init__(self, name):
        super().__init__(name)
        print("Animals Initilaized")

    def bark(self):
        print(f"{self.name} is barking. ")

my_dog = Dog("Buddy")

# my_dog.eat()
# my_dog.bark()
# print(my_dog.name)
# print(my_dog.age)

# print(my_dog.__init__)
print(dir(my_dog))