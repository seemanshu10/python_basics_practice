# Build a Vehicle Management System

# parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def display_info(self):
        print(f"The {self.brand} {self.model}")

class Car(Vehicle):
    def __init__(self, brand, model, car_type):
        # calling parent init constructor(vehicle) in child class(car)
        super().__init__(brand, model)
        self.car_type = car_type

    def start_engine(self):
        print(f"The {self.car_type} car engine is starting.")

class Bike(Vehicle):
    def __init__(self, brand, model, engine_type):
        super().__init__(brand, model)
        self.engine_type = engine_type

    def start_engine(self):
        print(f"The {self.engine_type} bike engine is now starting.")


car1 = Car("Toyota", "Corolla", "Sedan")
bike1 = Bike("Honda", "CBR 600", "Petrol")

# Display details and start engines
print(f'Car: "{car1.brand}, {car1.model}, {car1.car_type}"')
print(f'Bike: "{bike1.brand}, {bike1.model}, {bike1.engine_type}"\n')

car1.display_info()
car1.start_engine()

print()

bike1.display_info()
bike1.start_engine()

