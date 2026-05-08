"""
Choose one number and insert that number in its correct place

space - O(1)
time - O(n^2)
"""

nums = [4,1,3,9,7,2,1]
#nums = [1,3,4,8,4]
n = len(nums)

for i in range(1,n):
    key = nums[i]
    j = i-1
    while j<=0 and nums[j]>key:
        nums[j+1]=nums[j]
        j-=1
    nums[j+1]=key

print(nums)
