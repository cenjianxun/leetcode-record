'''
678. Valid Parenthesis String
Medium

Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.

The following rules define a valid string:

Any left parenthesis '(' must have a corresponding right parenthesis ')'.
Any right parenthesis ')' must have a corresponding left parenthesis '('.
Left parenthesis '(' must go before the corresponding right parenthesis ')'.
'*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
 
Example 1:

	Input: s = "()"
	Output: true

Example 2:

	Input: s = "(*)"
	Output: true

Example 3:

	Input: s = "(*))"
	Output: true
 
Constraints:

	1 <= s.length <= 100
	s[i] is '(', ')' or '*'.
'''

'''
不会

左不是值而是一个范围，匹配到了右就-1，但是这个范围的下限是正数，
为什么可以直接把负数置成0，是因为，负数表示左（欠缺，右）多，而下限表示这个多，是由于*当成）才多的，那么都多了就不把*当成）不就完了。
如果max值都不够，那就表示真的不行，就直接false
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        minleft = maxleft = 0
        for c in s:
            if c == '(':
                minleft += 1
                maxleft += 1
            if c == ')':
                minleft = max(0, minleft - 1)
                maxleft -= 1
            if c == '*':
                minleft = max(0, minleft - 1)
                maxleft += 1
            if maxleft < 0:
                return False
        return minleft == 0

'''
栈方法：
用两个栈保存left和star，来匹配） 
【在途中时匹配不计顺序，可以跳过更近的*匹配更远的（】
但是一旦出现（，（之前的*就不能当作）来匹配比这个（之前的*

即：
*当作（时匹配）不考虑顺序，因为一定是往前找的，正常顺序就是先（后）
但*当）时匹配（要考虑要顺序，因为它）只能匹配比它早的（

在stack里记录的是index，遍历完毕之后要匹配left和star，即把star当作）来用，这时就要考虑顺序
'''
class Solution:
    def checkValidString(self, s: str) -> bool:
        left, star = [], []
        for i, char in enumerate(s):
            if char == '(':
                left.append(i)
            if char == '*':
                star.append(i)
            if char == ')':
                if left:
                    left.pop()
                elif star:
                    star.pop()
                else:
                    return False
        while star:
            if not left:
                return True
            if left[-1] < star[-1]:
                left.pop()
                star.pop()
            else:
                return False
        if left:
            return False
        return True