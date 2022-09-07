'''
583. Delete Operation for Two Strings

Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.

In one step, you can delete exactly one character in either string.
'''

'''
可以算最大公共串
也可以算最少删除串

如果相等，直接是 = [i-1][j-1]
'''
def minDistance(self, word1: str, word2: str) -> int:
    dp = [[i + j for j in range(len(word2)+1)] for i in range(len(word1)+1)]

    for i in range(1, len(word1)+1):

        for j in range(1, len(word2)+1):
            if word1[i-1] != word2[j-1]:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + 1
            else:
                dp[i][j] = dp[i-1][j-1]
    
        # print(i, dp[i])
    return dp[-1][-1]