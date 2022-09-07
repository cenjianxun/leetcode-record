'''
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.
'''

'''
被之前那个题迷惑了 其实思路简单
之前那道题是找最大的，所以更小的就不用考虑
这个要求所有，所以必须从遍历开始入手
'''

# faster than 64.11% of Python3
def countSubstrings(self, s: str) -> int:
    res = 0
    for i in range(len(s)):
        odd = self.helper(s, i, i)
        even = self.helper(s, i, i+1)
        res = res + odd + even
    return res

def helper(self, s, i, j):
    res = 0
    while i >= 0 and j < len(s) and s[i] == s[j]:
        res = res + 1
        i = i - 1
        j = j + 1
    return res


'''
中心扩散法，根据第五题改编
这道题就不能重复了。第五题是求最长可以重复计算。
那么遍历的时候，必须严格定义当前为中心。（再来分奇偶两种情况）
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        
        def countPal(left, right):
            res = 0
            while left >= 0 and right < len(s) and s[left] == s[right]:
                res += 1
                left, right = left - 1, right + 1
            return res 
        
        for i in range(len(s)):
            res += countPal(i, i)
            res += countPal(i, i + 1)
        return res

'''
dp
'''
class Solution:
    def countSubstrings(self, s: str) -> int:
        res = 0
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i < 2 or dp[i+1][j-1]:
                        dp[i][j] = 1
                        res += 1
        return res