'''
Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
'''

'''
adjacent：邻接的

思路是对的。要注意优化函数的问题
1. 改原函数就行
2. 传参list，可以不用返回
3. 可以精细到每个情况的条件，再往下递归

'''
class Solution:
    def helper(self, i, j, grid, res):
        # print(i, j)
        if i < 0 or i >= len(grid) or j < 0 or j >= len(grid[0]):
            return res
        if grid[i][j] == '1' and res[i*len(grid[0])+j] == '0':
            # print(i,j)
            r = list(res)
            r[i*len(grid[0])+j] = '1'
            res = ''.join(r)
            res = self.helper(i-1,j,grid,res)
            res = self.helper(i+1,j,grid,res)
            res = self.helper(i,j-1,grid,res)
            res = self.helper(i,j+1,grid,res)
        return res
        
    def numIslands(self, grid: List[List[str]]) -> int:
        result = []
        res = '0'*len(grid[0])*len(grid) 
        new_res = res 
        flag = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1' and res[i*len(grid[0])+j] == '0':
                    new_res = self.helper(i, j, grid, res)
                    print(new_res, res)
                    if new_res != res:
                        flag = flag + 1
                        res = new_res
        return flag

# ↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓↓
class Solution:
    def helper(self, i, j, grid):
        grid[i][j] = '0'
        if i-1 >=0 and grid[i-1][j] == '1':
            self.helper(i-1,j, grid)
        if i+1 < len(grid) and grid[i+1][j] == '1':
            self.helper(i+1,j, grid)
        if j-1 >=0 and grid[i][j-1] == '1':
            self.helper(i,j-1, grid)
        if j+1 <len(grid[0]) and grid[i][j+1] == '1':
            self.helper(i,j+1, grid)
        
        
    def numIslands(self, grid: List[List[str]]) -> int:
        count = 0
        for i in range(0, len(grid)):
            for j in range(0, len(grid[0])):
                if grid[i][j] == '1' :
                    count = count + 1
                    self.helper(i,j,grid)
        return count