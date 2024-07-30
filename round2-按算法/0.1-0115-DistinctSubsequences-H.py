'''
115. Distinct Subsequences

Given two strings s and t, return the number of distinct subsequences of s which equals t.

A string's subsequence is a new string formed from the original string by deleting some (can be none) of the characters without disturbing the remaining characters' relative positions. (i.e., "ACE" is a subsequence of "ABCDE" while "AEC" is not).

It is guaranteed the answer fits on a 32-bit signed integer.
'''

'''
注意是 [i][j-1] + [i-1][j-1]
'''
def numDistinct(self, s: str, t: str) -> int:
    if len(t) > len(s):
        return 0
    dp = [[0 for _ in range(len(s))] for _ in range(len(t))]
    dp[0][0] = 1 if s[0] == t[0] else 0
    for i in range(1, len(s)):
        dp[0][i] = dp[0][i - 1] + int(t[0] == s[j-1])
    
    for i in range(1, len(t)):
        for j in range(i, len(s)):
            if t[i] == s[j]:
                dp[i][j] = dp[i][j-1] + dp[i-1][j-1]
            else:
                dp[i][j] = dp[i][j-1]
    return dp[-1][-1]

'''
dp[i][j]表示以 i-1 为结尾的 s 子序列中出现以 j−1 为结尾的 t 的个数为 dp[i][j]
如果s[i] != t[j]：
    s[i−1] 不能和 t[j-1] 匹配，因此只考虑 t[j-1] 作为 s[i-2] 的子序列，子序列个数为 dp[i-1][j] 
如果末尾项一样 (s[i]=t[j])，dp[i][j]的来源有两部份：
    如果 s[i-1] 和 t[j-1] 匹配，则考虑 t[j-1] 作为 s[i-1] 的子序列，子序列个数为 dp[i-1][j-1]；
    如果 s[i-1] 不和 t[j-1] 匹配，则考虑 t[j-1] 作为 s[i-2] 的子序列，子序列个数为 dp[i-1][j]。
综合以上两种情况：dp[i][j] = dp[i-1][j-1] + dp[i - 1][j] 
'''