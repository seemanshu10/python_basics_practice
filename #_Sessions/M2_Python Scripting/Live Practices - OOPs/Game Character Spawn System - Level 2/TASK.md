## Game Character Spawn System - Level 2 (Multilevel Inheritance)

### Problem Scenario
* In the first task, you created a base Character class and three child classes: Warrior, Archer, and Mage. 
    * Now the game is becoming bigger, and each main character type is getting its own advanced versions.
    * Your task in this level is to extend the previous system using multilevel inheritance.
* This means:
    * Character is the base class
    * Warrior, Archer, and Mage inherit from Character
    * Then new advanced classes inherit from Warrior, Archer, and Mage
* You need to create a deeper class hierarchy where the child classes of Warrior, Archer, and Mage have their own extra properties and methods.

### Task Requirements
Class Structure to Create
#### 1. Base Class
* **Character**
    * Every character should have:
        * name
        * health
        * speed
        * level
    * Methods:
        * spawn()
        * move()
        * show_stats()

#### 2. First-Level Child Classes
* ✔️ **Warrior inherits from Character**
    * Extra properties:
        * weapon = "Sword"
        * strength
    * Method:
        * attack()  

* ✔️ **Archer inherits from Character**
    * Extra properties:
        * weapon = "Bow"
        * range_power
    * Method:
        * shoot_arrow()

* ✔️ **Mage inherits from Character**
    * Extra properties:
        * weapon = "Staff"
        * mana
    * Method:
        * cast_spell()

#### 3. Second-Level Child Classes
* Now create three advanced types for each category.

**A. Warrior Types**
* ✔️ **Knight Inherit from Warrior**
    * Additional Attributes:
        * armor
        * shield_power
    * Method:
        * defend()  
* ✔️ **Berserker Inherit from Warrior**
    * Additional Attributes:
        * rage_level
        * axe_damage    
    * Method:
        * rage_attack()
* ✔️ **Paladin Inherit from Warrior**
    * Additional Attributes:
        * holy_power
        * healing_power
    * Method:
        * holy_strike()

**B. Archer Types**
* ✔️ **Sniper Inherit from Archer**
    * Additional Attributes:
        * accuracy
        * critical_damage
    * Method:
        * snipe()

* ✔️ **Hunter Inherit from Archer**
    * Additional Attributes:
        * trap_count
        * pet_name
    * Method:
        * set_trap()

* ✔️ **CrossbowMaster Inherit from Archer**
    * Additional Attributes:
        * bolt_damage
        * reload_speed
    * Method:
        * fire_bolt()

**C. Mage Types**
* ✔️ **FireMage Inherit from Mage**
    * Additional Attributes:
        * fire_damage
        * burn_time
    * Method:
        * fireball()

* ✔️ **IceMage Inherit from Mage**
    * Additional Attributes:
        * ice_power
        * freeze_time
    * Method:
        * freeze_enemy()

* ✔️ **HealerMage Inherit from Mage**
    * Additional Attributes:
        * heal_amount
        * support_range
    * Method:
        * heal_ally()

### Instructions

* You need to continue from the previous task and expand the class system.
* Create the following:
* Base class:
  * Character
* First-level classes:
  * Warrior
  * Archer
  * Mage
* Second-level classes:
  * 3 Warrior types
  * 3 Archer types
  * 3 Mage types
* For each second-level class :
  * Inherit all common behavior from its parent classes
  * Add its own extra properties
  * Add its own special method
* Create objects for all second-level classes  For each object:
  * Call methods from all levels of inheritance This includes:
* Base class methods:
  * spawn()
  * move()
  * show_stats()
* First-level Classes methods:
  * Warrior → attack()
  * Archer → shoot_arrow()
  * Mage → cast_spell()
* Second-level Classes methods:
  * Each class should call its own special method
* Example:
  * Knight → defend()
  * Berserker → rage_attack()
  * Sniper → snipe()
  * FireMage → fireball()
* Each object should be able to use methods from:
  * Its parent class
  * Its grandparent class
  * Its own class
* Example: 
    * A Knight object should be able to call:
    * spawn()
    * move()
    * show_stats()
    * attack()
    * defend()
* Ensure all methods execute correctly and follow the expected output

### Usage Script

