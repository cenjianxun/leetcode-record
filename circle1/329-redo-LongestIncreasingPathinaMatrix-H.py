'''
Given an m x n integers matrix, return the length of the longest increasing path in matrix.

From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).

'''

'''
慢 faster than 9.04% of Python3
'''

def addone(self, i, j, matrix):
    result = ''
    # print(matrix[i][j], matrix)
    if isinstance(matrix[i][j], str):
        return 
    if i-1>=0:
        # print([matrix[i-1][j], matrix[i][j]])
        if isinstance(matrix[i-1][j], int) and matrix[i-1][j] > matrix[i][j]:
            self.addone(i-1, j, matrix)
        if isinstance(matrix[i-1][j], str) and int(matrix[i-1][j].split('-')[0]) > matrix[i][j]:
            result = matrix[i-1][j] if matrix[i-1][j].count('-') > result.count('-') else result
    if j-1>=0:
        if isinstance(matrix[i][j-1], int) and matrix[i][j-1] > matrix[i][j]:
            self.addone(i, j-1, matrix)
        if isinstance(matrix[i][j-1], str) and int(matrix[i][j-1].split('-')[0]) > matrix[i][j]:
            result = matrix[i][j-1] if  matrix[i][j-1].count('-')  > result.count('-') else result
    if i+1<len(matrix):
        if isinstance(matrix[i+1][j], int) and matrix[i+1][j] > matrix[i][j]:
            self.addone(i+1, j, matrix)
        if isinstance(matrix[i+1][j], str) and int(matrix[i+1][j].split('-')[0]) > matrix[i][j]:
            result = matrix[i+1][j] if matrix[i+1][j].count('-') > result.count('-') else result
    if j+1<len(matrix[0]):
        if isinstance(matrix[i][j+1], int) and matrix[i][j+1] > matrix[i][j]:
            self.addone(i, j+1, matrix)
        if isinstance(matrix[i][j+1], str) and int(matrix[i][j+1].split('-')[0]) > matrix[i][j]:
            result = matrix[i][j+1] if matrix[i][j+1].count('-') > result.count('-') else result
    matrix[i][j] = str(matrix[i][j]) + '-' + result  
    
def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
    result = 0
    for i in range(0, len(matrix)):
        for j in range(0, len(matrix[0])):
            self.addone(i,j,matrix)
            result = max(result, matrix[i][j].count('-'))
    # print(matrix)
    return result


#----------dfs-----------------------
# faster than 44.40% of Python3
class Solution:
    def dfs(self, matrix, i, j, dp):
        if dp[i][j]:
            return dp[i][j]
        
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0 <= x < len(matrix) and 0 <= y < len(matrix[0]) and matrix[x][y] > matrix[i][j]:
                dp[i][j] = max(dp[i][j], self.dfs(matrix, x, y, dp))
        dp[i][j] = dp[i][j] + 1
        return dp[i][j]
            
        
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0
        result = 0
 
        dp = [[0] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(0, len(matrix)):
            for j in range(0, len(matrix[0])):
                result = max(result, self.dfs(matrix, i, j, dp))
        # print(matrix)
        return result



'''

dfs 超时
'''
class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        self.res = 0
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                print(i,j)
                self.helper(i, j, matrix, [matrix[i][j]])
        return self.res
        
    def helper(self, i, j, matrix, stack):
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=x<len(matrix) and 0<=y<len(matrix[0]) and matrix[x][y] > stack[-1]:
                self.helper(x,y,matrix,stack+[matrix[x][y]])
            else:
                self.res = max(self.res, len(stack))


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        dp = [[1] * len(matrix[0]) for _ in range(len(matrix))]
        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                self.helper(i, j, matrix, dp)
                
        return max([max(row) for row in dp])
    
    def helper(self, i, j, matrix, dp):
        for x, y in [(i-1,j),(i+1,j),(i,j-1),(i,j+1)]:
            if 0<=x<len(matrix) and 0<=y<len(matrix[0]):
                if matrix[x][y] > matrix[i][j]:
                    dp[x][y] = max(dp[x][y], dp[i][j] + 1)
                    self.helper(x, y, matrix, dp)