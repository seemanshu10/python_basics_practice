"""
binarySum
"""

n =77 
b = format(n,'b')
print(b)

num1 = int(input("Input the binary String a  :" ))
print(type(num1))

num2 = int(input("Input the binary String b  :" ))
print(type(num1))

num_a = format(num1,'b')

num_b = format(num2,'b')

total = str(num_a + num_b)
print (total)
