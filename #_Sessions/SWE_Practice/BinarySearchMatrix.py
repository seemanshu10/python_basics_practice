"""
Matrix binary search here we assume that values should be sorted and we assume the index number for each cell 


"""
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12]
]

rows = len(matrix)
cols = len(matrix[0])

l = 0
r = rows * cols - 1   # IMPORTANT: total elements - 1

target = 10

while l <= r:
    mid = (l + r) // 2

    # Convert 1D index to 2D index
    row = mid // cols
    col = mid % cols

    if matrix[row][col] == target:
        print("Number found at:", row, col)
        break

    elif matrix[row][col] > target:
        r = mid - 1
    else:
        l = mid + 1
else:
    print("No number found")