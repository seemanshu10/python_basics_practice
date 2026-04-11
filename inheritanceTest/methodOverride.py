# class Animals:
    
#     def sound(self):
#         print("Animal Makes a sound ")

# class Dog(Animals):

#     def sound(self):
#         print("Dog Barks ")

# generic_animal = Animals()
# mydog = Dog()

# generic_animal.sound()
# mydog.sound()


# super use to extend the animal class sound method 

class Animals:
    
    def sound(self):
        print("Animal Makes a sound ")

class Dog(Animals):

    def sound(self):
        super().sound()
        print("Dog Barks ")


mydog = Dog()
mydog.sound()

"""
Animal Makes a sound 
Dog Barks 
"""

