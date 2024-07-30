'''
1249. Minimum Remove to Make Valid Parentheses
Medium

Given a string s of '(' , ')' and lowercase English characters.

Your task is to remove the minimum number of parentheses ( '(' or ')', in any positions ) so that the resulting parentheses string is valid and return any valid string.

Formally, a parentheses string is valid if and only if:

It is the empty string, contains only lowercase characters, or
It can be written as AB (A concatenated with B), where A and B are valid strings, or
It can be written as (A), where A is a valid string.
 
Example 1:

	Input: s = "lee(t(c)o)de)"
	Output: "lee(t(c)o)de"
	Explanation: "lee(t(co)de)" , "lee(t(c)ode)" would also be accepted.

Example 2:

	Input: s = "a)b(c)d"
	Output: "ab(c)d"

Example 3:

	Input: s = "))(("
	Output: ""
	Explanation: An empty string is also valid.
'''

'''
注意j的范围
'''
# faster than 19.45% of Python3
class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i] == ')':
                if stack and s[stack[-1]] == '(':
                    stack.pop()
                else:
                    stack.append(i)
            if s[i] == '(':
                stack.append(i)
        res = ''
        j = 0
        for i in range(len(s)):
            if j < len(stack) and i == stack[j]:
                j += 1
            else:
                res += s[i]
        return res