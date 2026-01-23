"""
Docstring for list
"""

num = [1,2,4]
print (num)

num[1] = 21
print (num)

num[2] = 10
print(num)


num2 = [[1,2,4],[5,6,8]]
num2[1][2] = 10
print(num2) 


colors = ["red","Blue"]

colors.extend(["green","yellow"])

print(colors)
colors.extend("seemanshu")
print (colors)

colors.pop()
print(colors)

colors.pop(5)
print(colors)

del colors[2]
print(colors)

#del colors
#print(colors) 

index_ye  = colors.index("yellow") 
print (index_ye)

co = colors.count ("a")
print(co)

co = colors.count ("i")
print(co)

#mixed = [1, 3.5 , "Apple ", True ,1]

num = [1,2,3,4]

print (num.append("hello"))
print (num)