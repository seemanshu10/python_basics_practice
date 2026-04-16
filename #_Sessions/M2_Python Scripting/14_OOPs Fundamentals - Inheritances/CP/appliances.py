class Applicance:
    def __init__(self, brand):
        self.brand = brand

    def turn_on(self):
        print(f"The {self.brand} appliance is now on.")

class Refrigerator(Applicance):
    def cool(self):
        print(f"The {self.brand} refrigerator is cooling.")


fridge = Refrigerator("LG")

fridge.turn_on()
fridge.cool()

"""
The LG appliance is now on.
The LG refrigerator is cooling.
"""