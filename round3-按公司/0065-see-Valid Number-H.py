'''
65. Valid Number

A valid number can be split up into these components (in order):

A decimal number or an integer.
(Optional) An 'e' or 'E', followed by an integer.
A decimal number can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One of the following formats:
One or more digits, followed by a dot '.'.
One or more digits, followed by a dot '.', followed by one or more digits.
A dot '.', followed by one or more digits.
An integer can be split up into these components (in order):

(Optional) A sign character (either '+' or '-').
One or more digits.
For example, all the following are valid numbers: ["2", "0089", "-0.1", "+3.14", "4.", "-.9", "2e10", "-90E3", "3e+7", "+6e-1", "53.5e93", "-123.456e789"], while the following are not valid numbers: ["abc", "1a", "1e", "e3", "99e2.5", "--6", "-+3", "95a54e53"].

Given a string s, return true if s is a valid number.

Example 1:

	Input: s = "0"
	Output: true
	Example 2:

	Input: s = "e"
	Output: false
	Example 3:

	Input: s = "."
	Output: false
 
Constraints:

	1 <= s.length <= 20
	s consists of only English letters (both uppercase and lowercase), digits (0-9), plus '+', minus '-', or dot '.'.
'''

'''
要注意判断·前后的逻辑关系。ep:'0..'
'''
# faster than 50.20% of Python3
class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.replace('E', 'e')
        if 'e' in s:
            ie = s.index('e')
            before = self.isDec(s[:ie]) 
            after = self.isInt(s[ie+1:])
            if before and after:
                return True
            else:
                return False
        else:
            if self.isDec(s) :
                return True
            else:
                return False
            
    def isDec(self, s):
        s = self.removeChar(s)
        if not '.' in s:
            return self.isInt(s)
        idot = s.index('.')
        print(s[:idot], s[idot+1:])
        # before = s[:idot] and s[:idot].isdigit() 
        # after = s[idot+1:] and s[idot+1:].isdigit()  
        # if before or after: ❌
        sb, sa = s[:idot], s[idot+1:]
        before = sb and sb.isdigit()
        after = sa and sa.isdigit()
        if before and after or before and not sa or after and not sb:
            return True
        else:
            return False
        
        
    def isInt(self, s):
        s = self.removeChar(s)
        return s.isdigit()
        
    def removeChar(self, s):
        if s.startswith('+') or s.startswith('-'):
            return s[1:]
        return s