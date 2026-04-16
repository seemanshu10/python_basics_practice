## AP. Vehicle Management System

### Task Objective

* Create a system to represent different types of vehicles using class inheritance.
* Define a parent class that holds shared vehicle attributes.
* Create child classes that add specific properties and behaviors.
* Demonstrate inheritance through object creation and method usage.

### Instructions

* Define a parent class named `Vehicle` with attributes like `brand` and `model`.
* Add a method to the parent class to display the basic vehicle information.
* Create two child classes:
  * `Car` with an additional attribute like `car_type`.
  * `Bike` with an additional attribute like `engine_type`.
* Each child class should include its own method to simulate starting the engine.
* Use the `super()` function to call the parent class constructor from child classes.
* Create at least one object from each child class.
* Display the vehicle's details and call the method to start the engine.

### Sample Usage

``` python
# Create and test objects
car1 = Car("Toyota", "Corolla", "Sedan")
bike1 = Bike("Honda", "CBR 600", "Petrol")

car1.display_info()
car1.start_engine()

print()  # For spacing

bike1.display_info()
bike1.start_engine()
```

### Sample Output

```
Car: "Toyota, Corolla, Sedan"
Bike: "Honda, CBR 600, Petrol"

Toyota Corolla
The Sedan car engine is now starting.
Honda CBR 600
The Petrol bike engine is now starting.
```
