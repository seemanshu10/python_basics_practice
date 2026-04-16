## Game Character Spawn System - Level 3 (Character Grades)

### Problem Scenario
So far, you have created multiple types of characters using inheritance.
* The system now needs an additional feature.
* Every character must have a grade.
* A character can belong to one of the following grades:
    * Common
    * Rare
    * Epic
    * Legendary
* This grade should become part of the character system itself, meaning every character must store and display its grade when created.
* Your task is to update the existing class system and add the grade property so that it becomes part of all characters in the game.

### Task Requirements
You need to update the existing system:
* The Character class should now also store:
    * grade
* So the common properties become:
    * name
    * health
    * speed
    * level
    * grade
* Since all other classes inherit from Character, they should also automatically get this property.

* **Grade Values**
* Only these four grades should be used:
    * "Common"
    * "Rare"
    * "Epic"
    * "Legendary"

### Instructions
* You should update their old classes and constructors in such a way that grade becomes part of the full inheritance system.
* After doing that:
    * all objects must be created with a grade
    * show_stats() must also display the grade
    * the rest of the old functionality should still work properly
* You should use the same character hierarchy you already built and now include grade in it.
* **Characters to Test**
    * Use these four types of characters for testing:
        * Warrior
        * Knight
        * FireMage
    * This helps test:
        * base inheritance
        * multilevel inheritance
    * grade support across the full system

### Usage Script
```python
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
```

### Output

```
Thor has spawned into the game.
Name: Thor
Health: 150
Speed: 5
Level: 1
Grade: Common
Weapon: Sword
Strength: 80
Thor attacks with Sword.

Arthur has spawned into the game.
Name: Arthur
Health: 180
Speed: 4
Level: 2
Grade: Rare
Weapon: Sword
Strength: 90
Armor: 70
Shield Power: 85
Arthur attacks with Sword.
Arthur defends with shield power 85.

Blaze has spawned into the game.
Name: Blaze
Health: 95
Speed: 5
Level: 2
Grade: Epic
Weapon: Staff
Mana: 140
Fire Damage: 100
Burn Time: 6
Blaze casts a spell.
Blaze throws a fireball with fire damage 100.
```
