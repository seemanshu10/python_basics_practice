"""
in this we select an element probably min or max and then that mn number is removed from that arr and moved 
in front of the array 

space - O(1)
time - o(n^2)
"""


nums = [4,1,3,9,7,2,1]
#nums = [1,3,4,8,4]
n = len(nums)


for i in range(n):
    min_index = i
    for j in range(i+1,n):
        if nums[j]<nums[min_index]:
            min_index=j
        
        nums[i],nums[min_index]=nums[min_index],nums[i]

print(nums)
