class Vehicle:
    wheels = 4  # Class attribute

    def display_info(self):
        print(f"This vehicle has {self.wheels} wheels.")

car = Vehicle()
car.display_info()  # Output: This vehicle has 4 wheels.
