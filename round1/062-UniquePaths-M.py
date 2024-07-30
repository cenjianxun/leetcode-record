'''
A robot is located at the top-left corner of a m x n grid (marked 'Start' in the diagram below).

The robot can only move either down or right at any point in time. The robot is trying to reach the bottom-right corner of the grid (marked 'Finish' in the diagram below).

How many possible unique paths are there?
'''

'''
动态规划
'''

def uniquePaths(m: int, n: int) -> int:
    mat = [[0]*n for i in range(m)]
    for i in range(n):
        mat[0][i] = 1
    for i in range(m):
        mat[i][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            mat[i][j] = mat[i-1][j] + mat[i][j-1]
    return mat[m-1][n-1]