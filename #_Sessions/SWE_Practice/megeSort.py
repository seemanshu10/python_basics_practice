"""
Merge Sort Algorithm
Divide and Conquer approach
Time Complexity: O(n log n)
Space Complexity: O(n)
"""

def merge(nums, l, mid, r):
    # Temporary arrays
    left = []
    right = []

    # Copy data to temporary arrays
    for i in range(l, mid + 1):
        left.append(nums[i])

    for j in range(mid + 1, r + 1):
        right.append(nums[j])

    i = 0      # Initial index of left subarray
    j = 0      # Initial index of right subarray
    k = l      # Initial index of merged subarray

    # Merge the temp arrays back into nums[l..r]
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1

    # Copy remaining elements of left[] if any
    while i < len(left):
        nums[k] = left[i]
        i += 1
        k += 1

    # Copy remaining elements of right[] if any
    while j < len(right):
        nums[k] = right[j]
        j += 1
        k += 1


def mergeSort(nums, l, r):
    # Base case
    if l >= r:
        return

    # Find middle point
    mid = (l + r) // 2

    # Sort first and second halves
    mergeSort(nums, l, mid)
    mergeSort(nums, mid + 1, r)

    # Merge the sorted halves
    merge(nums, l, mid, r)


# Driver code
nums = [8, 2, 18, 5, 4, 1, 4, 99]

print("Original array:", nums)

mergeSort(nums, 0, len(nums) - 1)

print("Sorted array:", nums)