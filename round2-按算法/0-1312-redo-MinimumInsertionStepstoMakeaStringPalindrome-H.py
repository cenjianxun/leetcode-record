'''
1312. Minimum Insertion Steps to Make a String Palindrome

Given a string s. In one step you can insert any character at any index of the string.

Return the minimum number of steps to make s palindrome.

A Palindrome String is one that reads the same backward as well as forward.
'''

'''
回文基本思想：
1 从中间到两边
2 二维数组ij表示index i到j

为什么错：
1. (0 if j+1 < n and s[i] == s[j+1] else 1) 这里
在往外扩充的时候，应该在i-j范围内比较，不能把i-1，j+1拉出来。即肯定是+1的了，不存在+0

2. if i+1 <= j-1: 这里
如果是相邻相等，就会漏掉
'''
def minInsertions(self, s: str) -> int:
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            # 错的分法：
            # dp[i][j] = min(dp[i+1][j] + (0 if j+1 < n and s[i] == s[j+1] else 1),
            #               dp[i][j-1] + (0 if i > 0 and s[i-1] == s[j] else 1))
            # if i+1 <= j-1:
            #     dp[i][j] = min(dp[i][j], 
            #                    dp[i+1][j-1] + (0 if s[i] == s[j] else 2))
    return dp[0][-1]

'''
so正确版本：只用分s[i]是否=s[j]
'''

def minInsertions(self, s: str) -> int:
    n = len(s)
    dp = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n - 1, -1, -1):
        for j in range(i + 1, n):
            if s[i] == s[j]:
                dp[i][j] = dp[i+1][j-1]
            else:
                dp[i][j] = min(dp[i+1][j], dp[i][j-1]) + 1
 
    # print(dp)
    return dp[0][-1]