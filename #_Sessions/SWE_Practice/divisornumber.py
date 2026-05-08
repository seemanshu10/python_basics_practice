# So This is very efficient way to take out the divisors of a number 
# Where THe loop runs till sqrt of number 
# So the each number till range of for loop, so  the number and the qoutient of the number is also added to divisor list 


from math import sqrt

number = 36 
result = []

for i in range(1, int(sqrt(number)) + 1):
    if number % i == 0:
        result.append(i)
        if number // i != i:
            result.append(number // i)

result.sort()
print(result)