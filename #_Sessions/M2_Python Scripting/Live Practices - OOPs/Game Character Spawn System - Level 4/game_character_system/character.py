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