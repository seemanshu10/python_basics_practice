class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

a = Asset("Character_A", 1)

print(a.__init__)
# <bound method Asset.__init__ of <__main__.Asset object at 0x7f9b8f12a250>>