'''
1542. Find Longest Awesome Substring
Hard

You are given a string s. An awesome substring is a non-empty substring of s such that we can make any number of swaps in order to make it a palindrome.

Return the length of the maximum length awesome substring of s.

Example 1:

    Input: s = "3242415"
    Output: 5
    Explanation: "24241" is the longest awesome substring, we can form the palindrome "24142" with some swaps.

Example 2:

    Input: s = "12345678"
    Output: 1

Example 3:

    Input: s = "213123"
    Output: 6
    Explanation: "213123" is the longest awesome substring, we can form the palindrome "231132" with some swaps.
 
Constraints:

    1 <= s.length <= 105
    s consists only of digits.
'''

'''
超时
'''
class Solution:
    def longestAwesome(self, s: str) -> int:
        res = 0
        pattern = 0
        preCountOne = collections.defaultdict(dict)
        preCountOne[0][0] = -1
        for i, c in enumerate(s):
            pattern ^= 1<<int(c)
            countOne = str(bin(pattern)).count('1')
            for cOne in (-1, 0, 1):
                restOne = countOne - cOne
                if restOne in preCountOne:
                    for pa in preCountOne[restOne]:
                        restPa = pattern ^ pa
                        if str(bin(restPa)).count('1') < 2:
                            res = max(res, i - preCountOne[restOne][pa])            
            #print(res)
            if countOne not in preCountOne or pattern not in preCountOne[countOne]:
                preCountOne[countOne][pattern] = i
            #print(i, c, str(bin(pattern)), preCountOne)
        return res

'''
找只差1个1的是遍历0-9，然后又取异或
遍历到10 并且&1023是为了取异或0，就是没一位变的还是原值的那种情况 
'''
class Solution:
    def longestAwesome(self, s: str) -> int:
        res = 0
        status = 0
        preCountOne = [float('inf')] * (2 ** 10)
        preCountOne[0] = -1
        for i, c in enumerate(s):
            status ^= 1<<(int(c))
            for k in range(11):
                restStatus = (status ^ (1<<k)) & 1023
                if preCountOne[restStatus] != float(inf):
                    res = max(res, i - preCountOne[restStatus])
            preCountOne[status] = min(preCountOne[status], i)          
        return res