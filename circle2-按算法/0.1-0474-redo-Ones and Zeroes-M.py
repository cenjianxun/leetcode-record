'''
474. Ones and Zeroes
Medium

You are given an array of binary strings strs and two integers m and n.

Return the size of the largest subset of strs such that there are at most m 0's and n 1's in the subset.

A set x is a subset of a set y if all elements of x are also elements of y.

Example 1:

	Input: strs = ["10","0001","111001","1","0"], m = 5, n = 3
	Output: 4
	Explanation: The largest subset with at most 5 0's and 3 1's is {"10", "0001", "1", "0"}, so the answer is 4.
	Other valid but smaller subsets include {"0001", "1"} and {"10", "1", "0"}.
	{"111001"} is an invalid subset because it contains 4 1's, greater than the maximum of 3.

Example 2:

	Input: strs = ["10","0","1"], m = 1, n = 1
	Output: 2
	Explanation: The largest subset is {"0", "1"}, so the answer is 2.
 
Constraints:

	1 <= strs.length <= 600
	1 <= strs[i].length <= 100
	strs[i] consists only of digits '0' and '1'.
	1 <= m, n <= 100
'''

'''
dfs超时
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        zeros_and_ones = [[0,0] for i in range(len(strs))]
        for i in range(len(strs)):
            zeros_and_ones[i] = [strs[i].count('0'), strs[i].count('1')]
        
        largest = 0
        def dfs(start, subset, count, largest):
            if count[0] > m or count[1] > n:
                return largest
            largest = max(largest, len(subset))
            #print(start, subset, largest)
            for i in range(start, len(strs)):
                zeros, ones = zeros_and_ones[i]
                largest = dfs(i+1, subset + [strs[i]], [count[0]+zeros, count[1]+ones], largest)
            return largest
        
        largest = dfs(0, [], [0,0], largest)
        return largest

'''
三层dp
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[[0] * (n+1) for j in range(m+1)] for i in range(l+1)]
        for i in range(1, l+1):
            zeros, ones = strs[i-1].count('0'), strs[i-1].count('1')
            for j in range(m+1):
                for k in range(n+1):
                    if j < zeros or k < ones:
                        dp[i][j][k] = dp[i-1][j][k]
                    else:
                        dp[i][j][k] = max(dp[i-1][j][k], dp[i-1][j-zeros][k-ones] + 1)
        return dp[l][m][n]

'''
滚动压缩
'''
class Solution:
    def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
        l = len(strs)
        dp = [[0] * (n+1) for i in range(m+1)] 
        for s in strs:
            zeros, ones = s.count('0'), s.count('1')
            for i in range(m, zeros-1, -1):
                for j in range(n, ones-1, -1):
                    dp[i][j] = max(dp[i][j], dp[i-zeros][j-ones]+1)
        return dp[m][n]