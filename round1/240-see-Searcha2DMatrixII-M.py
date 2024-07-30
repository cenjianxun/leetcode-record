'''
Write an efficient algorithm that searches for a target value in an m x n integer matrix. The matrix has the following properties:

Integers in each row are sorted in ascending from left to right.
Integers in each column are sorted in ascending from top to bottom.
'''

'''
1. 边缘需要很注意
2. 看其他解法
'''
def searchMatrix(self, matrix, target: int) -> bool:
    m = len(matrix)  
    n = len(matrix[0]) 
    mini = 0
    maxi = m
    for i in range(0, m):
        if target in (matrix[i][n-1], matrix[i][0]):
            return True
        if target > matrix[i][n-1]:
            
            mini = max(mini, i)
        if target < matrix[i][0]:
            print(target, i, matrix[i][0])
            maxi = min(maxi, i)
    minj = 0
    maxj = n 
    for j in range(0, n):
        if target in (matrix[m-1][j], matrix[m-1][0]):
            return True
        if target > matrix[m-1][j]:
            minj = max(minj, j)
        if target < matrix[0][j]:
            maxj = min(maxj, j)
    print(mini, maxi,minj,maxj)
    for i in range(mini, maxi):
        for j in range(minj, maxj):
            if matrix[i][j] == target:
                return True
    return False

'''
暴力？
'''
# faster than 70.57% of Python3
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    return any(target in row for row in matrix)

'''
有序二维矩阵从右上or左下开始
'''
# faster than 53.62% of Python3
def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
    i = len(matrix) - 1
    j = 0
    while j < len(matrix[0]) and i >= 0:
        if matrix[i][j] == target:
            return True
        elif matrix[i][j] < target:
            j = j + 1
        else:
            i = i - 1
    return False