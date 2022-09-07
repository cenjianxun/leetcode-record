'''
131. Palindrome Partitioning

Given a string s, partition s such that every substring of the partition is a palindrome. Return all possible palindrome partitioning of s.

A palindrome string is a string that reads the same backward as forward.
'''

# faster than 70.02% of Python3
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.res = []
        self.helper(s, [])
        return self.res
 
    def helper(self, s, path):
        if not s:
            self.res.append(path)
        for i in range(1, len(s)+1):
            if self.isPalindrome(s[:i]):
                self.helper(s[i:], path + [s[:i]])
            
    def isPalindrome(self, s):
        return s == s[::-1]