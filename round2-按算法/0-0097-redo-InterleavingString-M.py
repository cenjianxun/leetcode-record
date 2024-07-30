'''
97. Interleaving String

Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

An interleaving of two strings s and t is a configuration where they are divided into non-empty substrings such that:

s = s1 + s2 + ... + sn
t = t1 + t2 + ... + tm
|n - m| <= 1
The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...
'''

'''
无语
'''
def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
    if len(s1) + len(s2) != len(s3):
        return False
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

    
    for i in range(len(s1)+1):
        for j in range(len(s2)+1):
            if i == 0 and j == 0:
                dp[i][j] = 1
            elif i == 0:
                dp[i][j] = dp[i][j-1] and s2[j-1] == s3[j-1]
            elif j == 0:
                dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
            else:
                dp[i][j] = ((dp[i-1][j] and s1[i-1] == s3[i+j-1]) or 
                            (dp[i][j-1] and s2[j-1] == s3[i+j-1]))
    return dp[-1][-1]