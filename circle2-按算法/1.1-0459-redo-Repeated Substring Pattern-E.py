'''
459. Repeated Substring Pattern
Easy

Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

Example 1:

	Input: s = "abab"
	Output: true
	Explanation: It is the substring "ab" twice.

Example 2:

	Input: s = "aba"
	Output: false

Example 3:

	Input: s = "abcabcabcabc"
	Output: true
	Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 
Constraints:

	1 <= s.length <= 104
	s consists of lowercase English letters.
'''

'''
假设s = [xyz] * k
那么s + s = [xyz] + [xyz] * (2*K-2) + [xyz]
掐头去尾：[x🔹(yz] + [xyz] * (2*k-2) +[x)🔹yz]
如果s 在 掐头去尾的s+s里则有：
2k-2 >= k   ====>   k >= 2，意思是s必须是一个重复串


and KMP:
'''
class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        return True if s in s[1:] + s[:-1] else False