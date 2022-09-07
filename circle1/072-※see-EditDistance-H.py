'''
72. Edit Distance

Given two strings word1 and word2, return the minimum number of operations required to convert word1 to word2.

You have the following three operations permitted on a word:

Insert a character
Delete a character
Replace a character
'''

'''
插入：dp[i][j-1] + 1
删除：dp[i-1][j] + 1
替换：dp[i-1][j-1] + if i != j

* boolen 可以直接int

误区在于：按动作分类，插入/删除时就表示一定要插入/删除，不用再额外考虑是否相同不必要增删的情况。 因为是否相同和动作不是一个维度的分类，在按动作分类的大前提下，指给其中一个动作就好了，这里指给替换。

！注意循环里word[i-1] 是i-1 不是i
'''

def minDistance(self, word1: str, word2: str) -> int:
    L1, L2 = len(word1), len(word2)
    dp = [[0 for _ in range(L2 + 1)] for _ in range(L1 + 1)]
    for i in range(L2 + 1):
        dp[0][i] = i 
    for i in range(L1 + 1):
        dp[i][0] = i 
    for i in range(1, L1 + 1):
        for j in range(1, L2 + 1):
            dp[i][j] = min(dp[i - 1][j] + 1, dp[i][j - 1] + 1, dp[i - 1][j - 1] + int(word1[i-1] != word2[j-1]))
    return dp[-1][-1]