"""
array should be sorted 

taking middle of the array and deciding where the target should be on the left or right side of this middle 
check if target is middle then return the numaber found found 
and if not found 

then if the target is less than middle shift the right to mid-1 and then again do same 
if is in right the move left to mid +1 
do it till l = r that means same position 

"""

nums = [3,4 ,5,7,10,12,15,25,26,30,45]

left = nums[0]
right = len(nums)-1

target = 26
while left <= right:

    mid = (left+right)//2
    
    if target == nums[mid]:
        print("Number found at :",mid)
        break

    elif target < nums[mid]:
        # left side 
        right = mid-1

    else : 
        # right side 
        left = mid+1

else:
    print("Number not in array")