from character import Character

class Warrior(Character):

    def __init__(self, name, health , speed , level, grade ,strength):
        super().__init__(name, health, speed, level, grade)
        self.weapon = "Sword"
        self.strength = strength

    def attack(self):
        print(f"{self.name} attacks with {self.weapon}.")

    def show_stats(self):
        super().show_stats()
        print(f"Weapon: {self.weapon}")
        print(f"Strength: {self.strength}")


class Archer(Character):

    def __init__(self, name, health , speed , level, grade,range_power):
        super().__init__(name, health, speed, level, grade)
        self.weapon = "Bow"
        self.range_power = range_power

    def shoot_arrow(self):
        print(f"{self.name} shoots an arrow.")

   
    def show_stats(self):
        super().show_stats()
        print(f"Weapon: {self.weapon}")
        print(f"Range Power: {self.range_power}")


class Mage(Character):

    def __init__(self, name, health, speed, level, grade, mana):
        super().__init__(name, health, speed, level, grade)
        self.weapon = "staff"
        self.mana = mana

    def cast_spell(self):
        print(f"{self.name} casts a spell.")

    def show_stats(self):
        super().show_stats()
        print(f"Weapon: {self.weapon}")
        print(f"Mana: {self.mana}")