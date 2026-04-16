## Game Character Spawn System - Level 4 (Modular Project Structure)

### Problem Scenario
Until now, you have been creating all classes and objects inside a single Python file.
* This approach works for small tasks,
    * but as the system grows, it becomes difficult to manage and maintain.
    * Now your task is to reorganize the game character system into a modular file structure.
* Instead of writing everything in one file,
    * you will separate the classes into different Python files based on their role in the system.
    * You will also create a main file where you import these classes, create objects, and run the program.
* Goal of this level is to organize your code in a cleaner and more structured way using Python modules.

### Task Requirements
You need to split the system into multiple files based on their role.
* ✔️ **File 1: character.py**
    * This file should contain the base class: Character
    * This class should include the common properties and methods that all characters share.
* ✔️ **File 2: basic_characters.py**
    * This file should contain the first-level child classes:
        * Warrior
        * Archer
        * Mage
    * These classes should inherit from Character.
* ✔️ **File 3: advanced_characters.py**
    * This file should contain the advanced classes you created in the multilevel inheritance task.
    * You should include these classes:
        * Knight
        * Berserker
        * Paladin
        * Sniper
        * Hunter
        * CrossbowMaster
        * FireMage
        * IceMage
        * HealerMage
    * These classes should inherit from the appropriate parent classes.
* ✔️ **File 4: main.py**
    * This file will be used to:
        * import all required classes from the other files
        * create character objects
        * call their methods
        * display the output
    * This is the file that should run the full program.

### Task Instructions
* Required Folder Structure. The project should look like this:
    ```
    game_character_system/
    │
    ├── character.py
    ├── basic_characters.py
    ├── advanced_characters.py
    └── main.py
    ```
* You must reorganize full character system code into the file structure above.
* should make sure that:
    * each file contains the correct classes
    * imports are written properly
    * inheritance still works correctly across files
    * objects are only created inside main.py
    * the program runs without errors
* You should use the same class system they have already built in earlier levels, but now place it in separate files.

### Usage Script (main.py)
```python
from basic_characters import Warrior, Archer, Mage
from advanced_characters import Knight, FireMage, Sniper

warrior1 = Warrior("Thor", 150, 5, 1, "Common", 80)
archer1 = Archer("Legolas", 100, 7, 1, "Rare", 95)
mage1 = Mage("Merlin", 90, 4, 1, "Epic", 120)

knight1 = Knight("Arthur", 180, 4, 2, "Rare", 90, 70, 85)
firemage1 = FireMage("Blaze", 95, 5, 2, "Epic", 140, 100, 6)
sniper1 = Sniper("EagleEye", 110, 8, 2, "Rare", 98, 92, 150)

warrior1.spawn()
warrior1.show_stats()
warrior1.attack()

print()

archer1.spawn()
archer1.show_stats()
archer1.shoot_arrow()

print()

mage1.spawn()
mage1.show_stats()
mage1.cast_spell()

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

print()

sniper1.spawn()
sniper1.show_stats()
sniper1.shoot_arrow()
sniper1.snipe()
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

Legolas has spawned into the game.
Name: Legolas
Health: 100
Speed: 7
Level: 1
Grade: Rare
Weapon: Bow
Range Power: 95
Legolas shoots an arrow.

Merlin has spawned into the game.
Name: Merlin
Health: 90
Speed: 4
Level: 1
Grade: Epic
Weapon: Staff
Mana: 120
Merlin casts a spell using Staff.

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
Blaze casts a spell using Staff.
Blaze throws a fireball with fire damage 100.

EagleEye has spawned into the game.
Name: EagleEye
Health: 110
Speed: 8
Level: 2
Grade: Rare
Weapon: Bow
Range Power: 98
Accuracy: 92
Critical Damage: 150
EagleEye shoots an arrow.
EagleEye performs a snipe with critical damage 150.
```
