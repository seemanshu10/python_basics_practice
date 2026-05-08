"""
Sorted array but has peek value in between 

arr = [0,2,4,7,5,1] peeke element or max is 7 
"""

nums = [0,2,4,7,5,1]
n = len(nums)
l = 0
r = n-2

ans = n-1

while l<=r:
    mid = (l+r)//2
    if nums[mid] < nums[mid+1]:
        # right 
        l = mid+1

    else:
        ans = mid
        # left 
        r = mid-1

print(ans)