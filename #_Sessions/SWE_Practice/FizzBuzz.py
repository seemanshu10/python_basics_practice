"""
Given an integer n, return a string array answer (1-indexed) where:

answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
answer[i] == "Fizz" if i is divisible by 3.
answer[i] == "Buzz" if i is divisible by 5.
answer[i] == i (as a string) if none of the above conditions are true.

"""
# taking input 
num = input("Input then numbers with a space :" )
split_num = num.split()
# mapping the input and convcert to integer  
nums =map(int,split_num)
list_num = list(nums)
print(list_num) 
result = []
# fizz buzz logic 
for i in list_num:
    if i%3==0 and i%5==0:
        result.append("FizzBuzz")
    elif i%3==0:
        result.append("Fizz")
    elif i%5==0:
        result.append("Buzz")
    else:
        result.append(str(i))

print (result)    
