# base class 
class Character:
    def __init__(self, name, health, speed, level):
        self.name = name
        self.health = health
        self.speed = speed
        self.level = level

    def spawn(self):
        print(f"{self.name} has spawned into the game." )

    def move(self):
        print(f"{self.name} moves with speed {self.speed}")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Speed: {self.speed}")
        print(f"Level: {self.level}")

class Warrior(Character):

    def __init__(self, name, health , speed , level, strength):
        super().__init__(name, health, speed, level)
        self.weapon = "Sword"
        self.strength = strength

    def attack(self):
        print(f"{self.name} attacks with {self.weapon}.")

    def show_stats(self):
        super().show_stats()
        print(f"Weapon: {self.weapon}")
        print(f"Strength: {self.strength}")


class Archer(Character):

    def __init__(self, name, health , speed , level, strength):
        super().__init__(name, health, speed, level)
        self.weapon = "Bow"
        self.strength = strength

    def shoot_arrow(self):
        print(f"{self.name} shoots an arrow.")

   
    def show_stats(self):
        super().show_stats()
        print(f"Weapon: {self.weapon}")
        print(f"Strength: {self.strength}")


class Mage(Character):

    def __init__(self, name, health , speed , level, mana):
        super().__init__(name, health, speed, level)
        self.weapon = "staff"
        self.mana = mana

    def cast_spell(self):
        print(f"{self.name} casts a spell.")

   
    def show_stats(self):
        super().show_stats()
        print(f"Weapon: {self.weapon}")
        print(f"Mana: {self.mana}")


warrior1 = Warrior("Thor", 150, 5, 1, 80)
warrior1.spawn()
warrior1.move()
warrior1.show_stats()
warrior1.attack()
        
print()

archer1 = Archer("Legolas", 100, 7, 1, 95)
archer1.spawn()
archer1.move()
archer1.show_stats()
archer1.shoot_arrow()


print()
mage1 = Mage("Merlin", 90, 4, 1, 120)
mage1.spawn()
mage1.move()
mage1.show_stats()
mage1.cast_spell()