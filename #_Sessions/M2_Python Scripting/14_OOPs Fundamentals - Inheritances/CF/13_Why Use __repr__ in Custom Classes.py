# -------------- Without repr
# Example without __repr__
class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

# Create some Asset objects
a1 = Asset("Character_A", 1)
a2 = Asset("Prop_B", 2)

# Print single object
print(a1)
# <__main__.Asset object at 0x00000241D0181FD0>

# Print list of objects
assets = [a1, a2]

print(assets)
# [<__main__.Asset object at 0x00000241D0181FD0>, <__main__.Asset object at 0x00000241D0181F10>]





# --------------- With __repr__
class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self):
        return f"<Asset(name='{self.name}', version={self.version})>"

a1 = Asset("Character_A", 1)
a2 = Asset("Prop_B", 2)

print(a1) # <Asset(name='Character_A', version=1)>

assets = [a1, a2]
print(assets)
# [<Asset(name='Character_A', version=1)>, <Asset(name='Prop_B', version=2)>] 