```python
knight1 = Knight("Arthur", 180, 4, 2, 90, 70, 85)
berserker1 = Berserker("Ragnar", 170, 5, 2, 100, 95, 120)
paladin1 = Paladin("Uther", 160, 4, 2, 85, 75, 60)

sniper1 = Sniper("EagleEye", 110, 8, 2, 98, 92, 150)
hunter1 = Hunter("Robin", 120, 7, 2, 88, 4, "Wolf")
crossbow1 = CrossbowMaster("Bolt", 125, 6, 2, 90, 130, 3)

firemage1 = FireMage("Blaze", 95, 5, 2, 140, 100, 6)
icemage1 = IceMage("Frost", 100, 5, 2, 135, 85, 4)
healer1 = HealerMage("Ariel", 105, 5, 2, 150, 70, 12)

knight1.spawn()
knight1.move()
knight1.show_stats()
knight1.attack()
knight1.defend()

print()

berserker1.spawn()
berserker1.move()
berserker1.show_stats()
berserker1.attack()
berserker1.rage_attack()

print()

paladin1.spawn()
paladin1.move()
paladin1.show_stats()
paladin1.attack()
paladin1.holy_strike()

print()

sniper1.spawn()
sniper1.move()
sniper1.show_stats()
sniper1.shoot_arrow()
sniper1.snipe()

print()

hunter1.spawn()
hunter1.move()
hunter1.show_stats()
hunter1.shoot_arrow()
hunter1.set_trap()

print()

crossbow1.spawn()
crossbow1.move()
crossbow1.show_stats()
crossbow1.shoot_arrow()
crossbow1.fire_bolt()

print()

firemage1.spawn()
firemage1.move()
firemage1.show_stats()
firemage1.cast_spell()
firemage1.fireball()

print()

icemage1.spawn()
icemage1.move()
icemage1.show_stats()
icemage1.cast_spell()
icemage1.freeze_enemy()

print()

healer1.spawn()
healer1.move()
healer1.show_stats()
healer1.cast_spell()
healer1.heal_ally()
```

### Expected Output

```
Arthur has spawned into the game.
Arthur moves with speed 4.
Name: Arthur
Health: 180
Speed: 4
Level: 2
Weapon: Sword
Strength: 90
Armor: 70
Shield Power: 85
Arthur attacks with Sword.
Arthur defends with shield power 85.

Ragnar has spawned into the game.
Ragnar moves with speed 5.
Name: Ragnar
Health: 170
Speed: 5
Level: 2
Weapon: Sword
Strength: 100
Rage Level: 95
Axe Damage: 120
Ragnar attacks with Sword.
Ragnar performs a rage attack with axe damage 120.

Uther has spawned into the game.
Uther moves with speed 4.
Name: Uther
Health: 160
Speed: 4
Level: 2
Weapon: Sword
Strength: 85
Holy Power: 75
Healing Power: 60
Uther attacks with Sword.
Uther uses holy strike with holy power 75.

EagleEye has spawned into the game.
EagleEye moves with speed 8.
Name: EagleEye
Health: 110
Speed: 8
Level: 2
Weapon: Bow
Range Power: 98
Accuracy: 92
Critical Damage: 150
EagleEye shoots an arrow.
EagleEye performs a snipe with critical damage 150.

Robin has spawned into the game.
Robin moves with speed 7.
Name: Robin
Health: 120
Speed: 7
Level: 2
Weapon: Bow
Range Power: 88
Trap Count: 4
Pet Name: Wolf
Robin shoots an arrow.
Robin sets a trap.

Bolt has spawned into the game.
Bolt moves with speed 6.
Name: Bolt
Health: 125
Speed: 6
Level: 2
Weapon: Bow
Range Power: 90
Bolt Damage: 130
Reload Speed: 3
Bolt shoots an arrow.
Bolt fires a powerful bolt.

Blaze has spawned into the game.
Blaze moves with speed 5.
Name: Blaze
Health: 95
Speed: 5
Level: 2
Weapon: Staff
Mana: 140
Fire Damage: 100
Burn Time: 6
Blaze casts a spell.
Blaze throws a fireball with fire damage 100.

Frost has spawned into the game.
Frost moves with speed 5.
Name: Frost
Health: 100
Speed: 5
Level: 2
Weapon: Staff
Mana: 135
Ice Power: 85
Freeze Time: 4
Frost casts a spell.
Frost freezes the enemy for 4 seconds.

Ariel has spawned into the game.
Ariel moves with speed 5.
Name: Ariel
Health: 105
Speed: 5
Level: 2
Weapon: Staff
Mana: 150
Heal Amount: 70
Support Range: 12
Ariel casts a spell.
Ariel heals an ally for 70 health points.
```
