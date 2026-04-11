class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self):
        return f"Asset(Name='{self.name}', version = {self.version})"

    # def __eq__(self, other):
    #     return self.name == other.name and self.version == other.version
    
a1 = Asset("Characters_A", 1)
a2 = Asset("Characters_A", 1)

print(repr(a1))
print(a1.__repr__())

# print(a1.__eq__(a2))
# print(a2.__eq__(a1))
# print(a1 == a2)
# print(id(a1) , id(a2))
# print(id(a1) == id(a2))

a = 5
b = 5

# print(id(a) == id(b))
# print(a == b)
# print(a.__eq__(b))


text = "Hello , World"

# print(text)
# print(str(text))
# print(text.__str__())

# print(repr(text))
# print(type(repr(text)))

