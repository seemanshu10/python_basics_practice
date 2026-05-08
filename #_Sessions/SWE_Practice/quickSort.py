"""
How It Works
Choose a pivot element from the array.
Partition the array:

Elements smaller than the pivot → left side
Elements greater than the pivot → right side

Recursively apply the same process to the left and right subarrays.

space - O(1)
time - O(n^2)
        average (nlogn)
"""
def partition(nums, l, r):
    key = nums[r]          # pivot
    start = l

    for i in range(l, r):  # go only till r-1
        if nums[i] <= key:
            nums[i], nums[start] = nums[start], nums[i]
            start += 1

    # place pivot in correct position
    nums[start], nums[r] = nums[r], nums[start]

    return start


def quickSort(nums, l, r):
    # base case
    if l >= r:
        return

    p = partition(nums, l, r)

    quickSort(nums, l, p - 1)
    quickSort(nums, p + 1, r)


# Driver code
nums = [8, 2, 18, 5, 4, 1, 4, 99]

print("Original array:", nums)

quickSort(nums, 0, len(nums) - 1)

print("Sorted array:", nums)