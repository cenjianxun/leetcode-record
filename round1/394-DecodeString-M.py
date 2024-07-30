'''
394. Decode String

Given an encoded string, return its decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
'''

#  faster than 99.91% of Python3
class Solution:
    def decodeString(self, s: str) -> str:
        res = ''
        i = len(s) - 1
        stack = []
        while i >= 0:
            if s[i] == ']':
                i, sub = self.multi(s[:i + 1], 1)
                res = sub + res
            elif s[i].isalpha():
                res = s[i] + res
            i = i - 1
        return res
    
    def multi(self, s, c):
        i = len(s) - 2
        res = ''
        while c:
            if s[i] == ']':
                i, sub = self.multi(s[:i + 1], 1)
                res = sub + res
            elif s[i].isalpha():
                res = s[i] + res
            elif s[i] == '[':
                c = c - 1
            i = i - 1
        num = s[i]
        while i - 1 >= 0 and s[i - 1].isdigit():
            i = i - 1
            num = s[i] + num
        res = int(num) * res
        return i, res