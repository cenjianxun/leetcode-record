'''
764. Largest Plus Sign
Medium

You are given an integer n. You have an n x n binary grid grid with all values initially 1's except for some indices given in the array mines. The ith element of the array mines is defined as mines[i] = [xi, yi] where grid[xi][yi] == 0.

Return the order of the largest axis-aligned plus sign of 1's contained in grid. If there is none, return 0.

An axis-aligned plus sign of 1's of order k has some center grid[r][c] == 1 along with four arms of length k - 1 going up, down, left, and right, and made of 1's. Note that there could be 0's or 1's beyond the arms of the plus sign, only the relevant area of the plus sign is checked for 1's.

Example 1:

	Input: n = 5, mines = [[4,2]]
	Output: 2
	Explanation: In the above grid, the largest plus sign can only be of order 2. One of them is shown.

Example 2:

	Input: n = 1, mines = [[0,0]]
	Output: 0
	Explanation: There is no plus sign, so return 0.

Constraints:

	1 <= n <= 500
	1 <= mines.length <= 5000
	0 <= xi, yi < n
	All the pairs (xi, yi) are unique.
'''

'''
坑点竟然是 二层里面是list。就不能 [] * n,而是要[ for _ in range(n)]

倒回来时候是比较i+1和i-1
''' 
class Solution:
    def orderOfLargestPlusSign(self, n: int, mines: List[List[int]]) -> int:
        dp = [[[1, 1] for _ in range(n)]  for _ in range(n)]
        largest = 0
        for x, y in mines:
            dp[x][y][0], dp[x][y][1] = 0, 0
        for i in range(n):
            for j in range(n):
                if dp[i][j][0] and dp[i][j][1]:
                    if i == 0:
                        dp[i][j][0] = 1
                    else:
                        dp[i][j][0] = dp[i-1][j][0] + 1
                    if j == 0:
                        dp[i][j][1] = 1
                    else:
                        dp[i][j][1] = dp[i][j-1][1] + 1
                    
        #print(dp)
        for i in range(n-1, -1, -1):
            for j in range(n-1, -1, -1):
                if dp[i][j][0] and dp[i][j][1]:
                    if i == n-1:
                        dp[i][j][0] = 1
                    elif i > 0:
                        dp[i][j][0] = min(dp[i+1][j][0], dp[i-1][j][0]) + 1
                    if j == n-1:
                        dp[i][j][1] = 1
                    elif j > 0:
                        dp[i][j][1] = min(dp[i][j-1][1], dp[i][j+1][1]) + 1
                    largest = max(largest, min(dp[i][j]))
        #print(dp)
        return largest