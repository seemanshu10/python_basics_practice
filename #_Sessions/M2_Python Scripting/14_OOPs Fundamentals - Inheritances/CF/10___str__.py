# --------------- Regular Usage 
text = "Hello, world"

print(text)           # Output: Hello, world
print(str(text))      # Output: Hello, world
print(text.__str__()) # Output: Hello, world




# ---------- With Custom Class
class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __str__(self):
        return f"{self.name}_v{self.version:03}"

a = Asset("Character_A", 1)

print(a)
print(str(a))
print(a.__str__())

# Character_A_v001
# Character_A_v001
# Character_A_v001