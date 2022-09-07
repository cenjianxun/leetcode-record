'''
856. Score of Parentheses

Given a balanced parentheses string s, return the score of the string.

The score of a balanced parentheses string is based on the following rule:

"()" has score 1.
AB has score A + B, where A and B are balanced parentheses strings.
(A) has score 2 * A, where A is a balanced parentheses string.
 

Example 1:

    Input: s = "()"
    Output: 1
    Example 2:

    Input: s = "(())"
    Output: 2
    Example 3:

    Input: s = "()()"
    Output: 2
 

Constraints:

    2 <= s.length <= 50
    s consists of only '(' and ')'.
    s is a balanced parentheses string.
'''

def scoreOfParentheses(self, s: str) -> int:
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(s[i])
        elif s[i] == ')':
            p = stack.pop()
            if p == '(':
                stack.append(1)
            else:
                if stack:
                    q = stack.pop()
                    while q != '(':
                        p = p + q
                        q = stack.pop()
                    if q == '(':
                        p = 2 * p
                stack.append(p)
        # print(i, stack)
    return sum(stack) 

'''
还可以有很多方法
'''

'''
必须一次动态，不能分两次循环

）才计算：
看左边：如果是(才计算：
    count + 1
    结果要分情况：①i-1是(: 为1； ②i-1是):为前一个结果+1
    如果左边的前一个存在且是)：
        count+1
        结果算和
'''

# faster than 23.43% of Python3
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        res = [0] * len(s)
        count = [0] * len(s)
        print(list(range(len(s))))
        print(list(s))
        for i in range(len(s)):
            if s[i] == ')':
                left = i - count[i-1] * 2 - 1
                if s[left] == '(':
                    count[i] = count[i-1] + 1
                    if s[i-1] == '(':
                        res[i] = 1
                    else:
                        res[i] = 2 * res[i-1]
                    if left > 0 and s[left-1] == ')':
                        count[i] = count[left-1] + count[i]
                        res[i] = res[i] + res[left-1]
        print(count)
        print(res)        
        return res[-1]


class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = [0]
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(0)
            else:
                pre = stack.pop()
                stack[-1] += max(2*pre, 1)
            print(i, stack)
        return stack.pop()

# ======
class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(s[i])
            elif s[i] == ')':
                score = 0
                while stack[-1] != '(':
                    score += stack.pop()
                stack.pop()
                if score == 0:                
                    stack.append(1)
                else:
                    stack.append(score * 2)
        return sum(stack) 