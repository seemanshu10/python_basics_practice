# base class 
class Character:
    VALID_GRADES = ["Common", "Rare", "Epic", "Legendary"]

    def __init__(self, name, health, speed, level, grade):
        
        if grade not in Character.VALID_GRADES:
            raise ValueError(f"Invalid grade '{grade}'. Must be one of: {', '.join(Character.VALID_GRADES)}")
        self.name = name
        self.health = health
        self.speed = speed
        self.level = level
        self.grade = grade

    def spawn(self):
        print(f"{self.name} has spawned into the game." )

    def move(self):
        print(f"{self.name} moves with speed {self.speed}")

    def show_stats(self):
        print(f"Name: {self.name}")
        print(f"Health: {self.health}")
        print(f"Speed: {self.speed}")
        print(f"Level: {self.level}")
        print(f"Grade: {self.grade}")

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

# Second-Level Child Classes
# Warrior Types 
class Knight(Warrior):
    def __init__(self, name, health, speed, level, strength, grade, armor, shield_power):
        super().__init__(name, health, speed, level, strength, grade)
        self.armor = armor
        self.shield_power = shield_power

    def defend(self):
        print(f"{self.name} defends with shield power {self.shield_power}.")

    def show_stats(self):
        super().show_stats()
        print(f"Armor: {self.armor}")
        print(f"Shield Power: {self.shield_power}")


# Warrior Types 
class Berserker(Warrior):
    def __init__(self, name, health, speed , level, strength, grade, rage_level, axe_Damage):
        super().__init__(name, health, speed, level, strength, grade)
        self.rage_level = rage_level
        self.axe_Damage = axe_Damage

    def rage_attack(self):
        print(f"{self.name} performs a rage attack with axe damage {self.axe_Damage}.")

    def show_stats(self):
        super().show_stats()
        print(f"Rage Level: {self.rage_level}")
        print(f"Axe Damage:  {self.axe_Damage}")

# Warrior Types 
class Paladin(Warrior):
    def __init__(self, name, health, speed, level, strength, grade, holy_power, healing_power):
        super().__init__(name, health, speed, level, strength, grade)
        self.holy_power = holy_power
        self.healing_power = healing_power

    def holy_strike(self):
        print(f"{self.name} uses holy strike with holy power {self.holy_power}.")

    def show_stats(self):
        super().show_stats()
        print(f"Holy Power: {self.holy_power}")
        print(f"Healing Power:  {self.healing_power}")

# Archer Types 
class Sniper(Archer):
    def __init__(self, name, health, speed, level, strength, grade, accuracy, critical_damage):
        super().__init__(name, health, speed, level, strength, grade)
        self.accuracy = accuracy
        self.critical_damage = critical_damage

    def snipe(self):
        print(f"{self.name} performs a snipe with critical damage {self.critical_damage}.")

    def show_stats(self):
        super().show_stats()
        print(f"Accuracy: {self.accuracy}")
        print(f"Critical Damage: {self.critical_damage}")

# Archer Types 
class Hunter(Archer):
    def __init__(self, name, health, speed, level, strength, grade, trap_count, pet_name):
        super().__init__(name, health, speed, level, strength, grade)
        self.trap_count = trap_count
        self.pet_name = pet_name

    def set_trap(self):
        print(f"{self.name} sets a trap.")

    def show_stats(self):
        super().show_stats()
        print(f"Trap Count: {self.trap_count}")
        print(f"Pet Name: {self.pet_name}")

# Archer Types 
class CrossbowMaster(Archer):
    def __init__(self, name, health, speed, level, strength, grade, bolt_damage, reload_speed):
        super().__init__(name, health, speed, level, strength, grade)
        self.bolt_damage = bolt_damage
        self.reload_speed = reload_speed

    def fire_bolt(self):
        print(f"{self.name} fires a powerful bolt.")

    def show_stats(self):
        super().show_stats()
        print(f"Bolt Damage: {self.bolt_damage}")
        print(f"Reload Speed: {self.reload_speed}")

# Mage Types 
class FireMage(Mage):
    def __init__(self, name, health, speed, level, strength, grade, fire_damage, burn_time):
        super().__init__(name, health, speed, level, strength, grade)
        self.fire_damage = fire_damage
        self.burn_time = burn_time

    def fireball(self):
        print(f"{self.name} throws a fireball with fire damage {self.fire_damage}")

    def show_stats(self):
        super().show_stats()
        print(f"Fire Damage:  {self.fire_damage}")
        print(f"Burn Time: {self.burn_time}")

# Mage Types 
class IceMage(Mage):
    def __init__(self, name, health, speed, level, strength, grade, ice_power, freeze_time):
        super().__init__(name, health, speed, level, strength, grade)
        self.ice_power = ice_power
        self.freeze_time = freeze_time

    def freeze_enemy(self):
        print(f"{self.name} freezes the enemy for {self.freeze_time} seconds.")

    def show_stats(self):
        super().show_stats()
        print(f"Ice Power: {self.ice_power}")
        print(f"Freeze Time: {self.freeze_time}")

# Mage Types 
class HealerMage(Mage):
    def __init__(self, name, health, speed, level, strength, grade, heal_amount, support_range):
        super().__init__(name, health, speed, level, strength, grade)
        self.heal_amount = heal_amount
        self.support_range = support_range

    def heal_ally(self):
        print(f"{self.name} heals an ally for {self.heal_amount} health points.")

    def show_stats(self):
        super().show_stats()
        print(f"Heal Amount: {self.heal_amount}")
        print(f"Support Range: {self.support_range}")

warrior1 = Warrior("Thor", 150, 5, 1, "Common", 80)
knight1 = Knight("Arthur", 180, 4, 2, "Rare", 90, 70, 85)
firemage1 = FireMage("Blaze", 95, 5, 2, "Epic", 140, 100, 6)

warrior1.spawn()
warrior1.show_stats()
warrior1.attack()

print()

knight1.spawn()
knight1.show_stats()
knight1.attack()
knight1.defend()

print()

firemage1.spawn()
firemage1.show_stats()
firemage1.cast_spell()
firemage1.fireball()