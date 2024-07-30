'''
64. Minimum Path Sum

Given a m x n grid filled with non-negative numbers, find a path from top left to bottom right, which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.
'''

'''
dp
'''

# faster than 78.59% of Python3
def minPathSum(self, grid: List[List[int]]) -> int:
    dp = [[0 for _ in range(len(grid[0]))] for _ in range(len(grid))]
    dp[0][0] = grid[0][0]
    for i in range(1, len(grid[0])):
        dp[0][i] = dp[0][i - 1] + grid[0][i]
    for i in range(1, len(grid)):
        dp[i][0] = dp[i - 1][0] + grid[i][0]
    for i in range(1, len(grid)):
        for j in range(1, len(grid[0])):
            dp[i][j] = min(dp[i][j-1], dp[i-1][j]) + grid[i][j]
    return dp[-1][-1]