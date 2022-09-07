'''
1139. Largest 1-Bordered Square
Medium

Given a 2D grid of 0s and 1s, return the number of elements in the largest square subgrid that has all 1s on its border, or 0 if such a subgrid doesn't exist in the grid.

Example 1:

    Input: grid = [[1,1,1],[1,0,1],[1,1,1]]
    Output: 9

Example 2:

    Input: grid = [[1,1,0,0]]
    Output: 1

Constraints:

    1 <= grid.length <= 100
    1 <= grid[0].length <= 100
    grid[i][j] is 0 or 1
'''

'''
注意初始max_edge = -1
如果用前缀和，idea是和=从开始到结束的长度
如果用动态规划需要两个二维数组分别记录长和宽till目前的状态
'''
class Solution:
    def largest1BorderedSquare(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        max_edge = -1
        for i in range(m):
            for j in range(n):
                edge = max_edge
                while i + edge < m and j + edge < n:
                    if self.isValid(i, j, edge, grid):
                        max_edge = max(max_edge, edge)
                    edge += 1
        return (max_edge + 1) ** 2
                    
    
    def isValid(self, i, j, edge, grid):

        for x in range(i, i + edge + 1):
            if grid[x][j] == 0 or grid[x][j+edge] == 0:
                return False
        for y in range(j, j + edge + 1):
            if grid[i][y] == 0 or grid[i+edge][y] == 0:
                return False
        return True