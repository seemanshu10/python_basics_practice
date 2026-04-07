#  ---------- Modifying via Class ----------
class Vehicle:
    wheels = 4  

car1 = Vehicle()
car2 = Vehicle()

# Check original values
print(car1.wheels)  # 4
print(car2.wheels)  # 4

# Modify via class
Vehicle.wheels = 6

# Check again
print(car1.wheels)  # 6
print(car2.wheels)  # 6




# ---------- Modifying via Object ----------
car1.wheels = 8

print(car1.wheels)  # 8 (instance attribute)
print(car2.wheels)  # 4 (still uses class attribute)
print(Vehicle.wheels)  # 4