# infinite loop
while True:
    print("This loop will run forever...")

# Iterating Over Integer
i = 0
while i < 5:
    print(i)
    i += 1


# Iterating Over a String
text = "Hello"
index = 0

while index < len(text):
    print(text[index])
    index += 1

print("All characters printed.")


# Iterating Over Integers
start = 1
end = 5
current = start

while current <= end:
    print(current)
    current += 1

print("All integers printed.")


# Iterating over List
numbers = [10, 20, 30, 40, 50]
index = 0

while index < len(numbers):
    print(numbers[index])
    index += 1 

print("All numbers printed.")



# Iterating Over a Dictionary's Keys
grades = {"Alice": 85, "Bob": 90, "Charlie": 78}
keys = list(grades.keys())
index = 0

while index < len(keys):
    key = keys[index]
    print(key)
    index += 1

print("All keys printed.")