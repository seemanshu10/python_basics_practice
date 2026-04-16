class Animal:
    def sound(self):
        print("This animal makes a sound.")

class Dog(Animal):
    def sound(self):  
        super().sound()           # Step 1: Call parent method
        print("The dog barks loudly.")  # Step 2: Add custom behavior

dog = Dog()
dog.sound()
