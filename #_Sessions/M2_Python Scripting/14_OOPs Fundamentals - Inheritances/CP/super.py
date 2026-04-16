class ElectronicDevices:
    def __init__(self, brand, power_status = False):
        self.brand = brand
        self.power_status = power_status

    def turn_on(self):
        self.power_status = True
        print(f"{self.brand} device is now ON.")

class Smartphone(ElectronicDevices):
    def __init__(self, brand, model, power_status=False):
        super().__init__(brand, power_status)
        self.model = model

    def display_info(self):
        print(f"Smartphone: {self.brand} {self.model}, power Status: {'ON' if self.power_status else 'OFF'}")

phone = Smartphone("Samsung", "Galaxy S21")
phone.display_info()

phone.turn_on()
phone.display_info()

"""
Smartphone: Samsung Galaxy S21, power Status: OFF
Samsung device is now ON.
Smartphone: Samsung Galaxy S21, power Status: ON

"""