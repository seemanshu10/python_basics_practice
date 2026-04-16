# Zoo Animal Tracker with Method Overriding
class Animal:
    def sound(self):
        print("The Animal Makes a geberic sound.")

    def feeding_time(self):
        print("Animal eats.")


class Dog(Animal):
    def sound(self):
        print("Dog Barks!")

    def feeding_time(self):
        print("The Dog Eats twice a day.")

class Cat(Animal):
    def sound(self):
        print("Dog Barks!")

    def feeding_time(self):
        print("The cat Eats once a day.")


dog1 = Dog()
cat1 = Cat()

dog1.sound()
dog1.feeding_time()

cat1.sound()
cat1.feeding_time()

"""
Dog Barks!
The Dog Eats twice a day.
Dog Barks!
The cat Eats once a day.
"""