'''
44. Wildcard Matching

Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*' where:

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).
The matching should cover the entire input string (not partial).
'''

'''
直接过了
'''
#  
def isMatch(self, s: str, p: str) -> bool:
    dp = [[0 for _ in range(len(p)+1)] for _ in range(len(s)+1)]
    dp[0][0] = 1
    for i in range(len(p)):
        if p[i] == '*':
            dp[0][i+1] = dp[0][i]
    for i in range(len(s)):
        for j in range(len(p)):
            if p[j] in (s[i], '?'):
                dp[i+1][j+1] = dp[i][j]
            elif p[j] == '*':
                dp[i+1][j+1] = dp[i][j+1] or dp[i+1][j]
    print(dp)  
    return dp[-1][-1]