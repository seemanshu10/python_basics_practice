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

    def __init__(self, name, health , speed , level, range_power):
        super().__init__(name, health, speed, level)
        self.weapon = "Bow"
        self.range_power = range_power

    def shoot_arrow(self):
        print(f"{self.name} shoots an arrow.")

   
    def show_stats(self):
        super().show_stats()
        print(f"Weapon: {self.weapon}")
        print(f"Range Power: {self.range_power}")


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


# Second-Level Child Classes

# Warrior Types 
class Knight(Warrior):
    def __init__(self, name, health , speed , level, strength ,armor, shield_power):
        super().__init__(name, health, speed, level, strength)
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
    def __init__(self, name, health , speed , level, strength ,rage_level, axe_Damage):
        super().__init__(name, health, speed, level, strength)
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
    def __init__(self, name, health , speed , level, strength ,holy_power, healing_power):
        super().__init__(name, health, speed, level, strength)
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
    def __init__(self, name, health , speed , level, strength , accuracy, critical_damage):
        super().__init__(name, health, speed, level, strength)
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
    def __init__(self, name, health , speed , level, strength , trap_count, pet_name):
        super().__init__(name, health, speed, level, strength)
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
    def __init__(self, name, health , speed , level, strength , bolt_damage, reload_speed):
        super().__init__(name, health, speed, level, strength)
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
    def __init__(self, name, health , speed , level, strength , fire_damage, burn_time):
        super().__init__(name, health, speed, level, strength)
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
    def __init__(self, name, health , speed , level, strength , ice_power, freeze_time):
        super().__init__(name, health, speed, level, strength)
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
    def __init__(self, name, health , speed , level, strength , heal_amount, support_range):
        super().__init__(name, health, speed, level, strength)
        self.heal_amount = heal_amount
        self.support_range = support_range

    def heal_ally(self):
        print(f"{self.name} heals an ally for {self.heal_amount} health points.")

    def show_stats(self):
        super().show_stats()
        print(f"Heal Amount: {self.heal_amount}")
        print(f"Support Range: {self.support_range}")


knight1 = Knight("Arthur", 180, 4, 2, 90, 70, 85)
knight1.spawn()
knight1.move()
knight1.show_stats()
knight1.attack()
knight1.defend()

berserker1 = Berserker("Ragnar", 170, 5, 2, 100, 95, 120)
print()

berserker1.spawn()
berserker1.move()
berserker1.show_stats()
berserker1.attack()
berserker1.rage_attack()

paladin1 = Paladin("Uther", 160, 4, 2, 85, 75, 60)

print()

paladin1.spawn()
paladin1.move()
paladin1.show_stats()
paladin1.attack()
paladin1.holy_strike()

sniper1 = Sniper("EagleEye", 110, 8, 2, 98, 92, 150)

print()

sniper1.spawn()
sniper1.move()
sniper1.show_stats()
sniper1.shoot_arrow()
sniper1.snipe()

hunter1 = Hunter("Robin", 120, 7, 2, 88, 4, "Wolf")
print()

hunter1.spawn()
hunter1.move()
hunter1.show_stats()
hunter1.shoot_arrow()
hunter1.set_trap()

crossbow1 = CrossbowMaster("Bolt", 125, 6, 2, 90, 130, 3)
crossbow1.spawn()
crossbow1.move()
crossbow1.show_stats()
crossbow1.shoot_arrow()
crossbow1.fire_bolt()

print()

firemage1 = FireMage("Blaze", 95, 5, 2, 140, 100, 6)

firemage1.spawn()
firemage1.move()
firemage1.show_stats()
firemage1.cast_spell()
firemage1.fireball()

icemage1 = IceMage("Frost", 100, 5, 2, 135, 85, 4)

print()

icemage1.spawn()
icemage1.move()
icemage1.show_stats()
icemage1.cast_spell()
icemage1.freeze_enemy()

healer1 = HealerMage("Ariel", 105, 5, 2, 150, 70, 12)

print()

healer1.spawn()
healer1.move()
healer1.show_stats()
healer1.cast_spell()
healer1.heal_ally()