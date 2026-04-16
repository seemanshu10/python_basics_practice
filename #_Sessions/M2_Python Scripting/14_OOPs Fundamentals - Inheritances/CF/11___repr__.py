# --------------- With Built-in Type
text = "Hello"

print(text)         # Output: Hello
print(repr(text))   # Output: 'Hello'
print(text.__repr__())  # Output: 'Hello'



# ------------ With Custom Class
class Asset:
    def __init__(self, name, version):
        self.name = name
        self.version = version

    def __repr__(self):
        return f"Asset(name='{self.name}', version={self.version})"

a = Asset("Character_A", 1)

print(repr(a))
print(a.__repr__())
