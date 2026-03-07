# append()
fruits = []

fruits.append("apple")
fruits.append("banana")


# insert()
fruits = ["banana", "orange", "mango"]
fruits.insert(0, "apple")


# extend()
colors = ["red", "blue"]
colors.extend(["green", "yellow"])


# remove()
fruits = ["apple", "banana", "cherry", "banana"]
fruits.remove("banana")


# pop()
colors = ["red", "blue", "green"]
last_color = colors.pop()

print("Removed color:", last_color)
print("Updated list:", colors)


# del keyword
colors = ["red", "green", "blue", "yellow"]
del colors[2]


# index()
fruits = ["apple", "banana", "cherry", "date", "banana"]
index_banana = fruits.index("banana")


# count()
fruits = ["apple", "banana", "kiwi", "date", "banana"]
index_banana = fruits.index("banana")