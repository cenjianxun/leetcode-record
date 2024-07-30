'''
221. Maximal Square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.
'''

def maximalSquare(self, matrix: List[List[str]]) -> int:
    area = 0
    m, n = len(matrix), len(matrix[0])
    # R = min(m, r)
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                r = 1
                while i + r < m and j + r < n and self.getArea(matrix, i, j, r):
                    r = r + 1
                # print(i, j, r)
                area = max(area, r * r)
                # i, j = i + r, j + r
                
    return area
                
def getArea(self, matrix, i, j, R):
    if matrix[i + R][j + R] == '0':
        return 0
    for r in range(R):
        if matrix[i + r][j + R] == '0' or matrix[i + R][j + r] == '0':
            return 0
    return 1

'''
dp

看看dp使用的多种方式，dp完了再找大的 and map的用法

注意是左 上 左上都要考虑
'''
def maximalSquare(self, matrix: List[List[str]]) -> int:
     
    m, n = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
    
    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dp[i+1][j+1] = min(dp[i+1][j], dp[i][j+1], dp[i][j]) + 1

    # print(dp)          
    return max(map(max, dp)) ** 2