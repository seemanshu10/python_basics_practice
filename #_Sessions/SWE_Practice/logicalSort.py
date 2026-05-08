"""
Here we take left and right 
Left - start element 
right - end element 
arr = [1,0,2,2,0,1,1,0,2,0]
and will travel from 
will travel to arr but will stop as soon as i == right  
check if the nums[i] < 1:
swap the nums to left and increment i 

if nums[i] > 1 : then swap to right but don't increment i , right negative 1

if nums[i] = 1 just increment i
"""
nums = [1,0,2,2,0,1,1,0,2,0]
left = 0 
right = len(nums)- 1
i =0

print("Original array:", nums)

while i <= right:
    if nums[i] == 1:
        i+=1
    elif nums[i]==0:
        nums[i],nums[left] = nums[left],nums[i]
        i +=1
        left+=1
    else:
        nums[i],nums[right] = nums[right],nums[i]
        right-=1

print("Sorted array:", nums)