'''
https://leetcode.com/problems/flip-string-to-monotone-increasing/
Flip String to Monotone Increasing

A binary string is monotone increasing if it consists of some number of 0's (possibly none), followed by some number of 1's (also possibly none).

You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.

Return the minimum number of flips to make s monotone increasing.

Example 1:

Input: s = "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: s = "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: s = "00011000"
Output: 2
Explanation: We flip to get 00000000.
'''

'''
遍历，每一个i的之前的1的个数和之后的0的个数
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        preSum = [0]
        for c in s:
            preSum.append(preSum[-1] + int(c))
        res = float('inf')
        for i in range(len(s)+1):
            res = min(res, preSum[i] + len(s)-i-(preSum[-1] - preSum[i]))
        return res

'''
dp
有两个状态，加横向遍历，故是2维
dp[i][1] 表示变1的次数
转移方程 
i的0 = i-1的0 + 本i要是1就多一次
i的1 = i-1选1和0里更小的 + 本i要是0就多一次。 本i要是1的话，前面是0是1都可以
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        dp = [[0, 0] for _ in range(len(s) + 1)]
        for i in range(len(s)):
            dp[i+1][0] = dp[i][0] + int(s[i])
            dp[i+1][1] = min(dp[i][0], dp[i][1]) + 1 - int(s[i])
        return min(dp[-1][0], dp[-1][1])

'''
降到1维
'''
class Solution:
    def minFlipsMonoIncr(self, s: str) -> int:
        preCount = [0, 0]
        for i in range(len(s)):
            cur0 = preCount[0] + int(s[i])
            cur1 = min(preCount[0], preCount[1]) + 1 - int(s[i])
            preCount = [cur0, cur1]
        return min(preCount)