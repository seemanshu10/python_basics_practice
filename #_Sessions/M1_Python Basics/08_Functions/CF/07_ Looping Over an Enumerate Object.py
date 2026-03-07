items = ['A', 'B', 'C']
result = enumerate(items)

print(result)
# Output: <enumerate object at 0x0000021F8A4B>


for value in enumerate(items):
    print(value)


# ----------- Unpacking Object
for index, item in enumerate(items):
    print(index, item)

# Output:
# 0 A
# 1 B
# 2 C