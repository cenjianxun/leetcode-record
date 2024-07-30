'''
316. Remove Duplicate Letters = 1081
Medium

Given a string s, return the lexicographically smallest subsequence of s that contains all the distinct characters of s exactly once.

Example 1:

    Input: s = "bcabc"
    Output: "abc"
Example 2:

    Input: s = "cbacdcbc"
    Output: "acdb"
 
Constraints:

    1 <= s.length <= 1000
    s consists of lowercase English letters.
'''

'''
bcabc
根本就不存在[b,c,a]，进a时就已经把bc pop掉了
stack不是在进第二个b的时候才判断，而是在a的时候就判断；
stack不是判断a本身，而是判断a前一个（在后面有没有）
'''
def removeDuplicateLetters(self, s: str) -> str:
    stack, count, seen = [], Counter(s), set()
    # print(marked)
    for i, e in enumerate(s):
        if e not in stack:
            while stack and e < stack[-1] and stack[-1] in s[i:]:
                stack.pop()
            stack.append(e)
        print(e, stack)
    return ''.join(stack)

'''
每个字母都有自己的计数，
之所以单调栈之前要判断是否c没有在stack里面，
是因为c如果在stack里面，就表示它已经出现在了更高位，更高位一定是更优解。所以c一但进去就固定了 不用再出来了
'''
class Solution:
    def smallestSubsequence(self, s: str) -> str:
        stack = []
        count = collections.Counter(s)
        for c in s:
            if c not in stack:
                while stack and count[stack[-1]] > 0 and stack[-1] > c:
                    stack.pop()
                stack.append(c)   
            count[c] -= 1
        return ''.join(stack)