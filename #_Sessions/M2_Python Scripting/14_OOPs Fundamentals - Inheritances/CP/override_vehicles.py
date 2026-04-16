class Vehicle:
    def display_info(self):
        print("This is a general Vehicle.")

class Car(Vehicle):
    def display_info(self):
        print("This is a Car.")

class Bike(Vehicle):
    def display_info(self):
        print("This is a Bike.")

vehicle = Vehicle()
vehicle.display_info()

car = Car()
car.display_info()

bike = Bike()
bike.display_info()

"""
This is a general Vehicle.
This is a Car.
This is a Bike.
"""