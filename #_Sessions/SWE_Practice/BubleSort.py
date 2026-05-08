"""
in this sort the largest number is moved
to correct poition and one elements is compared to the next element if it is less then swapped both of thier positions

"""

nums = [4,1,3,9,7,2,1]
#nums = [1,3,4,8,4]
n = len(nums)

for i in range(n-1):
    isSwap = False
    for j in range(n-i-1):
        if nums[j]>nums[j+1]:
            # swap 
            nums[j],nums[j+1]=nums[j+1],nums[j]
            isSwap = True
    
    if not isSwap:
        print(f"I ran",i)
        break

print(nums)


