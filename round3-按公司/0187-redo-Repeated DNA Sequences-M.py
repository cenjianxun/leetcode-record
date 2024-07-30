'''
187. Repeated DNA Sequences
Medium

The DNA sequence is composed of a series of nucleotides abbreviated as 'A', 'C', 'G', and 'T'.

For example, "ACGAATTCCG" is a DNA sequence.
When studying DNA, it is useful to identify repeated sequences within the DNA.

Given a string s that represents a DNA sequence, return all the 10-letter-long sequences (substrings) that occur more than once in a DNA molecule. You may return the answer in any order.

Example 1:

	Input: s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
	Output: ["AAAAACCCCC","CCCCCAAAAA"]

Example 2:

	Input: s = "AAAAAAAAAAAAA"
	Output: ["AAAAAAAAAA"]
 

Constraints:

	1 <= s.length <= 105
	s[i] is either 'A', 'C', 'G', or 'T'.
'''

'''
暴力超时
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        res = set()
        start, l = 0, 1 
        while start + 10 <= len(s):
            if s[start:start+10] in res:
                continue
            while l + 10 <= len(s):
                if s[start:start+10] == s[l:l+10]:
                    res.add(s[l:l+10])
                    break
                else:
                    l += 1
            start += 1
            l = start + 1
        return res

'''
无语
and 注意range的范围
'''
class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        from collections import defaultdict
        res = []
        count = defaultdict(int)
        for i in range(len(s)-10+1):
            count[s[i:i+10]] += 1
            if count[s[i:i+10]] == 2:
                res.append(s[i:i+10])
        return res