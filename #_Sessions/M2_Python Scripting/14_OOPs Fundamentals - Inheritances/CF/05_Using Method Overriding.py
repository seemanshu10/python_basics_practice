class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def sound(self): 
        print("The dog barks.")

generic_animal = Animal()
dog = Dog()

generic_animal.sound()  # Output: This animal makes a sound.
dog.sound()             # Output: The dog barks.