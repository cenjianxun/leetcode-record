'''
712. Minimum ASCII Delete Sum for Two Strings

Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.
'''

'''
注意ord的比较，默认max是比较第一个字符而已，所以要自己写比较函数
'''
def minimumDeleteSum(self, s1: str, s2: str) -> int:
    dp = [['' for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    res = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + s1[i - 1]
            else:
                dp[i][j] = self.comp(dp[i - 1][j], dp[i][j - 1])
            # print(i,  s1[i-1], j, s2[j-1], dp[i][j])
    # print(dp)
    for s in dp[-1][-1]:
        res = res - ord(s) * 2
    for s in s1:
        res = res + ord(s)
    for s in s2:
        res = res + ord(s)
    return res

def comp(self, s1, s2):
    res1 = res2 = 0
    for s in s1:
        res1 = res1 + ord(s)
    for s in s2:
        res2 = res2 + ord(s)
    return s1 if res1 > res2 else s2

'''
改进 直接存值可
'''
def minimumDeleteSum(self, s1: str, s2: str) -> int:
    dp = [[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]
    res = 0
    for i in range(1, len(s1) + 1):
        for j in range(1, len(s2) + 1):
            if s1[i - 1] == s2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1] + ord(s1[i - 1])
            else:
                dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
            # print(i,  s1[i-1], j, s2[j-1], dp[i][j])

    for s in s1:
        res = res + ord(s)
    for s in s2:
        res = res + ord(s)
    return res - 2 * dp[-1][-1]