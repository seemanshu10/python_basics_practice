## Game Character Spawn System - Level 1

### Problem Scenario
* You are building a fantasy game system where different types of characters can enter a battlefield.
* Every character shares some common properties like:
    * Name
    * Health
    * Speed
    * Level
* However, each character type (Warrior, Archer, Mage) has its own:
    * Weapon
    * Special abilities
* Your task is to create a character system using Python classes.

### Task Requirements
You need to design:
#### 1. Base Class
* Create a class called Character. Every character should have:
    * name
    * health
    * speed
    * level
* The class should also have methods to:
    * **spawn()**  the character into the game
        ```
        <name> has spawned into the game.
        ```
    * **move()** Move the character 
        ```
        <name> moves with speed <speed>.
        ```
    * **show_stats()** Show the character stats
        ```
        Name: <name>
        Health: <health>
        Speed: <speed>
        Level: <level>
        ```

#### 2. Child Classes
Create the following child classes from Character:
* ✔️ **Warrior**
    * Inherit from Character.
    * Additional attributes:
        * weapon = "Sword"
        * strength
    * Special  Method:
        * attack()
* ✔️ **Archer**
    * Inherit from Character
    * Additional Attributes:
        * weapon = "Bow"
        * range_power
    * Special Method:
        * shoot_arrow()
* ✔️ **Mage**
    * Inherit from Character
    * Additional Attributes:
        * weapon = "Staff"
        * mana
    * Special Method:
        * cast_spell()

### Instructions
* Create all classes using inheritance
* Ensure child classes inherit from the Character base class
* Create the following objects:
```python
warrior1 = Warrior("Thor", 150, 5, 1, 80)
archer1 = Archer("Legolas", 100, 7, 1, 95)
mage1 = Mage("Merlin", 90, 4, 1, 120)
```
* For each object:
  * Call methods inherited from Character
    * spawn()
    * move()
    * show_stats()
  * Call its own special method:
    * Warrior → attack()
    * Archer → shoot_arrow()
    * Mage → cast_spell()
* Ensure all methods execute correctly and produce the expected output

### Usage Script

```python
warrior1 = Warrior("Thor", 150, 5, 1, 80)
archer1 = Archer("Legolas", 100, 7, 1, 95)
mage1 = Mage("Merlin", 90, 4, 1, 120)

warrior1.spawn()
warrior1.move()
warrior1.show_stats()
warrior1.attack()

print()

archer1.spawn()
archer1.move()
archer1.show_stats()
archer1.shoot_arrow()

print()

mage1.spawn()
mage1.move()
mage1.show_stats()
mage1.cast_spell()
```

### Expected Output

```
Thor has spawned into the game.
Thor moves with speed 5.
Name: Thor
Health: 150
Speed: 5
Level: 1
Weapon: Sword
Strength: 80
Thor attacks with Sword.

Legolas has spawned into the game.
Legolas moves with speed 7.
Name: Legolas
Health: 100
Speed: 7
Level: 1
Weapon: Bow
Range Power: 95
Legolas shoots an arrow.

Merlin has spawned into the game.
Merlin moves with speed 4.
Name: Merlin
Health: 90
Speed: 4
Level: 1
Weapon: Staff
Mana: 120
Merlin casts a spell.
```
