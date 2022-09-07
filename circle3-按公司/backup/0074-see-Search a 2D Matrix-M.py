'''
74. Search a 2D Matrix

Write an efficient algorithm that searches for a value target in an m x n integer matrix matrix. This matrix has the following properties:

Integers in each row are sorted from left to right.
The first integer of each row is greater than the last integer of the previous row.
'''

'''
时间复杂度是log（mn）

注意while有等号，然后l是+1，r是-1
'''
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m, n = len(matrix), len(matrix[0])
        mid = m * n // 2
        l, r = 0, m * n - 1
        while l <= r:
            i, j = mid//n, mid%n
            if matrix[i][j] == target:
                return True
            if matrix[i][j] < target:
                l = mid + 1
            else:
                r = mid - 1
            mid = (l + r)//2
        return False