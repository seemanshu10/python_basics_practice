def factorial(num):
    if num == 0 or num == 1:
        return 1
    
    return num * factorial(num - 1)

fact = factorial(5)
print(fact)

# Time O(n)
# Space O(n) - this is a stack space as using recursion 