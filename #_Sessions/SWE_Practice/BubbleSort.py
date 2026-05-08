"""
Docstring for BubbleSort
"""

nums = [2,8,9,1,3,4]

for i in range(len(nums)):
    isSwap = False
    for j in range(len(nums)-i-1):
        if nums[j]>nums[j+1]:
            # swap 
            temp = nums[j]
            nums[j] = nums[j+1]
            nums[j+1] = temp
    if not isSwap:
        break
print(nums)
