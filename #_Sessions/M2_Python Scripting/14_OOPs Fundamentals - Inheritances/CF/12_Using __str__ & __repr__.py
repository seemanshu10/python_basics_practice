class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self):
        return f"Asset(name={self.name!r}, version={self.version!r})"

    def __str__(self):
        return f"<Asset name='{self.name}' version={self.version:03d}>"

a = Asset("Character_A", 1)

print(a)    # <Asset name='Character_A' version=001>

print(repr(a))    # Asset(name='Character_A', version=1)