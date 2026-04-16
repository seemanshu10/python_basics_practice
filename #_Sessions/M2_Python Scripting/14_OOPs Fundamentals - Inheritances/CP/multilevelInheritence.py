class LivingBeing:
    def breathe(self):
        print("Breathing...")

class Plant(LivingBeing):
    def photosynthesize(self):
        print("Photosynthesizing...")

class Flower(Plant):
    def bloom(self):
        print("The flower is blooming.")

flower = Flower()
flower.breathe()

flower.photosynthesize()
flower.bloom()

"""
Breathing...
Photosynthesizing...
The flower is blooming.
"""