'''
91. Decode Ways

Share
A message containing letters from A-Z can be encoded into numbers using the following mapping:

'A' -> "1"
'B' -> "2"
...
'Z' -> "26"
To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

"AAJF" with the grouping (1 1 10 6)
"KJF" with the grouping (11 10 6)
Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

Given a string s containing only digits, return the number of ways to decode it.

The answer is guaranteed to fit in a 32-bit integer.
'''


'''
新双 = 旧单
新单 = 旧sum(单+双)
'''
def addNum(nums, pren, n):
    one, two = nums
    if one and int(pren+n) < 27:
        nums[1] = one
    else:
        nums[1] = 0
    if n != '0':
        nums[0] = one + two
    else:
        nums[0] = 0
    return nums
    
def numDecodings(s: str) -> int:
    if not s or s[0] == '0':
        return 0
    if len(s) == 1:
        return 1
    nums = [1,0]
    
    for i in range(1, len(s)):
        nums = self.addNum(nums, s[i-1], s[i])

    return sum(nums)


'''
dp
dp[i] = dp[i-2] + dp[i-1]
但是有条件限制：
如果前一位合法(1-9)，dp[i]就+上dp[i-1]
如果前两位合法(10-26),dp[i]就+上dp[i-2]

dp 长度是len+1
这样做的时候默认dp[0]合法，如果s[1]合法，dp[1]就=1
'''
    def numDecodings(self, s: str) -> int:
        if not s or s[0] == '0':
            return 0
        if len(s) == 1:
            return 1
        dp = [0] * (len(s) + 1)
        dp[0] = 1
        dp[1] = 1 if s[1] != '0' else 0
        for i in range(2, len(s)+1):
            if s[i-1] != '0':
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) < 27:
                dp[i] += dp[i-2]         
        return dp[-1]