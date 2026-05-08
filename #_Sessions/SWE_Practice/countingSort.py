"""
Limit of numbers is predefined . 
like this error 
arr = [0-10]

use frequency arrr as len will max of the arr 

"""



nums = [2,1,0 , 0 ,4,6,7,6,1]
n= len(nums)

mx = max(nums)

freq = [0]*(mx+1)

for i in nums:
    freq[i] +=1
print("Original array:", nums)


nums = []

for i in range(0,mx+1):
    while freq[i]>0:
        nums.append(i)
        freq[i]-=1

print("Sorted array:", nums)