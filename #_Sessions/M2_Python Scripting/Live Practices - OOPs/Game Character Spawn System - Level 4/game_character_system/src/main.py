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