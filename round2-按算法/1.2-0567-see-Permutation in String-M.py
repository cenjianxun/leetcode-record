'''
567. Permutation in String
Medium

Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

In other words, return true if one of s1's permutations is the substring of s2.

Example 1:

	Input: s1 = "ab", s2 = "eidbaooo"
	Output: true
	Explanation: s2 contains one permutation of s1 ("ba").
Example 2:

	Input: s1 = "ab", s2 = "eidboaoo"
	Output: false
 
Constraints:

	1 <= s1.length, s2.length <= 104
	s1 and s2 consist of lowercase English letters.
'''

'''
固定窗口的滑动
比较每个char的频次，可以比较map
'''
class Solution:
    def checkInclusion(self, subS: str, S: str) -> bool:
        from collections import Counter
        subCount = Counter(subS)
        subLen = len(subS)
        left = 0
        print(subCount)
        while left + subLen <= len(S):
            if S[left] in subCount:
                count = Counter(S[left:left+subLen])
                #print(S[left],S[left:left+subLen])
                if count == subCount:
                    return True
            left += 1
        return False  