'''
Given a string s, return the longest palindromic substring in s.
'''

'''
一直超时 我也是不懂了
so 这个方法还是超时↓
'''


def longestPalindrome(s):
    substr = ''
    res = s[::-1]
    i = 0 
    l = len(s)
    j = l

    while i < len(s):
        # print(i, s[i:j], res[l-j:l-i], j-i, len(substr))
        if s[i:j] == res[l-j:l-i] and j-i > len(substr):
            substr = s[i:j]
        if j > i + 1:
            j = j - 1
        else:
            i = i + 1
            j = len(s)
    return substr

s = longestPalindrome("qatotpbvogjjgzotghxdrpdzyy")
print('::',s)

'''
基本思路是对任意字符串，如果头和尾相同，那么它的最长回文子串一定是去头去尾之后的部分的最长回文子串加上头和尾。如果头和尾不同，那么它的最长回文子串是去头的部分的最长回文子串和去尾的部分的最长回文子串的较长的那一个。

这个方法 的点在于：
1. 第二个if是入口，当str有1个字符or两个字符时进入
当有1个以上字符符合条件时，进入第一个if
2. 是往后推的，i始终往前走的，start是往后推的，所以距离一次进两步，i始终指向的是尾边界的那个str
3. 关于可不可以遍历所有情况的问题：因为maxl的值是不断变大的，所以后面有可能的结果，只有比当前的距离大，才会进入循环
'''

def longestPalindrome(s: str) -> str:
    maxl = 0
    start = 0
    for i in range(len(s)):
        if i - maxl > 0 and s[i-maxl-1:i+1] == s[i-maxl-1:i+1][::-1]:
            start = i - maxl - 1
            print('0:', i, maxl, s[i-maxl-1:i+1], start)
            maxl = maxl + 2
            continue
        if i - maxl >= 0 and s[i-maxl:i+1] == s[i-maxl:i+1][::-1]:
            start = i - maxl
            print('1:', i, maxl, s[i-maxl:i+1], start)
            maxl = maxl + 1
    return s[start:start+maxl]

'''
220728

找回文子串：中心扩散法。就是马拉车？

遍历每个char，先看左边和本char相不相等，再看右边和本char相不相等，最后看左边和右边相不相等
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        res = ''
        for i in range(len(s)):
            left, right = i-1, i+1
            while left >= 0 and s[left] == s[i]:
                left -= 1
            while right < len(s) and s[right] == s[i]:
                right += 1
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left, right = left - 1, right + 1
            #print(i, left, right)
            if right - left - 1 > len(res):
                res = s[left+1:right]
        return res

'''
动态规划：
设dp[i][j]的值为从i到j是不是回文
那么转移方程就是：如果s[i-1] == s[j+1] 且 dp[i][j] = True, 那么dp[i-1][j+1] = True
换算成求dp[i][j]，就移成 dp[i+1][j-1] ——> dp[i][j]
但无论如何，在二维矩阵中，这个方向都是【从左下到右上】。

如果不等，就是false，但是当s[i] == s[j]时，就要分具体分情况
① i = j
② j = i + 1
③ 更长，这时就需要看[i+1, j-1]的情况了
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        start, maxLen = 0, 1
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s) - 1, -1, -1):
            for j in range(i, len(s)):
                if s[i] == s[j]:
                    if j - i < 2 or dp[i+1][j-1]:
                        dp[i][j] = 1
                        if j - i + 1 > maxLen:
                            start, maxLen = i, j - i + 1
        return s[start:start + maxLen]
        
'''
提升性能：不用截取string，而是记录长度和起始位置，因为截取string需要耗费时间
'''