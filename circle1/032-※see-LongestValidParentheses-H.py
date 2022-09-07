'''
32. Longest Valid Parentheses

Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.
'''

'''
方法是记录隔断点（）无效点，然后隔断。
注意点是遍历隔断点时，要在后面在加一个len(s), 为了遍历到尾
'''
# faster than 20.06% of Python3
def longestValidParentheses(self, s: str) -> int:
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        if s[i] == ')':
            if stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
    count = 0
    pre = 0
    stack.append(len(s))
    for i in stack:
        count = max(count, self.helper(s[pre:i]))
        pre = i
    return count * 2

def helper(self, s):
    count = 0
    if not s:
        return count
    stack = []
    for p in s:
        if p == '(':
            stack.append(p)
        if p == ')':
            if stack and stack[-1] == '(':
                stack.pop()
                count = count + 1
    return count


'''
统计长度根本就是它本身的长度就可以了！
'''
def longestValidParentheses(self, s: str) -> int:
    stack = []
    for i in range(len(s)):
        if s[i] == '(':
            stack.append(i)
        if s[i] == ')':
            if stack and s[stack[-1]] == '(':
                stack.pop()
            else:
                stack.append(i)
    count = 0
    pre = -1 # pre = 0
    stack.append(len(s))
    print(stack)
    for i in stack:
#             count = max(count, self.helper(s[pre:i]))
#             pre = i
#         return count * 2

#     def helper(self, s):
#         count = 0
#         if not s:
#             return count
#         stack = []
#         for p in s:
#             if p == '(':
#                 stack.append(p)
#             if p == ')':
#                 if stack and stack[-1] == '(':
#                     stack.pop()
#                     count = count + 1
#         return count
        count = max(count, i - pre - 1)
        pre = i
    return count


'''
动态规划真的很难想
1. 只有）需要计数
2. j表示当前)对应的(，所以当i和j不相邻的时候，再往回找的步长是s[i-1]
3. 当前的累计算两遍，第一遍算当前的套里面count是多少，第二层要加，当前套之前的一位，就是上一个套结尾，可不可用加上来


22.5.29
对于）只有两种情况：
1是看它对应的（在哪里
2是看它对应的（前一格有没有需要累加的
'''
def longestValidParentheses(self, s: str) -> int:
    if not s:
        return 0
    dp = [0] * len(s)
    for i in range(1, len(s)):
        if s[i] == ')':
            j = i - 1 - dp[i-1]
            if j >= 0 and s[j] == '(':
                dp[i] = dp[i-1] + 2 
                if j > 0:
                    dp[i] = dp[i] + dp[j - 1]
                # print(i, j, dp)
    return max(dp)