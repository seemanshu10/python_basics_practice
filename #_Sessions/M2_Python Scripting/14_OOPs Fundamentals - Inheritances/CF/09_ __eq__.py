# ---------  With Built-in Type
a = 5
b = 5

print(a == b)          # Output: True
print(a.__eq__(b))     # Output: True




# ----------  With Custom Class
class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __eq__(self, other):
        return self.name == other.name and self.version == other.version

a1 = Asset("Character_A", 1)
a2 = Asset("Character_A", 1)
a3 = Asset("Character_A", 2)

print(a1.__eq__(a2))  # True
print(a1.__eq__(a3))  # False




# -------------- What if we don’t define __eq__?
class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

a1 = Asset("Character_A", 1)
a2 = Asset("Character_A", 1)

print(a1 == a2)          # False
print(a1.__eq__(a2))     # NotImplemented

print(id(a1), id(a2))    # Two different memory addresses