'''
409. Longest Palindrome
Easy

Given a string s which consists of lowercase or uppercase letters, return the length of the longest palindrome that can be built with those letters.

Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

Example 1:

	Input: s = "abccccdd"
	Output: 7
	Explanation: One longest palindrome that can be built is "dccaccd", whose length is 7.

Example 2:

	Input: s = "a"
	Output: 1
	Explanation: The longest palindrome that can be built is "a", whose length is 1.

Constraints:

1 <= s.length <= 2000
s consists of lowercase and/or uppercase English letters only.
'''

'''
奇数个的char不是整个都不能用！而是可以-1再全部用进去

注意if后面，第一次用了 if c%2 and c > odd: xxx else: xxx 是错的
'''
class Solution:
    def longestPalindrome(self, s: str) -> int:
        count = Counter(s)
        res = 0
        odd = 0
        for char, c in count.items():
            if c % 2:
                odd = 1
                c = c - 1
                res += c
            print(char, c, res, odd)
        return res + odd