'''
1092. Shortest Common Supersequence

Given two strings str1 and str2, return the shortest string that has both str1 and str2 as subsequences. If there are multiple valid strings, return any of them.

A string s is a subsequence of string t if deleting some number of characters from t (possibly 0) results in the string s.
'''

def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
    dp = [['' for _ in range(len(str2) + 1)] for _ in range(len(str1) + 1)]
    for i in range(1, len(str2) + 1):
        dp[0][i] = dp[0][i - 1] + str2[i - 1]
    for i in range(1, len(str1) + 1):
        dp[i][0] = dp[i - 1][0] + str1[i - 1]
    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + str1[i - 1]
            else:
                if len(dp[i - 1][j]) < len(dp[i][j - 1]):
                    dp[i][j] = dp[i - 1][j] + str1[i - 1]
                else:
                    dp[i][j] = dp[i][j - 1] + str2[j - 1]
    return dp[-1][-1]

'''
其实不懂为嘛下面的就不超时了，仍然是m*n
区别就是dp里面存的东西的长度。好吧 还要比较
答案👇
''' 

def shortestCommonSupersequence(self, A: str, B: str) -> str:
    res, i, j = "", 0, 0
    for c in self.longestCommonSubsequence(A, B):
        while A[i] != c:
            res += A[i]
            i += 1
        while B[j] != c:
            res += B[j]
            j += 1
        res+=c; i+=1; j+=1
    return res + A[i:] + B[j:]

def longestCommonSubsequence(self, A: str, B: str) -> str:
    n, m = len(A), len(B)
    dp = [["" for _ in range(m + 1)] for _ in range(n + 1)]
    for i in range(n):
        for j in range(m):
            if A[i] == B[j]:
                dp[i + 1][j + 1] = dp[i][j] + A[i]
            else:
                dp[i + 1][j + 1] = max(dp[i + 1][j], dp[i][j + 1], key=len)
    #print(dp)
    return dp[-1][-1]