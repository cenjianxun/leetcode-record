'''
516. Longest Palindromic Subsequence
Medium

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:

	Input: s = "bbbab"
	Output: 4
	Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:

	Input: s = "cbbd"
	Output: 2
	Explanation: One possible longest palindromic subsequence is "bb".
 
Constraints:

	1 <= s.length <= 1000
	s consists only of lowercase English letters.
'''

'''
不会

将字符串翻转，然后求两个字符串的最长公共子序列就可以了
'''
class Solution(object):
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        dp = [[0] * (n + 1) for i in range(n + 1)]
        ss = s[::-1]

        for i in range(1, n + 1):
            for j in range(1, n + 1):
                if s[i - 1] == ss[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i][j - 1], dp[i - 1][j])
        
        return dp[n][n]

'''
会了
'''
class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        dp = [[0] * len(s) for _ in range(len(s))]
        for i in range(len(s)-1, -1, -1):
            for j in range(i, len(s)):
                if i == j:
                    dp[i][j] = 1
                elif j - i == 1:
                    dp[i][j] = 1 + int(s[i] == s[j])
                else:
                    if s[i] == s[j]:
                        dp[i][j] = dp[i+1][j-1] + 2
                    else:
                        dp[i][j] = max(dp[i+1][j], dp[i][j-1])
                    
            #print(i, s[i], dp)
        return dp[0][-1]